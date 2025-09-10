from blog.models import Post
from django.core.management.base import BaseCommand

titles = [
    "The future of AI",
    "Exploring the cosmos",
    "Advancements in quantum computing",
    "The rise of renewable energy",
   "The impact of social media on society",
   "Understanding blockchain technology",
   "The future of work: Remote vs. Office"
]

contents = [
    "Artificial Intelligence (AI) is rapidly evolving and transforming various industries. From healthcare to finance, AI is enabling new possibilities and efficiencies.",
    "The universe is vast and full of mysteries. Recent advancements in space exploration have provided new insights into the cosmos.",
    "Quantum computing is set to revolutionize the way we process information. With its ability to solve complex problems faster than traditional computers, it holds great promise for various fields.",
    "Renewable energy sources such as solar and wind are becoming increasingly important in the fight against climate change. Innovations in this sector are driving a shift towards a more sustainable future.",
    "Social media has transformed the way we communicate and interact. While it has many benefits, it also poses challenges related to privacy, mental health, and misinformation.",
    "Blockchain technology is more than just the backbone of cryptocurrencies. Its potential applications in supply chain   management, voting systems, and secure data sharing are being explored.",
    "The traditional workplace is evolving, with remote work becoming more prevalent. This shift presents both  opportunities and challenges for employees and employers alike."
]

img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",   
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",   
    "https://picsum.photos/id/7/800/400"
]




class Command(BaseCommand):
    help = "Populate the database with initial data"

    def handle(self, *args, **options):
        for title, content, img_url in zip(titles, contents, img_urls):
            Post.objects.create(title=title, content=content, img_url=img_url)
        self.stdout.write(self.style.SUCCESS("Successfully populated the database with initial data"))