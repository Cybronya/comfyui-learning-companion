---
name: unknown_workflow_sampler_clip_unet_228
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.930833
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/高频噪点修复_2108555371207020545.json, 图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json, 图片生成/文生图/Flux.2双图编辑_1993607256262508545.json, 图片生成/文生图/Flux2 Dev 单图编辑_1999376869634043906.json, 图片生成/文生图/单图编辑+Flux2+Dev_1999389700567822338.json, 视频生成/图生视频/高频噪点修复_2114194025107513346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_228

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/高频噪点修复_2108555371207020545.json、图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json、图片生成/文生图/Flux.2双图编辑_1993607256262508545.json、图片生成/文生图/Flux2 Dev 单图编辑_1999376869634043906.json、图片生成/文生图/单图编辑+Flux2+Dev_1999389700567822338.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 4/6 个有
- `ImpactInt` —— 4/6 个有
- `ReferenceLatent` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `ImageSizeInfo` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `SplitSigmasDenoise` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
