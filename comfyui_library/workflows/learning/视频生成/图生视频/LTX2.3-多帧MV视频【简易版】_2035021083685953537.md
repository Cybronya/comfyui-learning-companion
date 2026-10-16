---
key: 视频生成/图生视频/LTX2.3-多帧MV视频【简易版】_2035021083685953537.json
name: LTX2.3-多帧MV视频【简易版】_2035021083685953537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035021083685953537.json
hash: 5024741a1004e337
coverage: 0.666667
learned_at: 2026-10-15 22:35:47
nodes: [CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, ManualSigmas, Reroute, LTXVSeparateAVLatent, VAELoaderKJ, PrimitiveInt, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, GetNode, GetNode, LTXVPreprocess, LTXVPreprocess, SetNode, SetNode, GetNode, LTXVPreprocess, SetNode, SetNode, GetNode, KSamplerSelect, VAELoaderKJ, easy showAnything, LTXVCropGuides, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, GetNode, UNETLoader, SolidMask, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, Note, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, GetNode, CM_IntToFloat, PrimitiveInt, GetNode, math_calculate, math_calculate, GetNode, GetNode, math_calculate, math_calculate, CM_IntToFloat, DualCLIPLoader, SetNode, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, Fast Groups Bypasser (rgthree), math_calculate, PrimitiveBoolean, PrimitiveBoolean, TextGenerateLTX2Prompt, PreviewAny, VAEDecodeTiled, LTXVAudioVAEDecode, LoadImage, LoadImage, LoadImage, INTConstant, INTConstant, INTConstant, RTXVideoSuperResolution, GetNode, CM_IntToFloat, VHS_VideoCombine, INTConstant, GetNode, LatentUpscaleModelLoader, Text Multiline, Switch any [Crystools], CLIPTextEncode, CLIPTextEncode, Lora Loader Stack (rgthree), RandomNoise, Switch any [Crystools], LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVConditioning, MarkdownNote, LoadAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-多帧MV视频【简易版】_2035021083685953537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035021083685953537.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（102 个）：
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
- `UNETLoader` ★核心
- `SolidMask`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
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
- `LTXVImgToVideoConditionOnly`
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
- `RTXVideoSuperResolution`
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
- `Lora Loader Stack (rgthree)`
- `RandomNoise`
- `Switch any [Crystools]`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVConditioning`
- `MarkdownNote`
- `LoadAudio`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（68/102）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAELoaderKJ`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`UNETLoader`、`SolidMask`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`ResizeImageMaskNode`、`CM_IntToFloat`、`math_calculate`、`DualCLIPLoader`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoadImage`、`INTConstant`、`RTXVideoSuperResolution`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`Text Multiline`、`Switch any [Crystools]`、`CLIPTextEncode`、`Lora Loader Stack (rgthree)`、`LTXVConditioning`、`LoadAudio`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
