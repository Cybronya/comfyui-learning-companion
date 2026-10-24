---
name: unknown_workflow_sampler_clip_unet_262
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9246
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.2双图编辑_1993607256262508545.json, 图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json, 图片生成/文生图/Flux.2溶图_1995426699946995714.json, 图片生成/文生图/Flux2 Dev 单图编辑_1999376869634043906.json, 图片生成/文生图/单图编辑+Flux2+Dev_1999389700567822338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_262

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux.2双图编辑_1993607256262508545.json、图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json、图片生成/文生图/Flux.2溶图_1995426699946995714.json、图片生成/文生图/Flux2 Dev 单图编辑_1999376869634043906.json、图片生成/文生图/单图编辑+Flux2+Dev_1999389700567822338.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
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
- `ImageScaleToTotalPixels` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `ImageSizeInfo` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Compositor3` —— 1/5 个有
- `CompositorConfig3` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `InspyrenetRembg` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
