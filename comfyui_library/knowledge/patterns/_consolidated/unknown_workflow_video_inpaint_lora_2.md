---
name: unknown_workflow_video_inpaint_lora_2
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.977375
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json, 视频生成/图生视频/2053760267812646913.json, 视频生成/图生视频/2077034706784309250.json, 视频生成/图生视频/2058077944274317314.json, 视频生成/图生视频/2069702802959589378.json, 视频生成/图生视频/2061290081482264578.json, 视频生成/图生视频/2054757647898955778.json, 视频生成/图生视频/2068856868998565889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json、视频生成/图生视频/2053760267812646913.json、视频生成/图生视频/2077034706784309250.json、视频生成/图生视频/2058077944274317314.json、视频生成/图生视频/2069702802959589378.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
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
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image To Mask` —— 7/8 个有
- `Seed (rgthree)` —— 7/8 个有
- `ImageConcatMulti` —— 4/8 个有
- `Int` —— 3/8 个有
- `MathExpression|pysssss` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageBatchMulti` —— 1/8 个有
- `ImageFromBatch+` —— 1/8 个有
- `ImageToMask` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `List of strings [Crystools]` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `ToInt` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
