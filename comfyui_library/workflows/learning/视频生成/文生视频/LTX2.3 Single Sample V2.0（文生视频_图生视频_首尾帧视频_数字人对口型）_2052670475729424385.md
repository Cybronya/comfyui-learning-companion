---
key: 视频生成/文生视频/LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385.json
name: LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385.json
hash: 67d0addd28112328
coverage: 0.857143
learned_at: 2026-10-15 22:44:58
nodes: [VAELoaderKJ, SamplerCustom, KSamplerSelect, VisualizeSigmasKJ, PathchSageAttentionKJ, LTXVConditioning, LTXVChunkFeedForward, Note, ImageResizeKJv2, Switch image [Crystools], ImageResizeKJv2, Switch image [Crystools], EmptyImage, easy isNone, SimpleMath+, SimpleMath+, easy isNone, EmptyImage, CM_BoolToInt, INTConstant, INTConstant, CM_BoolToInt, SaveVideo, CreateVideo, LTX2SamplingPreviewOverride, BasicScheduler, UNETLoader, DualCLIPLoader, DualCLIPLoaderGGUF, UnetLoaderGGUF, PlaySound|pysssss, VAELoaderKJ, Lora Loader Stack (rgthree), LTXVSeparateAVLatent, LTX2_NAG, LTXVImgToVideoInplaceKJ, EmptyLTXVLatentVideo, PreviewImage, Reroute, VHS_SelectImages, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, GetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, SetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVAudioVAEDecode, INTConstant, INTConstant, SimpleMath+, SimpleMath+, CLIPTextEncode, easy showAnything, PreviewImage, PreviewImage, ComfySwitchNode, VAEDecodeTiled, ComfySwitchNode, VHS_VideoCombine, PrimitiveBoolean, CLIPTextEncode, LoadImage, LoadImage, LoadAudio, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 361}
---

# 视频生成/文生视频/LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `VAELoaderKJ`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `LTXVChunkFeedForward`
- `Note`
- `ImageResizeKJv2`
- `Switch image [Crystools]`
- `ImageResizeKJv2`
- `Switch image [Crystools]`
- `EmptyImage`
- `easy isNone`
- `SimpleMath+`
- `SimpleMath+`
- `easy isNone`
- `EmptyImage`
- `CM_BoolToInt`
- `INTConstant`
- `INTConstant`
- `CM_BoolToInt`
- `SaveVideo`
- `CreateVideo`
- `LTX2SamplingPreviewOverride`
- `BasicScheduler`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `UnetLoaderGGUF` ★核心
- `PlaySound|pysssss`
- `VAELoaderKJ`
- `Lora Loader Stack (rgthree)`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `LTXVImgToVideoInplaceKJ`
- `EmptyLTXVLatentVideo`
- `PreviewImage`
- `Reroute`
- `VHS_SelectImages`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `PreviewImage`
- `PreviewImage`
- `ComfySwitchNode`
- `VAEDecodeTiled` ★核心
- `ComfySwitchNode`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `361`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（60/70）

**有卡**：`VAELoaderKJ`、`SamplerCustom`、`KSamplerSelect`、`VisualizeSigmasKJ`、`PathchSageAttentionKJ`、`LTXVConditioning`、`LTXVChunkFeedForward`、`ImageResizeKJv2`、`Switch image [Crystools]`、`EmptyImage`、`easy isNone`、`SimpleMath+`、`CM_BoolToInt`、`INTConstant`、`SaveVideo`、`CreateVideo`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`UNETLoader`、`DualCLIPLoader`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUF`、`PlaySound|pysssss`、`Lora Loader Stack (rgthree)`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`VHS_SelectImages`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`VAEDecodeTiled`、`VHS_VideoCombine`、`PrimitiveBoolean`、`LoadImage`、`LoadAudio`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
