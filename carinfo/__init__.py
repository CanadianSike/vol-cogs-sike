from .carinfo import CarInfo


async def setup(bot):
    await bot.add_cog(CarInfo(bot))