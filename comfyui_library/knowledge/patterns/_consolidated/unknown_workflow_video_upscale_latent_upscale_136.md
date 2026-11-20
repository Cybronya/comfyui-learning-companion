---
name: unknown_workflow_video_upscale_latent_upscale_136
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4195
common_nodes: [APGGuider, BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyAudio, GetImageSize, GetNode, ImageConcanate, ImageScaleBy, KSamplerSelect, LTXVAddGuide, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LoadAudio, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, RecordAudio, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, Textbox, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, easy convertAnything]
problems: []
missing: []
members: [数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json, 视频生成/图生视频/豆包视频 - 除水印_2056637158571732994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_136

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json、视频生成/图生视频/豆包视频 - 除水印_2056637158571732994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：42%

## 共有节点

全部 2 个 workflow 都包含：
- `APGGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyAudio`
- `GetImageSize`
- `GetNode`
- `ImageConcanate`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAddGuide`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `RecordAudio`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `Textbox`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LTXVAddGuideMulti` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `TextGenerate` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
