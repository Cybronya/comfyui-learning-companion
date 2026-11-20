---
name: unknown_workflow_lora_sampler_clip_313
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.837
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ColorMatch, DualCLIPLoader, GrowMaskWithBlur, Image Comparer (rgthree), KSamplerSelect, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, preview_mask]
problems: []
missing: []
members: [图片生成/图生图/人像遮罩-重绘细化_1951526025467473922.json, 平台全量/面部器官优化_1890079729947488257.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_313

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人像遮罩-重绘细化_1951526025467473922.json、平台全量/面部器官优化_1890079729947488257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ColorMatch`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `LayerMask: MediapipeFacialSegment` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `Text Concatenate (JPS)` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.65 | - | 2 | 77% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
