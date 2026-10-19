---
name: unknown_workflow_video_inpaint_lora
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.975727
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, Seed (rgthree), SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/2067532074952781825.json, 视频生成/图生视频/2053727074506035201.json, 视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json, 视频生成/图生视频/2053760267812646913.json, 视频生成/图生视频/2077034706784309250.json, 视频生成/图生视频/2058077944274317314.json, 视频生成/图生视频/2069702802959589378.json, 视频生成/图生视频/一键去字幕水印去模糊_2094407100247134209.json, 视频生成/图生视频/2059081651447222274.json, 视频生成/图生视频/2061290081482264578.json, 视频生成/图生视频/2068856868998565889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2067532074952781825.json、视频生成/图生视频/2053727074506035201.json、视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json、视频生成/图生视频/2053760267812646913.json、视频生成/图生视频/2077034706784309250.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image To Mask` —— 10/11 个有
- `Text Multiline` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `ImageConcatMulti` —— 4/11 个有
- `Int` —— 3/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `CR Text` —— 2/11 个有
- `INTConstant` —— 2/11 个有
- `ImageConcanate` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `CreateVideo` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageBatchMulti` —— 1/11 个有
- `ImageFromBatch+` —— 1/11 个有
- `ImageToMask` —— 1/11 个有
- `ImpactInt` —— 1/11 个有
- `List of strings [Crystools]` —— 1/11 个有
- `LoadImage` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `RHLLMChatNode` —— 1/11 个有
- `ToInt` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
