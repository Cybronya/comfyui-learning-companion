---
name: unknown_workflow_video_inpaint_lora
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.980909
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [数字人/数字人/视频去字幕_水印：LTX2.3_2074325622687617026.json, 视频生成/图生视频/LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json, 视频生成/图生视频/LTX-2.3-ICLORA视频高清化+修复组合版V1_2053727074506035201.json, 视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json, 视频生成/图生视频/LTX2.3 iclora insight整合大全高清、去字幕、去水印_2053760267812646913.json, 视频生成/图生视频/LTX2.3去水印字幕，彻底无残留？_2077034706784309250.json, 视频生成/图生视频/LTX2.3视频去水印+去字幕_2058077944274317314.json, 视频生成/图生视频/YJ-ltx2.3去水印 (1)_2069702802959589378.json, 视频生成/图生视频/一键去字幕水印去模糊_2094407100247134209.json, 视频生成/图生视频/四合一去水印+_+字幕+_+修复模糊+_+高清放大_2059081651447222274.json, 视频生成/图生视频/图生视频去水印_2061290081482264578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/视频去字幕_水印：LTX2.3_2074325622687617026.json、视频生成/图生视频/LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json、视频生成/图生视频/LTX-2.3-ICLORA视频高清化+修复组合版V1_2053727074506035201.json、视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json、视频生成/图生视频/LTX2.3 iclora insight整合大全高清、去字幕、去水印_2053760267812646913.json…）

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
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `Seed (rgthree)` —— 10/11 个有
- `easy imageSize` —— 10/11 个有
- `Image To Mask` —— 9/11 个有
- `ImageConcatMulti` —— 4/11 个有
- `Text Multiline` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `INTConstant` —— 2/11 个有
- `ImageConcanate` —— 2/11 个有
- `ImageToMask` —— 2/11 个有
- `Int` —— 2/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `CreateVideo` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageBatchMulti` —— 1/11 个有
- `ImpactInt` —— 1/11 个有
- `List of strings [Crystools]` —— 1/11 个有
- `LoadImage` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `RHLLMChatNode` —— 1/11 个有
- `ToInt` —— 1/11 个有
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
