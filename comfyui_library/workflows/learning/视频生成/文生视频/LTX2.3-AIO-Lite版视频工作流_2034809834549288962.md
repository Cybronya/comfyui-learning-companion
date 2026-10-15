---
key: 视频生成/文生视频/LTX2.3-AIO-Lite版视频工作流_2034809834549288962.json
name: LTX2.3-AIO-Lite版视频工作流_2034809834549288962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-AIO-Lite版视频工作流_2034809834549288962.json
hash: b1d628330aae816e
coverage: 0.663366
learned_at: 2026-10-15 22:45:02
nodes: [CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, ManualSigmas, Reroute, LTXVSeparateAVLatent, VAELoaderKJ, PrimitiveInt, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, GetNode, GetNode, LTXVPreprocess, LTXVPreprocess, SetNode, SetNode, GetNode, LTXVPreprocess, SetNode, SetNode, GetNode, KSamplerSelect, VAELoaderKJ, easy showAnything, LTXVCropGuides, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, GetNode, SolidMask, LTXVConcatAVLatent, Note, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, LoadAudio, GetNode, CM_IntToFloat, PrimitiveInt, GetNode, math_calculate, math_calculate, GetNode, GetNode, math_calculate, math_calculate, CM_IntToFloat, DualCLIPLoader, SetNode, ManualSigmas, LTXVLatentUpsampler, Fast Groups Bypasser (rgthree), math_calculate, PrimitiveBoolean, PrimitiveBoolean, TextGenerateLTX2Prompt, PreviewAny, VAEDecodeTiled, LTXVAudioVAEDecode, LoadImage, LoadImage, LoadImage, INTConstant, INTConstant, INTConstant, GetNode, CM_IntToFloat, VHS_VideoCombine, INTConstant, GetNode, LatentUpscaleModelLoader, Text Multiline, Switch any [Crystools], CLIPTextEncode, CLIPTextEncode, RandomNoise, Switch any [Crystools], LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVConditioning, MarkdownNote, LTXVImgToVideoInplaceKJ, LTXVImgToVideoInplaceKJ, UNETLoader, Lora Loader Stack (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3-AIO-Lite版视频工作流_2034809834549288962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-AIO-Lite版视频工作流_2034809834549288962.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（101 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `Reroute`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `PrimitiveInt`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `easy showAnything`
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `LTXVConcatAVLatent`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LoadAudio`
- `GetNode`
- `CM_IntToFloat`
- `PrimitiveInt`
- `GetNode`
- `math_calculate`
- `math_calculate`
- `GetNode`
- `GetNode`
- `math_calculate`
- `math_calculate`
- `CM_IntToFloat`
- `DualCLIPLoader`
- `SetNode`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `math_calculate`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `CM_IntToFloat`
- `VHS_VideoCombine`
- `INTConstant`
- `GetNode`
- `LatentUpscaleModelLoader`
- `Text Multiline`
- `Switch any [Crystools]`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `Switch any [Crystools]`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVConditioning`
- `MarkdownNote`
- `LTXVImgToVideoInplaceKJ`
- `LTXVImgToVideoInplaceKJ`
- `UNETLoader` ★核心
- `Lora Loader Stack (rgthree)`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（67/101）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAELoaderKJ`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SolidMask`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`LoadAudio`、`CM_IntToFloat`、`math_calculate`、`DualCLIPLoader`、`LTXVLatentUpsampler`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoadImage`、`INTConstant`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`Text Multiline`、`Switch any [Crystools]`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVImgToVideoInplaceKJ`、`UNETLoader`、`Lora Loader Stack (rgthree)`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
