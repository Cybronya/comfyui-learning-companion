---
name: unknown_workflow_sampler_clip_unet_255
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9478
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商产品FLUX2精修_2094400191687385090.json, 图片生成/图生图/电商产品FLUX2精修_2096169386120925186.json, 图片生成/图生图/电商产品FLUX2精修_2096403269538115586.json, 图片生成/图生图/高频噪点修复_2108555371207020545.json, 图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_255

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/电商产品FLUX2精修_2094400191687385090.json、图片生成/图生图/电商产品FLUX2精修_2096169386120925186.json、图片生成/图生图/电商产品FLUX2精修_2096403269538115586.json、图片生成/图生图/高频噪点修复_2108555371207020545.json、图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/5 个有
- `easy imageConcat` —— 3/5 个有
- `easy imageSize` —— 3/5 个有
- `easy int` —— 3/5 个有
- `ImpactInt` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `SplitSigmasDenoise` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
