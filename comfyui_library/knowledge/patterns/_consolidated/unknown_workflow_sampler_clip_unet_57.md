---
name: unknown_workflow_sampler_clip_unet_57
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.831889
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Crop Face, LayerUtility: PurgeVRAM V2, ImageSmartSharpen+, easy int, Seed (rgthree)]
members: [图片生成/图生图/2012770534232170497.json, 图片生成/图生图/2025838254557237250.json, 图片生成/图生图/2029595679181508609.json, 图片生成/图生图/2034605360421543938.json, 图片生成/图生图/2041822266979262465.json, 图片生成/图生图/2047233928045531137.json, 图片生成/文生图/Klein - 万物迁移自用_2064658422053818370.json, 图片生成/文生图/Klein-一致性_2096434383749210114.json, 图片生成/文生图/二次元老婆秒变真人！ComfyUI动漫转写实，脸不变质感拉满_2059589704609255426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_57

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2012770534232170497.json、图片生成/图生图/2025838254557237250.json、图片生成/图生图/2029595679181508609.json、图片生成/图生图/2034605360421543938.json、图片生成/图生图/2041822266979262465.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 7/9 个有
- `CR Text` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `GetImageSize` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `LayerUtility: ImageReel` —— 4/9 个有
- `LayerUtility: ImageReelComposit` —— 4/9 个有
- `JWFloat` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `ImageConcanate` —— 2/9 个有
- `ImageSmartSharpen+` —— 2/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `easy int` —— 2/9 个有
- `Image Crop Face` —— 1/9 个有
- `ImageStitch` —— 1/9 个有
- `Int` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: ImageReel、LayerUtility: ImageReelComposit、Image Crop Face
