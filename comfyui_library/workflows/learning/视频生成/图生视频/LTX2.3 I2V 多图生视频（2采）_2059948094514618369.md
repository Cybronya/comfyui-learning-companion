---
key: 视频生成/图生视频/LTX2.3 I2V 多图生视频（2采）_2059948094514618369.json
name: LTX2.3 I2V 多图生视频（2采）_2059948094514618369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 I2V 多图生视频（2采）_2059948094514618369.json
hash: 0e40a116ec8ada75
coverage: 0.6125
learned_at: 2026-10-15 22:38:44
nodes: [GetNode, VAELoaderKJ, CheckpointLoaderSimple, LazySwitchKJ, CreateVideo, SetNode, ImageScaleBy, SetNode, Float to Int, GetNode, KSamplerSelect, PrimitiveBoolean, BasicScheduler, GetNode, VAELoaderKJ, GetNode, LTXVAudioVAEDecode, VAEDecode, VAEDecodeTiled, GetNode, LTXVLatentUpsampler, GetNode, VAELoaderKJ, BasicScheduler, GetNode, SetNode, SetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, Float to Int, CFGGuider, LTXVConcatAVLatent, LatentUpscaleModelLoader, GetNode, LTXSequencer, LTXVConditioning, SamplerCustomAdvanced, LTXVCropGuides, GetNode, LTXVEmptyLatentAudio, GetImageSize, LTXSequencer, LTXVSeparateAVLatent, GetNode, LTXVConcatAVLatent, easy mathInt, easy mathInt, CLIPTextEncode, GetNode, ConditioningZeroOut, GetNode, CFGGuider, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, KSamplerSelect, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SaveVideo, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, LTXVSeparateAVLatent, RandomNoise, MultiImageLoader, Int, Text, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, SetNode, LTXAVTextEncoderLoader, SetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 1}
---

# 视频生成/图生视频/LTX2.3 I2V 多图生视频（2采）_2059948094514618369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059948094514618369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `GetNode`
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `LazySwitchKJ`
- `CreateVideo`
- `SetNode`
- `ImageScaleBy`
- `SetNode`
- `Float to Int`
- `GetNode`
- `KSamplerSelect` ★核心
- `PrimitiveBoolean`
- `BasicScheduler`
- `GetNode`
- `VAELoaderKJ`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `VAELoaderKJ`
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Float to Int`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `GetNode`
- `LTXSequencer`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `LTXSequencer`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVConcatAVLatent`
- `easy mathInt`
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SaveVideo`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `MultiImageLoader`
- `Int`
- `Text`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXAVTextEncoderLoader`
- `SetNode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `1`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（49/80）

**有卡**：`VAELoaderKJ`、`CheckpointLoaderSimple`、`LazySwitchKJ`、`CreateVideo`、`ImageScaleBy`、`Float to Int`、`KSamplerSelect`、`PrimitiveBoolean`、`BasicScheduler`、`LTXVAudioVAEDecode`、`VAEDecode`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`LTXSequencer`、`LTXVConditioning`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`GetImageSize`、`LTXVSeparateAVLatent`、`easy mathInt`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLTXVLatentVideo`、`SaveVideo`、`RandomNoise`、`MultiImageLoader`、`Int`、`Text`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
