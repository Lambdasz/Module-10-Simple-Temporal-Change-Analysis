
"""M10.5 - Tree Count Change"""


def calculate_tree_count_change(before_counts, after_counts):
    """
    Membandingkan jumlah pohon pada dua periode.

    before_counts dan after_counts berbentuk:
    {location_id: jumlah_pohon}
    """

    if not isinstance(before_counts, dict):
        raise TypeError("before_counts harus berupa dictionary")

    if not isinstance(after_counts, dict):
        raise TypeError("after_counts harus berupa dictionary")

    if set(before_counts) != set(after_counts):
        raise ValueError(
            "Lokasi pada kedua periode harus sama"
        )

    for location_id in before_counts:
        for count in (before_counts[location_id], after_counts[location_id]):
            if not isinstance(count, int) or isinstance(count, bool):
                raise TypeError("Jumlah pohon harus berupa bilangan bulat")

            if count < 0:
                raise ValueError("Jumlah pohon tidak boleh negatif")

    return [
        {
            "location_id": location_id,
            "before": before_counts[location_id],
            "after": after_counts[location_id],
            "change": after_counts[location_id] - before_counts[location_id],
            "direction": (
                "bertambah"
                if after_counts[location_id] > before_counts[location_id]
                else "berkurang"
                if after_counts[location_id] < before_counts[location_id]
                else "tetap"
            ),
        }
        for location_id in sorted(before_counts)
    ]


# ==========================================
# DATA DUMMY DAN PENGUJIAN M10.5
# ==========================================

if __name__ == "__main__":
    before_counts = {
        "area-A": 120,
        "area-B": 80,
        "area-C": 50,
    }

    after_counts = {
        "area-A": 105,
        "area-B": 95,
        "area-C": 50,
    }

    results = calculate_tree_count_change(
        before_counts,
        after_counts,
    )

    print("=== M10.5 TREE COUNT CHANGE ===")

    for item in results:
        print(
            f'{item["location_id"]}: '
            f'{item["before"]} -> {item["after"]} pohon '
            f'({item["direction"]}, perubahan {item["change"]:+d})'
        )

    print("\n=== PENGUJIAN TAMBAHAN M10.5 ===")

    # Tes 1: Lokasi berbeda
    try:
        calculate_tree_count_change(
            {"area-A": 100},
            {"area-B": 90},
        )
    except ValueError:
        print("[LULUS] Lokasi berbeda terdeteksi")

    # Tes 2: Input tidak berubah
    before_original = before_counts.copy()
    after_original = after_counts.copy()

    calculate_tree_count_change(before_counts, after_counts)

    if (
        before_counts == before_original
        and after_counts == after_original
    ):
        print("[LULUS] Data input tetap sama")

    # Tes 3: Jumlah pohon negatif
    try:
        calculate_tree_count_change(
            {"area-A": -5},
            {"area-A": 10},
        )
    except ValueError:
        print("[LULUS] Jumlah pohon negatif ditolak")

    # Tes 4: Jumlah pohon bukan bilangan bulat
    try:
        calculate_tree_count_change(
            {"area-A": 10.5},
            {"area-A": 12},
        )
    except TypeError:
        print("[LULUS] Jumlah pohon non-integer ditolak")
