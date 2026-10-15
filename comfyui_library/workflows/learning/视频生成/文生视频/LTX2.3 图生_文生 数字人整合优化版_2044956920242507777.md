---
key: 视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json
name: LTX2.3 图生_文生 数字人整合优化版_2044956920242507777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json
hash: 0551046d34a7fde0
coverage: 0.79661
learned_at: 2026-10-15 22:44:59
nodes: [Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, INTConstant, SetNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, RandomNoise, SetLatentNoiseMask, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, PreviewAudio, LTXVImgToVideoInplace, GetNode, LTXVSeparateAVLatent, GetNode, VAEDecode, CheckpointLoaderSimple, CLIPTextEncode, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, BasicScheduler, KSampler, LatentUpscaleModelLoader, LTXVImgToVideoInplace, VHS_VideoCombine, INTConstant, INTConstant, VHS_LoadAudioUpload, LoadImage, LTXVPreprocess, ImageResizeKJv2, LTXVConditioning, CLIPTextEncode, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVSeparateAVLatent, LTXVLatentUpsampler, GetNode, GetNode, LTXVAudioVAELoader, Note, PrimitiveBoolean]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.5000000000000001, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 614846256472314, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `Reroute`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `RandomNoise`
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `KSampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `VHS_LoadAudioUpload`
- `LoadImage`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `LTXVAudioVAELoader`
- `Note`
- `PrimitiveBoolean`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `614846256472314`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **80%**（47/59）

**有卡**：`LTXVCropGuides`、`INTConstant`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`RandomNoise`、`SetLatentNoiseMask`、`CM_FloatToInt`、`LTXVAudioVAEEncode`、`SolidMask`、`PreviewAudio`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`VAEDecode`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`KSampler`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`VHS_LoadAudioUpload`、`LoadImage`、`LTXVPreprocess`、`ImageResizeKJv2`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVLatentUpsampler`、`LTXVAudioVAELoader`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
