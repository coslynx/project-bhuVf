role_management.py

# Python code for role management functionality

import discord
from discord.ext import commands

class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='assign_role')
    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been assigned the {role.name} role.')
        except discord.Forbidden:
            await ctx.send('I do not have permission to assign roles.')
        except discord.HTTPException:
            await ctx.send('An error occurred while assigning the role.')

    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f'{role.name} role has been removed from {member.mention}.')
        except discord.Forbidden:
            await ctx.send('I do not have permission to remove roles.')
        except discord.HTTPException:
            await ctx.send('An error occurred while removing the role.')

def setup(bot):
    bot.add_cog(RoleManagement(bot))