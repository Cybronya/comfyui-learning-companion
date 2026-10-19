---
name: unknown_workflow_sampler_clip_unet_82
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.987667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/图生图/2093623432524156930.json, 图片生成/图生图/2102605007383261185.json, 视频生成/图生视频/2014254176355753986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2093623432524156930.json、图片生成/图生图/2102605007383261185.json、视频生成/图生视频/2014254176355753986.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `InpaintCropImproved` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `InpaintStitchImproved` —— 1/3 个有
- `JWFloat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
