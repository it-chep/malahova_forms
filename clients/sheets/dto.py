from dataclasses import dataclass
from typing import Optional


@dataclass
class NewProductData:
    source: Optional[str] = None
    bought_products: Optional[str] = None
    city: Optional[str] = None
    age: Optional[str] = None
    specialization: Optional[str] = None
    income_rub: Optional[str] = None
    operations_status: Optional[str] = None
    study_goal: Optional[str] = None
    current_difficulties: Optional[str] = None
    attempted_solutions: Optional[str] = None
    subscription_info: Optional[str] = None
    top_questions: Optional[str] = None
    warmup_level: Optional[str] = None
    workload_level: Optional[str] = None
    full_name: Optional[str] = None
    instagram: Optional[str] = None
    telegram_channel: Optional[str] = None
    telegram: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    policy_agreement: bool = False

    @classmethod
    def from_model(cls, model_instance) -> "NewProductData":
        return cls(
            source=model_instance.get_source_display(),
            bought_products=model_instance.get_bought_products_display(),
            city=model_instance.city,
            age=model_instance.age,
            specialization=model_instance.specialization,
            income_rub=model_instance.income_rub,
            operations_status=model_instance.get_operations_status_display(),
            study_goal=model_instance.study_goal,
            current_difficulties=model_instance.current_difficulties,
            attempted_solutions=model_instance.attempted_solutions,
            subscription_info=model_instance.subscription_info,
            top_questions=model_instance.top_questions,
            warmup_level=model_instance.get_warmup_level_display(),
            workload_level=model_instance.get_workload_level_display(),
            full_name=model_instance.full_name,
            instagram=model_instance.instagram,
            telegram_channel=model_instance.telegram_channel,
            telegram=model_instance.telegram,
            phone=model_instance.phone,
            email=model_instance.email,
            policy_agreement=model_instance.policy_agreement,
        )
