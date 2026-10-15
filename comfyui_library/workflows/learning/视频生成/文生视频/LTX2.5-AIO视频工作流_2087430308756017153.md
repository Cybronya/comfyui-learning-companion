---
key: 视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json
name: LTX2.5-AIO视频工作流_2087430308756017153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json
hash: 467dbe70196fc091
coverage: 0.677778
learned_at: 2026-10-15 22:45:16
nodes: [CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, Reroute, LTXVAudioVAEDecode, LTXVSeparateAVLatent, PrimitiveInt, ComfyMathExpression, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CFGGuider, CLIPTextEncode, CLIPTextEncode, PathchSageAttentionKJ, RandomNoise, KSamplerSelect, VAELoaderKJ, easy showAnything, ComfyMathExpression, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVCropGuides, LTXVSeparateAVLatent, SetNode, GetNode, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LTXVConditioning, SetNode, GetNode, GetNode, GetNode, GetNode, SolidMask, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplaceKJ, VAEDecodeTiled, PrimitiveInt, ComfyMathExpression, LoadAudio, Note, Switch any [Crystools], LTXVImgToVideoInplaceKJ, UNETLoader, VAELoaderKJ, LatentUpscaleModelLoader, VHS_VideoCombine, ManualSigmas, ManualSigmas, CLIPLoader, CLIPLoader, PrimitiveString, PreviewAny, GetNode, TextGenerateLTX2Prompt, ResizeImageMaskNode, LTXVPreprocess, SetNode, LoadImage, ResizeImageMaskNode, LTXVPreprocess, SetNode, LoadImage, ResizeImageMaskNode, LTXVPreprocess, SetNode, Fast Groups Bypasser (rgthree), INTConstant, LoadImage, PrimitiveBoolean, INTConstant, INTConstant, Text Multiline, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（90 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `ComfyMathExpression`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `easy showAnything`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplaceKJ`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `LoadAudio`
- `Note`
- `Switch any [Crystools]`
- `LTXVImgToVideoInplaceKJ`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `VHS_VideoCombine`
- `ManualSigmas`
- `ManualSigmas`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveString`
- `PreviewAny`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `SetNode`
- `LoadImage`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `SetNode`
- `LoadImage`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `LoadImage`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `Text Multiline`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（61/90）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`ComfyMathExpression`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SolidMask`、`LTXVImgToVideoInplaceKJ`、`VAEDecodeTiled`、`LoadAudio`、`Switch any [Crystools]`、`UNETLoader`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`ManualSigmas`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LoadImage`、`INTConstant`、`PrimitiveBoolean`、`Text Multiline`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
