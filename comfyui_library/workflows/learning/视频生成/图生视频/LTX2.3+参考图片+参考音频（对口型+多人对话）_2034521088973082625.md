---
key: 视频生成/图生视频/LTX2.3+参考图片+参考音频（对口型+多人对话）_2034521088973082625.json
name: LTX2.3+参考图片+参考音频（对口型+多人对话）_2034521088973082625.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034521088973082625.json
hash: c544334a5b57945f
coverage: 0.814815
learned_at: 2026-10-15 22:35:45
nodes: [Reroute, Reroute, GetNode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SetLatentNoiseMask, GetNode, GetImageSizeAndCount, GetNode, SetNode, CFGGuider, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVAudioVAEEncode, LTXVPreprocess, LTXVLatentUpsampler, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SamplerCustomAdvanced, RandomNoise, LTXVPreprocess, PathchSageAttentionKJ, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, KSamplerSelect, BasicScheduler, ImageScaleBy, SolidMask, LTXVConditioning, SolidMask, SetLatentNoiseMask, BasicScheduler, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, GetNode, VHS_VideoCombine, VAEDecodeTiled, GetNode, GetImageSizeAndCount, SetNode, CLIPTextEncode, LoadImage, ImageResizeKJv2, CLIPTextEncode, LoadAudio, TrimAudioDuration, INTConstant]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3+参考图片+参考音频（对口型+多人对话）_2034521088973082625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034521088973082625.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
- `Reroute`
- `Reroute`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `CFGGuider`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEEncode` ★核心
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVPreprocess`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ImageScaleBy`
- `SolidMask`
- `LTXVConditioning`
- `SolidMask`
- `SetLatentNoiseMask`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `TrimAudioDuration`
- `INTConstant`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **81%**（44/54）

**有卡**：`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`GetImageSizeAndCount`、`CFGGuider`、`easy cleanGpuUsed`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`RandomNoise`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`BasicScheduler`、`ImageScaleBy`、`SolidMask`、`LTXVConditioning`、`VHS_VideoCombine`、`VAEDecodeTiled`、`CLIPTextEncode`、`LoadImage`、`ImageResizeKJv2`、`LoadAudio`、`TrimAudioDuration`、`INTConstant`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
