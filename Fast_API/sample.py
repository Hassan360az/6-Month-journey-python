# Bahut achha. Ab hum **SQLAlchemy Models** shuru karte hain.

# Lekin **seedha `declarative_base()` ya `Column` par nahi jayenge**, kyun ke agar intro nahi hoga to sab ratta lagega.

# Main waise hi padhaunga jaise aap ne kaha:

# > **Pehle kya hua → phir problem kya aayi → phir us problem ka solution kya hai → phir code kya karta hai.**

# ---

# # Step 1 - Abhi tak hum kya kar rahe the?

# Suppose hum user banana chahte hain.

# Client request bhejta hai.

# ```text
# POST /users

# Name = Hassan
# Age = 22
# ```

# ↓

# FastAPI function call karta hai.

# ```python
# def create_user():
# ```

# ↓

# Ab hame user database mein save karna hai.

# ---

# # Step 2 - Database ko kaise pata chalega "User" kya hota hai?

# Database khud nahi jaanta.

# Usay koi batayega.

# Example.

# Agar main bolun.

# ```text
# User Save Kar Do
# ```

# Database poochega.

# ```text
# User mein kya kya hoga?

# ID?

# Name?

# Email?

# Age?
# ```

# Usay structure chahiye.

# ---

# # Step 3 - Isi structure ko Model kehte hain.

# Model matlab

# > **Database ko batana ke table kaisi hogi.**

# Example

# Hum bolte hain.

# ```text
# User Table

# ----------------------

# ID

# Name

# Email

# Age
# ```

# Ab database samajh gaya.

# ---

# # SQLAlchemy mein Model kaise banta hai?

# Yahan se `declarative_base()` aata hai.

# ---

# # declarative_base() kya hai?

# Sabse pehle code dekho.

# ```python
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()
# ```

# Ab isko step by step samajho.

# ---

# ## Step 1

# Hum import karte hain.

# ```python
# from sqlalchemy.orm import declarative_base
# ```

# Yani SQLAlchemy se ek helper mang rahe hain.

# Abhi kuch nahi hua.

# Sirf import hua.

# ---

# ## Step 2

# Ye line chalti hai.

# ```python
# Base = declarative_base()
# ```

# Ab SQLAlchemy kehta hai.

# > "Theek hai."

# > "Main tumhare liye ek Base class bana deta hoon."

# Ye Base class special hoti hai.

# Ab jitni bhi tables banaoge.

# Sab isi Base se inherit karengi.

# ---

# # Real-life Example

# Socho ek school hai.

# Principal kehta hai.

# ```text
# School ka Rule Book
# ```

# Ab jitni bhi classes hongi.

# ```text
# Class 1

# Class 2

# Class 3

# Class 4
# ```

# Sab isi Rule Book ko follow karengi.

# `Base` bhi Rule Book ki tarah hai.

# Har model usi se banega.

# ---

# # Ab Model banate hain.

# ```python
# class User(Base):
# ```

# Is line ko samajho.

# ---

# ## Step 1

# Hum Python class bana rahe hain.

# ```python
# class User
# ```

# Ye normal Python class hai.

# ---

# ## Step 2

# Hum likhte hain.

# ```python
# (Base)
# ```

# Matlab

# > "Ye class Base ke rules follow karegi."

# Ab SQLAlchemy samajh gaya.

# > "Acha!"

# > "Ye normal Python class nahi."

# > "Ye database table banegi."

# ---

# # Ab Table ka naam dete hain.

# ```python
# __tablename__ = "users"
# ```

# Step by step.

# Hum SQLAlchemy ko bolte hain.

# ```text
# Database mein table ka naam

# users
# ```

# Ab database banega.

# ```text
# users
# ```

# ---

# # Ab Columns banate hain.

# ```python
# id = Column(Integer, primary_key=True)
# ```

# Is line ko dheere dheere samajho.

# ---

# ## Step 1

# Hum likhte hain.

# ```python
# id
# ```

# Yani table mein ek column hoga.

# Naam

# ```text
# id
# ```

# ---

# ## Step 2

# Hum likhte hain.

# ```python
# Column(...)
# ```

# SQLAlchemy kehta hai.

# > "Acha."

# > "Ye database ka column hai."

# ---

# ## Step 3

# Hum likhte hain.

# ```python
# Integer
# ```

# Yani

# ```text
# id

# ↓

# Sirf Number
# ```

# Example

# ```text
# 1

# 2

# 3

# 4
# ```

# String nahi.

# ---

# ## Step 4

# Hum likhte hain.

# ```python
# primary_key=True
# ```

# Ye bahut important hai.

# Database kehta hai.

# > "Har row ko uniquely identify karne ke liye ye column use hoga."

# Example

# ```text
# ID      Name

# 1       Ali

# 2       Hassan

# 3       Ahmed
# ```

# Kabhi bhi do rows ka ID same nahi hoga.

# ---

# # Name Column

# ```python
# name = Column(String)
# ```

# Step by step.

# Hum bolte hain.

# ```text
# Ek column aur banao.

# Naam

# name
# ```

# Type

# ```text
# String
# ```

# Example

# ```text
# Ali

# Hassan

# Ahmed
# ```

# ---

# # Age Column

# ```python
# age = Column(Integer)
# ```

# Database.

# ```text
# Age

# 18

# 20

# 25
# ```

# Sirf integer.

# ---

# # Email Column

# ```python
# email = Column(String)
# ```

# Example.

# ```text
# abc@gmail.com

# xyz@gmail.com
# ```

# ---

# # Complete Model

# ```python
# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String

# Base = declarative_base()

# class User(Base):

#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)

#     name = Column(String)

#     age = Column(Integer)

#     email = Column(String)
# ```

# ---

# # Ab SQLAlchemy kya karega?

# Ye model dekh kar SQL bana dega.

# ```sql
# CREATE TABLE users(

# id INTEGER PRIMARY KEY,

# name VARCHAR,

# age INTEGER,

# email VARCHAR

# );
# ```

# Hum ne SQL nahi likhi.

# SQLAlchemy ne khud bana di.

# ---

# # Complete Flow

# ```text
# Hum Python Model banate hain

# ↓

# SQLAlchemy Model padhta hai

# ↓

# SQL Query banata hai

# ↓

# Database ko bhejta hai

# ↓

# Database Table Create karta hai
# ```

# ---

# # Column Types

# ## Integer

# Sirf numbers.

# ```python
# age = Column(Integer)
# ```

# Example

# ```text
# 18

# 25

# 30
# ```

# ---

# ## String

# Text.

# ```python
# name = Column(String)
# ```

# Example

# ```text
# Ali

# Ahmed

# Hassan
# ```

# ---

# ## Boolean

# True ya False.

# ```python
# is_admin = Column(Boolean)
# ```

# Example

# ```text
# True

# False
# ```

# ---

# ## Float

# Decimal numbers.

# ```python
# price = Column(Float)
# ```

# Example

# ```text
# 99.99

# 10.5
# ```

# ---

# ## Date

# Sirf date.

# ```python
# dob = Column(Date)
# ```

# Example

# ```text
# 2026-07-13
# ```

# ---

# ## DateTime

# Date aur time dono.

# ```python
# created_at = Column(DateTime)
# ```

# Example

# ```text
# 2026-07-13 10:30:00
# ```

# ---

# # Sabse Important Concept

# Ye line:

# ```python
# id = Column(Integer, primary_key=True)
# ```

# **Step by step kya karti hai?**

# ```text
# id

# ↓

# Ye column ka naam hai

# ↓

# Column()

# ↓

# SQLAlchemy ko batata hai ke ye database column hai

# ↓

# Integer

# ↓

# Is column mein sirf integer values hongi

# ↓

# primary_key=True

# ↓

# Ye har row ki unique pehchan hogi
# ```

# ---

# ## 📌 Ek baat yaad rakhna

# * **`declarative_base()`** = SQLAlchemy ka **base/rule book** hai. Har model isi se inherit karta hai.
# * **Model (`class User(Base)`)** = Database table ka Python version.
# * **`Column()`** = Table ka ek field/column define karta hai.
# * **`Integer`, `String`, `Boolean`, `Float`...** = Column kis type ka data store karega.
# * **`primary_key=True`** = Is column ki value har row ke liye unique hogi aur us row ki pehchan hogi.

# Yani pehle hum **Python mein model banate hain**, phir **SQLAlchemy us model ko dekh kar database mein table create karne ki information tayar karta hai.**
# # 