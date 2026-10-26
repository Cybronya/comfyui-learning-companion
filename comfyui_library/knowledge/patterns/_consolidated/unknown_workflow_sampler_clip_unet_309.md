---
name: unknown_workflow_sampler_clip_unet_309
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95325
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2029798924080390146.json, 图片生成/文生图/2031356956467798017.json, 图片生成/文生图/AA--超快！Klein 9b 文生图+5图编辑+自由多角度图+4K放大_2014671333396848641.json, 图片生成/文生图/Klein 9b base文生图&编辑  工作流_2014242527360065538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_309

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/2029798924080390146.json、图片生成/文生图/2031356956467798017.json、图片生成/文生图/AA--超快！Klein 9b 文生图+5图编辑+自由多角度图+4K放大_2014671333396848641.json、图片生成/文生图/Klein 9b base文生图&编辑  工作流_2014242527360065538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoraLoaderModelOnly_Any` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `easy float` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
