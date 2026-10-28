
"""M10.4 - Land-Cover Change"""


def identify_land_cover_changes(before_classes, after_classes):
    """Bandingkan kelas tutupan lahan dari dua periode."""

    if not isinstance(before_classes, dict):
        raise TypeError("before_classes harus berupa dictionary")

    if not isinstance(after_classes, dict):
        raise TypeError("after_classes harus berupa dictionary")

    if set(before_classes) != set(after_classes):
        raise ValueError(
            "Lokasi pada kedua periode harus sama"
        )

    return [
        {
            "location_id": location_id,
            "before": before_classes[location_id],
            "after": after_classes[location_id],
            "changed": (
                before_classes[location_id]
                != after_classes[location_id]
            ),
        }
        for location_id in sorted(before_classes)
    ]


def get_changed_areas(results):
    """Mengambil lokasi yang mengalami perubahan."""
    return [item for item in results if item["changed"]]


# DATA DUMMY DAN PENGUJIAN M10.4

if __name__ == "__main__":
    before_classes = {
        "area-A": "vegetation",
        "area-B": "water",
        "area-C": "bare_soil",
    }

    after_classes = {
        "area-A": "built_up",
        "area-B": "water",
        "area-C": "vegetation",
    }

    results = identify_land_cover_changes(
        before_classes,
        after_classes,
    )

    print("=== M10.4 LAND-COVER CHANGE ===")

    for item in results:
        status = "BERUBAH" if item["changed"] else "TETAP"
        print(
            f'{item["location_id"]}: '
            f'{item["before"]} -> {item["after"]} '
            f'({status})'
        )

    print("\nArea yang mengalami perubahan:")

    for item in get_changed_areas(results):
        print(item["location_id"])


# ==========================================
# PENGUJIAN TAMBAHAN M10.4
# ==========================================

def run_additional_tests():
    print("\n=== PENGUJIAN TAMBAHAN M10.4 ===")

    # Tes 1: Lokasi berbeda harus menghasilkan error
    try:
        identify_land_cover_changes(
            {"area-A": "vegetation"},
            {"area-B": "water"},
        )
    except ValueError:
        print("[LULUS] Lokasi berbeda terdeteksi")

    # Tes 2: Data input tidak boleh berubah
    before = {"area-A": "vegetation"}
    after = {"area-A": "built_up"}

    before_original = before.copy()
    after_original = after.copy()

    identify_land_cover_changes(before, after)

    if before == before_original and after == after_original:
        print("[LULUS] Data input tetap sama")

    # Tes 3: Tidak ada perubahan
    results = identify_land_cover_changes(
        {"area-A": "water"},
        {"area-A": "water"},
    )

    if len(get_changed_areas(results)) == 0:
        print("[LULUS] Tidak ada perubahan terdeteksi")


if __name__ == "__main__":
    run_additional_tests()
