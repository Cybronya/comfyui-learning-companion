---
name: unknown_workflow_video_inpaint_lora
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.979385
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json, 视频生成/图生视频/LTX2.3 iclora insight整合大全高清、去字幕、去水印_2053760267812646913.json, 视频生成/图生视频/LTX2.3去水印字幕，彻底无残留？_2077034706784309250.json, 视频生成/图生视频/LTX2.3视频去水印+去字幕_2058077944274317314.json, 视频生成/图生视频/YJ-ltx2.3去水印 (1)_2069702802959589378.json, 视频生成/图生视频/一键去字幕水印去模糊_2094407100247134209.json, 视频生成/图生视频/四合一去水印+_+字幕+_+修复模糊+_+高清放大_2059081651447222274.json, 视频生成/图生视频/图生视频去水印_2061290081482264578.json, 视频生成/图生视频/视频去水印 LTX2.3 工作流_2054757647898955778.json, 视频生成/图生视频/视频去水印去字幕 LTX2.3时长加长_2068856868998565889.json, 视频生成/图生视频/视频去水印，去字幕LTX2.3 iclora insight工作流_2054762008184147969.json, 视频生成/图生视频/视频高清修复 LTX2.3 工作流_2054733348798509058.json, 视频生成/图生视频/视频高清修复+去水印去字幕 LTX2.3 工作流_2054767077927473153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3-IClora_视频去水印_字幕_2107466125268312066.json、视频生成/图生视频/LTX2.3 iclora insight整合大全高清、去字幕、去水印_2053760267812646913.json、视频生成/图生视频/LTX2.3去水印字幕，彻底无残留？_2077034706784309250.json、视频生成/图生视频/LTX2.3视频去水印+去字幕_2058077944274317314.json、视频生成/图生视频/YJ-ltx2.3去水印 (1)_2069702802959589378.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
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
- `Image To Mask` —— 12/13 个有
- `Seed (rgthree)` —— 10/13 个有
- `ImageConcatMulti` —— 8/13 个有
- `Text Multiline` —— 6/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `Int` —— 3/13 个有
- `MathExpression|pysssss` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `INTConstant` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `ImageBatchMulti` —— 1/13 个有
- `ImageFromBatch+` —— 1/13 个有
- `ImageToMask` —— 1/13 个有
- `ImpactInt` —— 1/13 个有
- `List of strings [Crystools]` —— 1/13 个有
- `LoadImage` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `ToInt` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
