from .carinfo import carinfo


async def setup(bot):
    await bot.add_cog(carinfo(bot))