from app.services.ai_service import AITaskService

def test_ai_priority_high():
    priority = AITaskService.analyze_priority("Erro crítico no servidor de produção")
    assert priority == "alta"

def test_ai_priority_medium():
    priority = AITaskService.analyze_priority("Reunião de alinhamento com equipe")
    assert priority == "média"

def test_ai_priority_low():
    priority = AITaskService.analyze_priority("Comprar café para o escritório")
    assert priority == "baixa"
