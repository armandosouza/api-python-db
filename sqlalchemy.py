from typing import List
from sqlalchemy import String, ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase):
	pass

class Cliente(Base):
	__tablename__ = "cliente"

	id: Mapped[int] = mapped_column(primary_key=True)
	nome: Mapped[str]
	cpf: Mapped[str] = mapped_column(String(9))
	endereco: Mapped[str] = mapped_column(String(9))

	contas: Mapped[List["Conta"]] = relationship(
		back_populates="cliente", cascade="all, delete-orphan"
	)

	def __repr__(self):
		return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
	__tablename__ = "conta"

	id: Mapped[int] = mapped_column(primary_key=True)
	tipo: Mapped[str]
	agencia: Mapped[str]
	num: Mapped[int]
	id_cliente: Mapped[int] = mapped_column(ForeignKey("cliente.id"))
	saldo: Mapped[float]

	cliente: Mapped["Cliente"] = relationship(back_populates="contas")

	def __repr__(self):
		return f"Conta(id: {self.id}, tipo: {self.tipo}, agencia: {self.agencia}, num: {self.num}, saldo: {self.saldo})"

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
	cliente1 = Cliente(
		nome="Armando Souza",
		cpf="123456789",
		endereco="Rua A",
		contas=[
			Conta(tipo="CC", agencia="0001", num=1, saldo=0)
		]
	)

	cliente2 = Cliente(
		nome="Ana Souza",
		cpf="123456759",
		endereco="Rua C",
		contas=[
			Conta(tipo="CC", agencia="0001", num=2, saldo=0),
			Conta(tipo="CP", agencia="0001", num=3, saldo=0)
		]
	)

	session.add_all([cliente1, cliente2])
	session.commit()

session = Session(engine)

statement = select(Cliente).where(Cliente.nome.in_(["Souza"]))
for user in session.scalars(statement):
	print(user)