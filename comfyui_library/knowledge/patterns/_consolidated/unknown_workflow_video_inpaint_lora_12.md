---
name: unknown_workflow_video_inpaint_lora_12
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.901
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, GetImageRangeFromBatch, GetImageSize, Image To Mask, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecodeTiled, VAEEncodeForInpaint, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-视频自动去字幕_去水印_模糊修复_高清放大（4合1）_2053854443006898178.json, 视频生成/图生视频/LTX2.3自动一键去字幕_2042927263661957121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-视频自动去字幕_去水印_模糊修复_高清放大（4合1）_2053854443006898178.json、视频生成/图生视频/LTX2.3自动一键去字幕_2042927263661957121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `Image To Mask`
- `ImageResizeKJv2`
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
- `PrimitiveInt`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
