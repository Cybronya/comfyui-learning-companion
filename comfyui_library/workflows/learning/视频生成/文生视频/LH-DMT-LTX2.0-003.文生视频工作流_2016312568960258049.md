---
key: 视频生成/文生视频/LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049.json
name: LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049.json
hash: 10c20d9330827a84
coverage: 0.9
learned_at: 2026-10-15 22:44:30
nodes: [INTConstant, INTConstant, INTConstant, PrimitiveInt, PrimitiveInt, PrimitiveFloat, EmptyImage, LatentUpscaleModelLoader, ImageScaleBy, LTXVLatentUpsampler, GetImageSize, LTXVConditioning, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, CFGGuider, RandomNoise, KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAEDecode, RandomNoise, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, VAEDecodeTiled, LTXVSeparateAVLatent, Note, VHS_VideoCombine, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（40 个）：
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `EmptyImage`
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `LTXVLatentUpsampler` ★核心
- `GetImageSize`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `Note`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`INTConstant`、`EmptyImage`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`LTXVLatentUpsampler`、`GetImageSize`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`ManualSigmas`、`VAEDecodeTiled`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
