from .cli import run

output_root = "C:\\Temp\\3DPrinter\\Gridfinity\\Bins and Labels\\Labels\\Bins\\"

def create_label(label_text, file_name):
  run(["ruggedbox", label_text, "--width", "88.7", "--height", "31.25", "-o", output_root + file_name + ".step"])

create_label("SAE  {bolt(5)} {nut} {washer}\nScrews, Nuts, Washers\n#2 #4 #6", "sae_screws_2-6")
create_label("Metric  {bolt(5,tapping)}\nScrews\nM1 M1.2 M1.4 M1.7", "metric_screws_tapping_less_than_M2")
create_label("Metric  {bolt(5,tapping)}\nScrews\nM2 M2.2 M2.3 M2.6 M3", "metric_screws_tapping_M2-M3")
create_label("Metric  {bolt(5)}\nScrews\nM3", "metric_screws_M3")
create_label("Metric  {bolt(10,countersunk)}\nScrews\nM3", "metric_screws_countersunk_M3")
create_label("Metric  {bolt(10,countersunk,tapping)}\nScrews\nM2.2 M2.6 M2.9 M3.5\nM4.2 M4.8 M5.5", "metric_screws_countersunk_tapping")
