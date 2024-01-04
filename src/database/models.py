from . import db
from sqlalchemy.orm import Mapped, mapped_column


class Occurance(db.Model):
    __tablename__ = 'Occurances'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String)
