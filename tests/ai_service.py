class AITaskService:

  @staticmethod
  def analyze_priority(title: str, description: Optional[str] = None) -> str:
    """Analisa o texto da tarefa e sugere uma prioridade com base em palavras-chave."""
    text = f"{title} {description or ''}".lower()

    if any(
        word in text for word in ["urgente", "critico", "producao", "erro"]
    ):
      return "alta"
    elif any(word in text for word in ["reuniao", "documentacao", "ajuste"]):
      return "média"
    else:
      return "baixa"