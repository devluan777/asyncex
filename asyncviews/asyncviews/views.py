import asyncio
import httpx
from django.http import JsonResponse
from django.views.decorators.http import require_GET

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
        async with httpx.AsyncClient() as client:
            response = await client.get("https://httpbin.org/get")
            print(response.json())  # Parse the response as JSON for better readability

@require_GET  # Ensures that only GET requests are allowed
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return JsonResponse({"message": "Non-blocking HTTP request"})  # Return JSON response for better client-side handling



