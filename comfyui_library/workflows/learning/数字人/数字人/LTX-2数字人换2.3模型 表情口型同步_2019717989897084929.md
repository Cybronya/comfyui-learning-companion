---
key: 数字人/数字人/LTX-2数字人换2.3模型 表情口型同步_2019717989897084929.json
name: LTX-2数字人换2.3模型 表情口型同步_2019717989897084929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX-2数字人换2.3模型 表情口型同步_2019717989897084929.json
hash: bb4e12fc9687b5af
coverage: 0.477477
learned_at: 2026-10-26 01:55:46
nodes: [KSamplerSelect, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, LTXVLatentUpsampler, SamplerCustomAdvanced, GetNode, GetNode, GetNode, CFGGuider, GetNode, GetNode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, SetNode, GetNode, LTXVPreprocess, EmptyLTXVLatentVideo, GetImageSize, MarkdownNote, PathchSageAttentionKJ, LTXVChunkFeedForward, GetNode, GetNode, GetNode, GetNode, SetLatentNoiseMask, SetNode, LTXVAudioVAEDecode, Reroute, GetNode, LTXVAudioVAEEncode, SolidMask, SetNode, GetNode, SimpleCalculatorKJ, GetNode, LTXVConditioning, SimpleMath+, GetNode, LTXVEmptyLatentAudio, ComfySwitchNode, PrimitiveFloat, MarkdownNote, VHS_VideoCombine, KSamplerSelect, GetNode, GetNode, CFGGuider, LTXVScheduler, ImageResizeKJv2, SetNode, ImageScaleBy, RandomNoise, RandomNoise, GetNode, SetNode, SetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, Note, GetNode, MarkdownNote, SetNode, VAELoaderKJ, VAELoader, LatentUpscaleModelLoader, ResizeImagesByLongerEdge, ManualSigmas, INTConstant, INTConstant, DualCLIPLoaderGGUF, CLIPTextEncode, CLIPTextEncode, UnetLoaderGGUF, CheckpointLoaderSimple, CheckpointLoaderSimple, LoraLoaderModelOnly, LoadAudio, LoadImage, TrimAudioDuration, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-phr00tmerge-nsfw-v5.safetensors", "height": 25, "width": 121}
---

# 数字人/数字人/LTX-2数字人换2.3模型 表情口型同步_2019717989897084929.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX-2数字人换2.3模型 表情口型同步_2019717989897084929.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（111 个）：
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `LTXVConditioning`
- `SimpleMath+`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `ComfySwitchNode`
- `PrimitiveFloat`
- `MarkdownNote`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `CFGGuider`
- `LTXVScheduler`
- `ImageResizeKJv2`
- `SetNode`
- `ImageScaleBy`
- `RandomNoise`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `Note`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `VAELoaderKJ`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `ResizeImagesByLongerEdge`
- `ManualSigmas`
- `INTConstant`
- `INTConstant`
- `DualCLIPLoaderGGUF`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `LoadImage`
- `TrimAudioDuration`
- `INTConstant`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-phr00tmerge-nsfw-v5.safetensors`

## 知识

覆盖率 **48%**（53/111）

**有卡**：`KSamplerSelect`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`CFGGuider`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`GetImageSize`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`SetLatentNoiseMask`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`SolidMask`、`SimpleCalculatorKJ`、`LTXVConditioning`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`LTXVScheduler`、`ImageResizeKJv2`、`ImageScaleBy`、`RandomNoise`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`VAELoaderKJ`、`VAELoader`、`LatentUpscaleModelLoader`、`ResizeImagesByLongerEdge`、`ManualSigmas`、`INTConstant`、`DualCLIPLoaderGGUF`、`CLIPTextEncode`、`UnetLoaderGGUF`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LoadAudio`、`LoadImage`、`TrimAudioDuration`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
