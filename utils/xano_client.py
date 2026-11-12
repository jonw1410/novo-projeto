"""
EduTrack AI - Xano Client & URL Resolver
Handles dynamic endpoint resolution, automatic fallback between API groups,
and detailed diagnostic formatting for Xano connections.
"""

import os
from typing import Any, Dict, List, Tuple
import requests
from dotenv import load_dotenv

load_dotenv()


def get_endpoint_urls() -> Dict[str, str]:
    """
    Resolve base URLs for Auth, Subjects, and Tasks groups.
    Supports individual group URLs or derives them from XANO_BASE_URL.
    """
    base_url = os.getenv("XANO_BASE_URL", "").rstrip("/")
    
    # Extract host prefix, e.g. https://x8ki-letl-twmt.n7.xano.io
    if "/api:" in base_url:
        host = base_url.split("/api:")[0]
    else:
        host = base_url

    # Canonical IDs from .xs files
    # Subjects canonical: WTDGU8XU
    # Tasks canonical: VIQ0W9tI
    # Auth canonical: cPkbqL8B
    subjects_base = os.getenv("XANO_SUBJECTS_BASE_URL", "").rstrip("/") or f"{host}/api:WTDGU8XU"
    tasks_base = os.getenv("XANO_TASKS_BASE_URL", "").rstrip("/") or f"{host}/api:VIQ0W9tI"
    auth_base = base_url or f"{host}/api:cPkbqL8B"

    return {
        "host": host,
        "auth": auth_base,
        "subjects": subjects_base,
        "tasks": tasks_base,
        "fallback_subjects": f"{base_url}/subjects",
        "fallback_tasks": f"{base_url}/academic_tasks",
    }


def parse_xano_error(err: requests.RequestException) -> Dict[str, Any]:
    """Parse HTTP exception into structured diagnostic information."""
    info = {
        "status_code": getattr(err.response, "status_code", None),
        "url": getattr(getattr(err, "request", None), "url", "Desconhecida"),
        "message": str(err),
        "hint": "",
    }
    
    if hasattr(err, "response") and err.response is not None:
        try:
            body = err.response.json()
            if isinstance(body, dict):
                info["message"] = body.get("message") or body.get("error") or str(body)
        except Exception:
            info["message"] = err.response.text or str(err)
            
    # Intelligent hints for common Xano errors
    msg = info["message"].lower()
    if "token belongs to a different object type" in msg:
        info["hint"] = (
            "O token JWT de autenticação foi gerado para a tabela 'user', mas o endpoint no Xano "
            "espera outro tipo ou está sem autenticação. Verifique se você fez o push das mudanças "
            "(.xs) com 'auth = \"user\"' para o Xano e refaça o login na página Perfil."
        )
    elif info["status_code"] == 404:
        info["hint"] = (
            "O endpoint não foi encontrado na URL chamada. Verifique se o endpoint está publicado "
            "no grupo de API correto no Xano (Canonical WTDGU8XU para Disciplinas, VIQ0W9tI para Tarefas)."
        )
    elif info["status_code"] == 401:
        info["hint"] = (
            "Não autorizado. Sua sessão pode ter expirado ou o token está inválido. "
            "Acesse a página de Perfil e faça login novamente."
        )
    elif "connection" in msg or "nameresolution" in msg:
        info["hint"] = (
            "Não foi possível conectar ao servidor do Xano. Verifique sua conexão com a internet "
            "e a URL configurada no arquivo .env."
        )
        
    return info


def request_with_fallback(
    method: str,
    primary_url: str,
    fallback_url: str,
    headers: Dict[str, str],
    json_data: Any = None,
    timeout: int = 10,
) -> Tuple[requests.Response, str]:
    """
    Attempt request on primary_url; if 404 occurs, retry on fallback_url.
    Returns (response, used_url).
    """
    try:
        resp = requests.request(method, primary_url, headers=headers, json=json_data, timeout=timeout)
        if resp.status_code == 404 and fallback_url and fallback_url != primary_url:
            fallback_resp = requests.request(method, fallback_url, headers=headers, json=json_data, timeout=timeout)
            if fallback_resp.status_code != 404:
                return fallback_resp, fallback_url
        return resp, primary_url
    except requests.RequestException:
        if fallback_url and fallback_url != primary_url:
            try:
                fallback_resp = requests.request(method, fallback_url, headers=headers, json=json_data, timeout=timeout)
                return fallback_resp, fallback_url
            except Exception:
                pass
        raise
