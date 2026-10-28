import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def visualize_changes(before_image_path, after_image_path, analysis_results):
    """
    M10.8 Change Visualization
    Menampilkan citra before-and-after dan hasil analisis.
    """
    # 1. Siapkan Figure untuk visualisasi
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # 2. Tampilkan Citra Before (Jika file gambarnya ada)
    try:
        img_before = mpimg.imread(before_image_path)
        axes[0].imshow(img_before)
        axes[0].set_title('Sebelum (Before)')
        axes[0].axis('off')
    except FileNotFoundError:
        axes[0].text(0.5, 0.5, 'Gambar Before\nTidak Ditemukan', 
                     ha='center', va='center', fontsize=12)
        axes[0].set_title('Sebelum (Before)')
        axes[0].axis('off')

    # 3. Tampilkan Citra After
    try:
        img_after = mpimg.imread(after_image_path)
        axes[1].imshow(img_after)
        axes[1].set_title('Sesudah (After)')
        axes[1].axis('off')
    except FileNotFoundError:
        axes[1].text(0.5, 0.5, 'Gambar After\nTidak Ditemukan', 
                     ha='center', va='center', fontsize=12)
        axes[1].set_title('Sesudah (After)')
        axes[1].axis('off')

    plt.suptitle('M10.8: Before-and-After Imagery', fontsize=16)
    plt.tight_layout()
    plt.show()

def display_analytical_results(land_cover_results, tree_results, veg_results):
    """
    Menampilkan hasil analisis dalam bentuk grafik atau teks.
    """
    print("\n Hasil Analisis Perubahan (Analytical Results)")
    
    # Menampilkan hasil Land Cover (M10.4)
    if land_cover_results:
        print("\n[Land-Cover Changes]")
        for item in land_cover_results:
            if item['changed']:
                print(f" - {item['location_id']}: {item['before']} -> {item['after']}")
    
    # Menampilkan hasil Tree Count (M10.5)
    if tree_results:
        print("\n[Tree Count Changes]")
        for item in tree_results:
            print(f" - {item['location_id']}: {item['change']:+d} pohon ({item['direction']})")
            
    # Menampilkan hasil Vegetation Coverage
    if veg_results:
        print(f"\n[Vegetation Coverage]")
        print(f" - Perubahan: {veg_results['change']} percentage points")

# Contoh Cara Menggunakan (mock data)
if __name__ == "__main__":
    # Data Dummy (sesuai dengan kode sebelumnya)
    before_img = "data/image_01.tif" # Pastikan path ini benar jika ingin melihat gambar
    after_img = "data/image_02.tif"
    
    # Simulasi hasil dari file M10.4 dan M10.5
    mock_land_cover = [
        {"location_id": "area-A", "before": "vegetation", "after": "built_up", "changed": True},
        {"location_id": "area-B", "before": "water", "after": "water", "changed": False}
    ]
    mock_tree_count = [
        {"location_id": "area-A", "before": 120, "after": 105, "change": -15, "direction": "berkurang"},
        {"location_id": "area-B", "before": 80, "after": 95, "change": 15, "direction": "bertambah"}
    ]
    mock_veg = {"before": 60.0, "after": 72.0, "change": 12.0}

    # Jalankan visualisasi
    visualize_changes(before_img, after_img, mock_land_cover)
    
    # Tampilkan teks hasil analisis
    display_analytical_results(mock_land_cover, mock_tree_count, mock_veg)