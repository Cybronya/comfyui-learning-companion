---
name: unknown_workflow_sampler_clip_unet_185
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.920333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/AA--超快！Klein 9b 文生图+5图编辑+自由多角度图+4K放大_2014671333396848641.json, 图片生成/文生图/Klein 9b base文生图&编辑  工作流_2014242527360065538.json, 视频生成/图生视频/2072586147523551233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/AA--超快！Klein 9b 文生图+5图编辑+自由多角度图+4K放大_2014671333396848641.json、图片生成/文生图/Klein 9b base文生图&编辑  工作流_2014242527360065538.json、视频生成/图生视频/2072586147523551233.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LoraLoaderModelOnly_Any` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `easy float` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
