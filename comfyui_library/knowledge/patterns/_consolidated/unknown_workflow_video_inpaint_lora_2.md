---
name: unknown_workflow_video_inpaint_lora_2
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.960286
common_nodes: [CFGGuider, CLIPTextEncode, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-视频自动去字幕_去水印_模糊修复_高清放大（4合1）_2053854443006898178.json, 视频生成/图生视频/LTX2.3自动一键去字幕_2042927263661957121.json, 视频生成/图生视频/视频去水印 LTX2.3 工作流_2054757647898955778.json, 视频生成/图生视频/视频去水印去字幕 LTX2.3时长加长_2068856868998565889.json, 视频生成/图生视频/视频去水印，去字幕LTX2.3 iclora insight工作流_2054762008184147969.json, 视频生成/图生视频/视频高清修复 LTX2.3 工作流_2054733348798509058.json, 视频生成/图生视频/视频高清修复+去水印去字幕 LTX2.3 工作流_2054767077927473153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-视频自动去字幕_去水印_模糊修复_高清放大（4合1）_2053854443006898178.json、视频生成/图生视频/LTX2.3自动一键去字幕_2042927263661957121.json、视频生成/图生视频/视频去水印 LTX2.3 工作流_2054757647898955778.json、视频生成/图生视频/视频去水印去字幕 LTX2.3时长加长_2068856868998565889.json、视频生成/图生视频/视频去水印，去字幕LTX2.3 iclora insight工作流_2054762008184147969.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `Image To Mask`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ColorImage`
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
- `CheckpointLoaderSimple` —— 5/7 个有
- `LTXAVTextEncoderLoader` —— 5/7 个有
- `LTXVAudioVAELoader` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `easy imageSize` —— 5/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `ComfyMathExpression` —— 2/7 个有
- `DualCLIPLoader` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `VAELoaderKJ` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `Int` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
