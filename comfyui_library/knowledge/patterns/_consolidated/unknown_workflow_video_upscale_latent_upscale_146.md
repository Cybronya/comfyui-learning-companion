---
name: unknown_workflow_video_upscale_latent_upscale_146
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6105
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, PrimitiveString, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, Switch any [Crystools], Text Multiline, TextGenerateLTX2Prompt, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json, 视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_146

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json、视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `Switch any [Crystools]`
- `Text Multiline`
- `TextGenerateLTX2Prompt`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 1/2 个有
- `ComfyUILTX25MSRICLoRALoader` —— 1/2 个有
- `ComfyUILTX25MSRMultiReferenceGuide` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LTXVImgToVideoInplaceKJ` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有

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
