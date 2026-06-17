from rest_framework import serializers
from .models import Stock, StockPriceDaily, DailyMarketWeather, MarketIndexDaily, UserBookmark

class MarketIndexDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketIndexDaily
        fields = ['index_name', 'base_date', 'close_price', 'change', 'change_rate']

class DailyMarketWeatherSerializer(serializers.ModelSerializer):
    weather_emoji = serializers.SerializerMethodField()

    class Meta:
        model = DailyMarketWeather
        fields = ['target_date', 'weather_status', 'weather_emoji', 'message']

    def get_weather_emoji(self, obj):
        emoji_map = {
            'SUNNY': '☀️',
            'CLOUDY': '☁️',
            'RAINY': '🌧️',
            'SNOWY': '❄️',
            'STORMY': '⚡',
        }
        return emoji_map.get(obj.weather_status, '❓')
    
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
    
class StockPriceDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPriceDaily
        fields = ['record_date', 'open_price', 'close_price', 'high_price', 'low_price', 'volume',]

class StockDetailSerializer(serializers.ModelSerializer):
    daily_prices = StockPriceDailySerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'stock_code', 'stock_name', 'market_type', 'daily_prices',]


class UserBookmarkSerializer(serializers.ModelSerializer):
    stock_code = serializers.CharField(source='stock.stock_code', read_only=True)
    stock_name = serializers.CharField(source='stock.stock_name', read_only=True)
    market_type = serializers.CharField(source='stock.market_type', read_only=True)

    class Meta:
        model = UserBookmark
        fields = ['id', 'stock_code', 'stock_name', 'market_type', 'created_at']


