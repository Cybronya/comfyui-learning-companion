---
name: unknown_workflow_sampler_clip_unet_356
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93575
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.2溶图_1995426699946995714.json, 图片生成/文生图/Flux2 Dev 单图编辑_1999376869634043906.json, 图片生成/文生图/单图编辑+Flux2+Dev_1999389700567822338.json, 图片生成/文生图/反差人设-剧场后台花絮_1999861137980223490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_356

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux.2溶图_1995426699946995714.json、图片生成/文生图/Flux2 Dev 单图编辑_1999376869634043906.json、图片生成/文生图/单图编辑+Flux2+Dev_1999389700567822338.json、图片生成/文生图/反差人设-剧场后台花絮_1999861137980223490.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ImageSizeInfo` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Compositor3` —— 1/4 个有
- `CompositorConfig3` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `InspyrenetRembg` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
