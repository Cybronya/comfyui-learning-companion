---
key: 视频生成/图生视频/LTX2.0数字人 自适应音频 效果还可以_2010630264770269185.json
name: LTX2.0数字人 自适应音频 效果还可以_2010630264770269185.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010630264770269185.json
hash: 6e764a19cfe5a881
coverage: 0.710526
learned_at: 2026-10-15 22:34:18
nodes: [KSamplerSelect, BasicScheduler, RandomNoise, GetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, easy cleanGpuUsed, SetNode, SetNode, CheckpointLoaderSimple, CLIPTextEncode, LTXVConditioning, AudioSeparation, GetNode, LTXVAudioVAEEncode, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, PathchSageAttentionKJ, easy cleanGpuUsed, GetNode, SimpleMath+, SimpleMath+, SetNode, TrimAudioDuration, Reroute, ImageScaleBy, Reroute, LTXVPreprocess, EmptyLTXVLatentVideo, ImageResizeKJv2, LTXVImgToVideoInplace, Reroute, SolidMask, LTXVConcatAVLatent, SetLatentNoiseMask, SetLatentNoiseMask, LTXVPreprocess, SolidMask, GetImageSizeAndCount, GetNode, GetNode, easy cleanGpuUsed, Reroute, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, BasicScheduler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, VAEDecodeTiled, GetImageSizeAndCount, SetNode, GetNode, SamplerCustomAdvanced, SetNode, easy cleanGpuUsed, ImpactInt, ImpactInt, ImpactInt, MarkdownNote, MarkdownNote, Float, CFGGuider, Note Plus (mtb), MarkdownNote, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, LoadAudio, CLIPTextEncode, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2-19b-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.0数字人 自适应音频 效果还可以_2010630264770269185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010630264770269185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（76 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `GetNode`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `AudioSeparation`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `TrimAudioDuration`
- `Reroute`
- `ImageScaleBy`
- `Reroute`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `Reroute`
- `SolidMask`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `SolidMask`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `Reroute`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `easy cleanGpuUsed`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `MarkdownNote`
- `MarkdownNote`
- `Float`
- `CFGGuider`
- `Note Plus (mtb)`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **71%**（54/76）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTXVConditioning`、`AudioSeparation`、`LTXVAudioVAEEncode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`SimpleMath+`、`TrimAudioDuration`、`ImageScaleBy`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`LTXVImgToVideoInplace`、`SolidMask`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`GetImageSizeAndCount`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`ImpactInt`、`Float`、`CFGGuider`、`Note Plus (mtb)`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`、`CR Text`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
