---
name: unknown_workflow_sampler_clip_unet_26
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88725
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Crop Face, LayerUtility: PurgeVRAM V2, ImageSmartSharpen+, easy int, Seed (rgthree)]
members: [图片生成/图生图/2012770534232170497.json, 图片生成/图生图/2025838254557237250.json, 图片生成/图生图/2029595679181508609.json, 图片生成/图生图/2034605360421543938.json, 图片生成/图生图/2041822266979262465.json, 图片生成/图生图/2047233928045531137.json, 图片生成/文生图/人像换脸丨Flux2-Klein 9B丨面部发型替换_2105644038434152450.json, 数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/2012770534232170497.json、图片生成/图生图/2025838254557237250.json、图片生成/图生图/2029595679181508609.json、图片生成/图生图/2034605360421543938.json、图片生成/图生图/2041822266979262465.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `GetImageSize` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `LayerUtility: ImageReel` —— 3/8 个有
- `LayerUtility: ImageReelComposit` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `JWFloat` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `AutoCropFaces` —— 1/8 个有
- `Image Crop Face` —— 1/8 个有
- `ImageSmartSharpen+` —— 1/8 个有
- `Int` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: ImageReel、LayerUtility: ImageReelComposit、Image Crop Face
