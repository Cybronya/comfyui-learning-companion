---
name: unknown_workflow_upscale_lora_sampler_105
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8485
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Upscale Image, ConditioningZeroOut, DeepTranslatorTextNode, DisableNoise, DualCLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, ImageConcanate, ImageResizeKJ, ImpactSwitch, InjectLatentNoise+, KSamplerSelect, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LoadImage, LoraLoaderModelOnly, OpenposePreprocessor, PreviewImage, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SplitSigmasDenoise, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageInsetCrop, easy imageSize, easy int, easy positive, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/人物一致性6宫格小红书风格写真_1917818133267288066.json, 图片生成/文生图/【趣味】FLUX网红一致性六连拍工作流_1905449688709910529.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物一致性6宫格小红书风格写真_1917818133267288066.json、图片生成/文生图/【趣味】FLUX网红一致性六连拍工作流_1905449688709910529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Upscale Image`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DisableNoise`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImpactSwitch`
- `InjectLatentNoise+`
- `KSamplerSelect`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OpenposePreprocessor`
- `PreviewImage`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageInsetCrop`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
