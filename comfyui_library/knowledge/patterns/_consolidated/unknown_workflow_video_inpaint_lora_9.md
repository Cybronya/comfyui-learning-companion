---
name: unknown_workflow_video_inpaint_lora_9
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.956667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/LTX2.3视频编辑版2_2054082498807779330.json, 平台全量/LTX2.3视频高清修复-视频去模糊高清化工作流_2054563894345125889.json, 平台全量/LTX2.3长视频祛除水印去水印去字幕清理字幕去文字_2060306627844198402.json, 平台全量/LTX23一键视频去字幕+自动删除水印_2054102609975357441.json, 平台全量/ltx2.3 全自动一键去水印 _ 字幕 _ 修复模糊 _ 高清放大_2057663022172303362.json, 平台全量/ltx2.3 全自动一键去水印(豆包视频)_2069402196575350785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/LTX2.3视频编辑版2_2054082498807779330.json、平台全量/LTX2.3视频高清修复-视频去模糊高清化工作流_2054563894345125889.json、平台全量/LTX2.3长视频祛除水印去水印去字幕清理字幕去文字_2060306627844198402.json、平台全量/LTX23一键视频去字幕+自动删除水印_2054102609975357441.json、平台全量/ltx2.3 全自动一键去水印 _ 字幕 _ 修复模糊 _ 高清放大_2057663022172303362.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `Image To Mask`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
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
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `ResizeImageMaskNode` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `VHS_VideoInfoLoaded` —— 5/6 个有
- `easy imageSize` —— 5/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `LTXICLoRALoaderModelOnly` —— 3/6 个有
- `CR Load LoRA` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `CustomAddLabel` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `Any To String (mtb)` —— 1/6 个有
- `CM_IntUnaryOperation` —— 1/6 个有
- `ConvertAny2Int` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageFromBatch+` —— 1/6 个有
- `ImageScaleToMaxDimension` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `IntConditions` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `StringListToCombo` —— 1/6 个有
- `StringToInt` —— 1/6 个有
- `TextSwitchCase` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `ttN int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
