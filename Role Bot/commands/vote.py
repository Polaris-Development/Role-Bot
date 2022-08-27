import discord
from discord import app_commands
from discord.ext import commands
import json

class vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vote(self, ctx, member: discord.Member, role: discord.Role):
        print(member.id)
        print(role.id)
        if role.id in self.bot.allowedroles:
            try:
                count = self.bot.data[str(member.id)][str(role.id)]["count"] + 1
                self.bot.data[str(member.id)][str(role.id)] = {"count": count}
                    
            except:
                self.bot.data[str(member.id)][str(role.id)] = {"count": 1}

            count = self.bot.data[str(member.id)][str(role.id)]["count"]
            if count >= self.bot.rolecount:
                await member.add_roles(role)
                await ctx.send(f"{member.name} has reached enough votes! {role.name} given.")
                self.bot.data[str(member.id)][str(role.id)] = {"count": 0}
            else:
                await ctx.send(f"You have voted to give {member.name} the {role.name} role!\nCurrent Votes: {count}")


            with open(self.bot.filename, "w") as file:
                json.dump(self.bot.data,file, indent=2)
        else:
            await ctx.send(f"You can not vote to give a user that role!")

async def setup(bot):
    await bot.add_cog(vote(bot))