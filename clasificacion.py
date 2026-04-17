import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot ecológico conectado como {bot.user}')
# Diccionario de residuos
residuos = {
    "plastico": "♻️ Reciclable",
    "botella de plastico": "♻️ Reciclable",
    "bolsa de plastico": "♻️ Reciclable",
    "papel": "♻️ Reciclable",
    "carton": "♻️ Reciclable",
    "vidrio": "♻️ Reciclable",
    "botella de vidrio": "♻️ Reciclable",
    "lata": "♻️ Reciclable",
    "aluminio": "♻️ Reciclable",
    "tela": "♻️ Reciclable",
    "banana": "🌱 Orgánico",
    "manzana": "🌱 Orgánico",
    "restos de comida": "🌱 Orgánico",
    "pañal": "🗑️ Basura",
    "colilla": "🗑️ Basura",
    "papel higienico": "🗑️ Basura",
    "bateria": "⚠️ Desecho especial",
    "pilas": "⚠️ Desecho especial"
}
# Tiempo de descomposición de materiales
tiempos_descomposicion = {
    "plastico": "500 años",
    "botella de plastico": "500 años",
    "bolsa de plastico": "500 años",
    "papel": "2-6 meses",
    "carton": "5 años",
    "vidrio": "1 millón de años",
    "botella de vidrio": "1 millón de años",
    "lata": "200-500 años",
    "aluminio": "200-500 años",
    "tela": "1-5 años",
    "banana": "2-10 días",
    "manzana": "1-2 semanas",
    "restos de comida": "1-2 semanas",
    "pañal": "450 años",
    "colilla": "10-15 años",
    "papel higienico": "1-3 meses",
    "bateria": "No se descompone fácilmente, debe reciclarse en un punto de recogida",
    "pilas": "No se descomponen fácilmente, deben reciclarse en un punto de recogida"
}
# Lista de recomendaciones aleatorias para el reciclaje
recomendaciones_reciclaje = [
    "Recuerda separar los materiales reciclables en contenedores diferentes para facilitar el proceso.",
    "Reutiliza las bolsas de plástico en lugar de tirarlas para reducir el consumo.",
    "Compra productos con menos embalaje para generar menos residuos.",
    "Participa en campañas de limpieza de playas o parques para cuidar el medio ambiente.",
    "Educa a tus amigos y familia sobre la importancia del reciclaje.",
    "Usa botellas reutilizables en lugar de botellas de un solo uso.",
    "Composta tus restos orgánicos para crear abono natural para plantas.",
    "Evita tirar baterías en la basura común; llévalas a puntos de reciclaje específicos."
]
@bot.command()
async def residuo(ctx, *, nombre):
    nombre = nombre.lower()
    if nombre in residuos:
        recomendacion = random.choice(recomendaciones_reciclaje)
        await ctx.send(f"🔍 **{nombre}** → {residuos[nombre]}\n💡 **Recomendación ecológica:** {recomendacion}")
    else:
        await ctx.send(
            f"🤔 No sé qué hacer con **{nombre}**.\n"
            "Pregunta a un experto o revisa normas locales."
        )

@bot.command()
async def recomendacion(ctx):
    recomendacion = random.choice(recomendaciones_reciclaje)
    await ctx.send(f"💡 **Recomendación ecológica:** {recomendacion}")

@bot.command()
async def descomposicion(ctx):
    texto = "**Lista de descomposición de residuos:**\n"
    for material, tiempo in tiempos_descomposicion.items():
        texto += f"- **{material}**: {tiempo}\n"
    await ctx.send(texto)

bot.run("MTQ4NjkwNDUwMTY5OTg3MDkxMg.G3ml8S.FUkyIiIgbBI3kMYE_n68TZjzN9c4URhksFmHmU")
