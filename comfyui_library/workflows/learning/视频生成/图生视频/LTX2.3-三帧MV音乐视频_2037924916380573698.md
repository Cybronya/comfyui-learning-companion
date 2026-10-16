---
key: 视频生成/图生视频/LTX2.3-三帧MV音乐视频_2037924916380573698.json
name: LTX2.3-三帧MV音乐视频_2037924916380573698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037924916380573698.json
hash: 8c79ccc865fb419b
coverage: 0.68
learned_at: 2026-10-15 22:36:00
nodes: [CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, ManualSigmas, Reroute, LTXVSeparateAVLatent, PrimitiveInt, SetLatentNoiseMask, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, GetNode, LTXVPreprocess, LTXVPreprocess, SetNode, SetNode, GetNode, LTXVPreprocess, GetNode, KSamplerSelect, easy showAnything, LTXVCropGuides, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, UNETLoader, SolidMask, LTXVConcatAVLatent, Note, GetNode, GetNode, GetNode, GetNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, GetNode, CM_IntToFloat, PrimitiveInt, GetNode, math_calculate, math_calculate, GetNode, GetNode, math_calculate, math_calculate, CM_IntToFloat, SetNode, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, math_calculate, PrimitiveBoolean, PrimitiveBoolean, TextGenerateLTX2Prompt, PreviewAny, VAEDecodeTiled, LTXVAudioVAEDecode, CM_IntToFloat, GetNode, Switch any [Crystools], CLIPTextEncode, CLIPTextEncode, RandomNoise, Switch any [Crystools], LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVConditioning, LatentUpscaleModelLoader, Lora Loader Stack (rgthree), TrimAudioDuration, LTXVAudioVAEEncode, LoadAudio, LoadImage, LoadImage, LoadImage, Text Multiline, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTXVImgToVideoInplaceKJ, GetNode, GetNode, ResizeImageMaskNode, RTXVideoSuperResolution, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, INTConstant, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-三帧MV音乐视频_2037924916380573698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037924916380573698.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（100 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `Reroute`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `SetLatentNoiseMask`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `KSamplerSelect` ★核心
- `easy showAnything`
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `SolidMask`
- `LTXVConcatAVLatent`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `SetNode`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `math_calculate`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CM_IntToFloat`
- `GetNode`
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
- `LatentUpscaleModelLoader`
- `Lora Loader Stack (rgthree)`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `RTXVideoSuperResolution`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（68/100）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`UNETLoader`、`SolidMask`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`CM_IntToFloat`、`math_calculate`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`Switch any [Crystools]`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`Lora Loader Stack (rgthree)`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`LoadAudio`、`LoadImage`、`Text Multiline`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`RTXVideoSuperResolution`、`VHS_VideoCombine`、`INTConstant`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
