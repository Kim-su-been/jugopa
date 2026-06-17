from rest_framework import serializers

from .models import NewsArticle, SectorCardNews


class RepresentativeArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsArticle
		fields = ['title', 'link', 'source', 'published_at']


class SectorCardNewsSerializer(serializers.ModelSerializer):
	sector_name = serializers.CharField(source='sector.name', read_only=True)
	representative_articles = RepresentativeArticleSerializer(many=True, read_only=True)

	class Meta:
		model = SectorCardNews
		fields = [
			'rank', 'sector_name', 'target_date', 'headline', 'summary',
			'key_points', 'article_count', 'representative_articles',
		]
