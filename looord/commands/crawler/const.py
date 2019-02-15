headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 '
        'Safari/537.36'
}

# for simple info crawling
stat_card_idx = [
    'ranked_stats',
    'casual_stats',
    'overall_stats',
    'team_play',
    'kills_breakdown',
    'secure_stats',
    'bomb_stats',
    'hostage_stats',
]

stat_section_idx = [  # only for ranked_stats, casual_stats, overall_stats
    'time played',
    'matched played',
    'kills/match',
    'kills',
    'deaths',
    'k/d ratio',
    'wins',
    'losses',
    'w/l ratio',
]

kills_breakdown_idx = [  # only for kills_breakdown
    'total kills',
    'blind kills',
    'melee kills',
    'penetration kills',
    'headshots',
    'headshot %',
]
