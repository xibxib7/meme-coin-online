# def format_token_info(token):
#     text = f"🪙 آدرس توکن: {token.get('tokenAddress')}\n"
#     text += f"🌐 لینک: {token.get('url')}\n"
#     text += f"🖼️ آیکون: {token.get('icon')}\n"

#     links = token.get("links", [])
#     if links:
#         for link in links:
#             link_type = link.get("type", "ناشناخته")
#             link_url = link.get("url", "ندارد")
#             text += f"🔗 {link_type}: {link_url}\n"
#     else:
#         text += "🔗 بدون لینک‌های اجتماعی\n"

#     return text


def format_token_info(token):
    text = f"🪙 <b>Token Address:</b> {token.get('tokenAddress')}\n\n"
    text += f"🌐 <b>DEXScreener Link:</b> {token.get('url')}\n\n"
    text += f"🖼️ <b>Icon:</b> {token.get('icon')}\n\n"

    links = token.get("links", [])
    links = token.get("links", [])
    if links:
        text += "🔗 <b>Social Links:</b>\n"
        for link in links:
            link_type = link.get("type", "Unknown").capitalize()
            link_url = link.get("url", "Unavailable")
            text += f"  • {link_type}: {link_url}\n"
    else:
        text += "🔗 <b>Social Links:</b> None\n"

    return text