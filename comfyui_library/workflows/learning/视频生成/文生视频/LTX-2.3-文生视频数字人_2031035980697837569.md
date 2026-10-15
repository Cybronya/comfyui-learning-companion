---
key: 视频生成/文生视频/LTX-2.3-文生视频数字人_2031035980697837569.json
name: LTX-2.3-文生视频数字人_2031035980697837569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-文生视频数字人_2031035980697837569.json
hash: 21e0ee9526f474c1
coverage: 0.716418
learned_at: 2026-10-15 22:44:41
nodes: [VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, SamplerCustomAdvanced, CFGGuider, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVCropGuides, EmptyLTXVLatentVideo, SimpleMath+, CR Float To Integer, MelBandRoFormerSampler, SetLatentNoiseMask, GetNode, SolidMask, LTXVSeparateAVLatent, GetNode, GetNode, SimpleMath+, LTXVAudioVAEEncode, CLIPTextEncode, ImageSharpen, VHS_VideoCombine, DualCLIPLoader, MelBandRoFormerModelLoader, SoundFlow_GetLength, SetNode, PreviewAudio, PreviewAny, VAEDecodeTiled, GetNode, easy cleanGpuUsed, easy showAnything, CR Prompt Text, VHS_VideoCombine, Note, TrimAudioDuration, TextGenerateLTX2Prompt, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, DiffusionModelLoaderKJ, LoraLoaderModelOnly, CLIPTextEncode, KSampler, KSamplerSelect, BasicScheduler, SigmasPreview, RandomNoise, Note, Note, LoadAudio, Note, Note, FloatConstant, SetNode, SimpleMath+, LTXVConditioning, GetNode, GetNode, Int, Int, PrimitiveFloat]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.4, "sampler_name": "euler_ancestral_cfg_pp", "scheduler": "simple", "seed": 345701868114235, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX-2.3-文生视频数字人_2031035980697837569.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-文生视频数字人_2031035980697837569.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（67 个）：
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `CR Float To Integer`
- `MelBandRoFormerSampler` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `SolidMask`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageSharpen`
- `VHS_VideoCombine`
- `DualCLIPLoader`
- `MelBandRoFormerModelLoader`
- `SoundFlow_GetLength`
- `SetNode`
- `PreviewAudio`
- `PreviewAny`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `easy showAnything`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `Note`
- `TrimAudioDuration`
- `TextGenerateLTX2Prompt`
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SigmasPreview`
- `RandomNoise`
- `Note`
- `Note`
- `LoadAudio`
- `Note`
- `Note`
- `FloatConstant`
- `SetNode`
- `SimpleMath+`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `PrimitiveFloat`

## 关键参数

- `seed` = `345701868114235`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **72%**（48/67）

**有卡**：`VAELoaderKJ`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`CR Float To Integer`、`MelBandRoFormerSampler`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`ImageSharpen`、`VHS_VideoCombine`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`SoundFlow_GetLength`、`PreviewAudio`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`CR Prompt Text`、`TrimAudioDuration`、`TextGenerateLTX2Prompt`、`LatentUpscaleModelLoader`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`KSampler`、`KSamplerSelect`、`BasicScheduler`、`SigmasPreview`、`RandomNoise`、`LoadAudio`、`FloatConstant`、`LTXVConditioning`、`Int`

**用到的条目**：KSampler、LoraLoaderModelOnly、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
