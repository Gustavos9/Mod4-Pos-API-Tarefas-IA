import unicodedata
from typing import Optional


class AITaskService:

  @staticmethod
  def analyze_priority(title: str, description: Optional[str] = None) -> str:
    """Analisa o texto da tarefa e sugere uma prioridade com base em palavras-chave,

    removendo acentos automaticamente para maior robustez.
    """
    raw_text = f"{title} {description or ''}".lower()

    # Remove acentos e diacríticos (ex: 'reunião' vira 'reuniao')
    text = "".join(
        c
        for c in unicodedata.normalize("NFD", raw_text)
        if unicodedata.category(c) != "Mn"
    )

    if any(word in text for word in ["urgente", "critico", "producao", "erro"]):
      return "alta"
    elif any(word in text for word in ["reuniao", "documentacao", "ajuste"]):
      return "média"
    else:
      return "baixa"
