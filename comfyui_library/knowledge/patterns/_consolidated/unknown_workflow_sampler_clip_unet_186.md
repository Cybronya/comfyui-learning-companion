---
name: unknown_workflow_sampler_clip_unet_186
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.876286
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, FlipSigmas, FluxForwardODESampler, FluxReverseODESampler, InFluxModelSamplingPred, LoadImage, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/64.tonnie-Zimage逆降噪精修（效果反而变得极差）_2009428798395125762.json, 图片生成/图生图/FLUX一键精修增强版本_1892213225352765442.json, 图片生成/图生图/Z-image-万物精修（速度狠快）_2001643362954407937.json, 图片生成/图生图/一键产品精修_1917438601485811714.json, 图片生成/图生图/一键产品精修_1930085411941466113.json, 图片生成/图生图/产品精修_1900359476417916930.json, 图片生成/图生图/精修3.0_1949401662776586242.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_186

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/64.tonnie-Zimage逆降噪精修（效果反而变得极差）_2009428798395125762.json、图片生成/图生图/FLUX一键精修增强版本_1892213225352765442.json、图片生成/图生图/Z-image-万物精修（速度狠快）_2001643362954407937.json、图片生成/图生图/一键产品精修_1917438601485811714.json、图片生成/图生图/一键产品精修_1930085411941466113.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `FlipSigmas`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `InFluxModelSamplingPred`
- `LoadImage`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `DualCLIPLoader` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `FluxDeGuidance` —— 4/7 个有
- `Image Lucy Sharpen` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `ImageResize+` —— 3/7 个有
- `CLIPLoader` —— 2/7 个有
- `FluxGuidance` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CR Simple Image Compare` —— 1/7 个有
- `ConditioningAddConDelta` —— 1/7 个有
- `ConditioningScale` —— 1/7 个有
- `ConditioningSubtract` —— 1/7 个有
- `ConfigureModifiedFlux` —— 1/7 个有
- `Display Int (rgthree)` —— 1/7 个有
- `FlowEditGuider` —— 1/7 个有
- `FlowEditSampler` —— 1/7 个有
- `Get Image Size` —— 1/7 个有
- `GetImageSize+` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImpactInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
