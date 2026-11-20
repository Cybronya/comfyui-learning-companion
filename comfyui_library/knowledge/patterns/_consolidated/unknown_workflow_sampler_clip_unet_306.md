---
name: unknown_workflow_sampler_clip_unet_306
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9426
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2029798924080390146.json, 图片生成/文生图/2031356956467798017.json, 图片生成/文生图/AA--超快！Klein 9b 文生图+5图编辑+自由多角度图+4K放大_2014671333396848641.json, 图片生成/文生图/Klein 9b base文生图&编辑  工作流_2014242527360065538.json, 视频生成/图生视频/Flux2_klein_图生图+高清放大_2072586147523551233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_306

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/2029798924080390146.json、图片生成/文生图/2031356956467798017.json、图片生成/文生图/AA--超快！Klein 9b 文生图+5图编辑+自由多角度图+4K放大_2014671333396848641.json、图片生成/文生图/Klein 9b base文生图&编辑  工作流_2014242527360065538.json、视频生成/图生视频/Flux2_klein_图生图+高清放大_2072586147523551233.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `SeedVR2LoadDiTModel` —— 2/5 个有
- `SeedVR2LoadVAEModel` —— 2/5 个有
- `SeedVR2VideoUpscaler` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoraLoaderModelOnly_Any` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有
- `easy float` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
