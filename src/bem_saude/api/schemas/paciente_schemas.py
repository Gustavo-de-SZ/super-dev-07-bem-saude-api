from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, Field


class PacienteCriarRequest(BaseModel):

    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome completo do paciente",
        examples=["Maria da Silva"]
    )

    telefone: str | None = None
    cpf: str | None = None
    data_nascimento: date | None = None
    email: str | None = None
    endereco: str | None = None
    observacoes: str | None = None
    status: bool


class PacienteAlterarRequest(BaseModel):

    id: UUID = Field(
        ...,
        description="Identificador unico do paciente",
        examples=["019c445a-d6d3-7353-a9cf-66626a819a4a"]
    )

    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome completo do paciente"
    )

    telefone: str | None = None
    email: str | None = None
    endereco: str | None = None
    observacoes: str | None = None


class PacienteResponse(BaseModel):

    id: UUID
    nome: str
    telefone: str | None
    cpf: str | None
    data_nascimento: date | None
    email: str | None
    endereco: str | None
    observacoes: str | None
    status: bool
    criado_em: datetime
    alterado_em: datetime | None
