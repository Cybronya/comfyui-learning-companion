---
name: unknown_workflow_video_inpaint_lora_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.894
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, GetImageRangeFromBatch, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAEEncodeForInpaint, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/视频去水印字幕和高清修复_LTX2.3_2063371785399267329.json, 视频生成/图生视频/LTX2.3自动一键去字幕_2042927263661957121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频去水印字幕和高清修复_LTX2.3_2063371785399267329.json、视频生成/图生视频/LTX2.3自动一键去字幕_2042927263661957121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `KSamplerSelect`
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
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `Image To Mask` —— 1/2 个有
- `ImageColorToMask` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

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
