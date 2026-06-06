import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.models import Service

services = [
  { 
    "slug": "electrician",
    "title": "Electrician", 
    "desc": "Certified installations, rewiring, lighting and safety inspections.",
    "full_desc": "We provide professional electrical services for residential and commercial properties. Our electricians handle installations, repairs, maintenance, and troubleshooting to ensure safe and reliable electrical systems.",
    "features": [
      "Electrical wiring and rewiring",
      "Switch and socket installation",
      "Lighting installation and repairs",
      "Ceiling fan installation",
      "Circuit breaker repairs",
      "Power fault troubleshooting",
      "Electrical maintenance",
      "Indoor and outdoor lighting",
      "Appliance electrical connections",
      "Safety inspections"
    ],
    "why_choose_us": [
      "Licensed and skilled electricians",
      "Fast response and reliable service",
      "High-quality workmanship",
      "Safety-focused solutions",
      "Transparent pricing",
      "Customer satisfaction guaranteed"
    ],
    "conclusion": "We deliver safe, efficient, and reliable electrical solutions tailored to your needs."
  },
  { 
    "slug": "plumber",
    "title": "Plumbing", 
    "desc": "Leak repair, boiler servicing, bathrooms and full heating installations.",
    "full_desc": "We provide professional plumbing services for homes, offices, and commercial properties. Our team handles installations, repairs, and maintenance to keep your water systems functioning smoothly.",
    "features": [
      "Pipe installation and repairs",
      "Leak detection and fixing",
      "Tap and faucet installation",
      "Drain cleaning",
      "Toilet installation and repairs",
      "Sink and shower fitting",
      "Water tank installation",
      "Bathroom and kitchen plumbing",
      "Water pressure solutions",
      "Plumbing maintenance"
    ],
    "why_choose_us": [],
    "conclusion": "We ensure quality workmanship and dependable plumbing solutions for every project."
  },
  { 
    "slug": "carpenter",
    "title": "Carpenter", 
    "desc": "Bespoke joinery, flooring, fitted units and structural timber work.",
    "full_desc": "Our professional carpenters provide quality woodworking and furniture solutions for homes and businesses. We handle custom furniture, repairs, installations, and woodwork projects with precision and attention to detail.",
    "features": [
      "Custom furniture making",
      "Furniture repair and restoration",
      "Door installation and repairs",
      "Window frame installation",
      "Cabinet and wardrobe fitting",
      "Kitchen woodwork",
      "Shelving and storage solutions",
      "Wooden flooring installation",
      "Office furniture installation",
      "General carpentry work"
    ],
    "why_choose_us": [],
    "conclusion": "We deliver durable, functional, and professionally crafted woodwork tailored to your requirements."
  },
  { 
    "slug": "painting",
    "title": "Painting", 
    "desc": "Interior and exterior decorating with premium finishes and a tidy crew.",
    "full_desc": "We provide professional painting services for residential and commercial properties. Our team delivers clean, high-quality finishes that enhance the appearance and protection of your walls and surfaces.",
    "features": [
      "Interior painting",
      "Exterior painting",
      "Wall painting and touch-ups",
      "Ceiling painting",
      "Door and window painting",
      "Waterproof coating application",
      "Texture and decorative painting",
      "Office and commercial painting",
      "Surface preparation and priming",
      "Repainting and renovation painting"
    ],
    "why_choose_us": [],
    "conclusion": "We ensure smooth finishes, attention to detail, and long-lasting results for every painting project."
  },
  { 
    "slug": "gardens",
    "title": "Gardens decorating and cleaning", 
    "desc": "Landscaping, regular upkeep, jet-washing and seasonal clearances.",
    "full_desc": "We provide professional garden decorating and cleaning services to keep outdoor spaces neat, attractive, and well-maintained. Our team helps enhance the beauty of gardens through regular care, cleaning, and decorative improvements.",
    "features": [
      "Garden cleaning and maintenance",
      "Lawn mowing and trimming",
      "Weed removal",
      "Plant and flower bed care",
      "Hedge and shrub trimming",
      "Leaf and debris removal",
      "Garden decoration and arrangement",
      "Seasonal garden clean-up",
      "Outdoor space beautification",
      "General garden upkeep"
    ],
    "why_choose_us": [],
    "conclusion": "We ensure your garden remains clean, organized, and visually appealing throughout the year."
  },
  { 
    "slug": "remover",
    "title": "Remover", 
    "desc": "Insured house and office moves across the UK with careful packing.",
    "full_desc": "We provide reliable moving and removal services for homes, offices, and commercial properties. Our team ensures the safe handling, packing, transportation, and unloading of your belongings with care and efficiency.",
    "features": [
      "House shifting services",
      "Office relocation",
      "Furniture moving",
      "Packing and unpacking assistance",
      "Loading and unloading",
      "Local and long-distance moves",
      "Appliance and equipment moving",
      "Item removal and disposal",
      "Storage moving assistance",
      "Residential and commercial relocations"
    ],
    "why_choose_us": [],
    "conclusion": "We ensure a smooth, organized, and hassle-free moving experience from start to finish."
  },
  { 
    "slug": "cleaning",
    "title": "Cleaning", 
    "desc": "Deep cleans, end-of-tenancy and recurring domestic visits.",
    "full_desc": "We provide professional cleaning services for homes, offices, and commercial spaces. Our team ensures clean, hygienic, and well-maintained environments using efficient cleaning methods and attention to detail.",
    "features": [
      "Home cleaning",
      "Office cleaning",
      "Deep cleaning",
      "Kitchen cleaning",
      "Bathroom cleaning",
      "Floor cleaning and mopping",
      "Dusting and sanitization",
      "Window cleaning",
      "Move-in and move-out cleaning",
      "Regular maintenance cleaning"
    ],
    "why_choose_us": [],
    "conclusion": "We deliver reliable cleaning solutions to keep your space fresh, organized, and spotless."
  },
  { 
    "slug": "kitchen-fittings",
    "title": "Kitchen fittings", 
    "desc": "Complete kitchen installation, worktops, and appliance fitting.",
    "full_desc": "We provide professional kitchen fitting services for residential and commercial properties. Our team installs and upgrades kitchen components to ensure functionality, durability, and a well-organized space.",
    "features": [
      "Kitchen cabinet installation",
      "Modular kitchen fitting",
      "Countertop installation",
      "Sink fitting and replacement",
      "Kitchen storage solutions",
      "Drawer and shelf installation",
      "Hardware and accessory fitting",
      "Kitchen renovation support",
      "Cabinet repairs and adjustments",
      "Custom kitchen fitting solutions"
    ],
    "why_choose_us": [],
    "conclusion": "We ensure precise installation and quality workmanship to create a functional and efficient kitchen space."
  }
]

for s in services:
    Service.objects.update_or_create(slug=s['slug'], defaults=s)
    print(f"Created/updated {s['slug']}")

print("Done populating!")
