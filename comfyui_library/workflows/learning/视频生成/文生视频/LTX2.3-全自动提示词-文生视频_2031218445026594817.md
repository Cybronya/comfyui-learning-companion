---
key: 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json
name: LTX2.3-全自动提示词-文生视频_2031218445026594817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json
hash: 7e6404902a8a1d23
coverage: 0.714286
learned_at: 2026-10-11 03:16:46
nodes: [LTXVAudioVAELoader, CLIPTextEncode, TextGenerateLTX2Prompt, PreviewAny, CFGGuider, LTXVScheduler, LTXVCropGuides, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, CreateVideo, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, RandomNoise, VAEDecodeTiled, VAEDecode, LTXVAudioVAEDecode, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, SaveVideo, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly, CR Prompt Text, Note, Note, RH_LLMAPI_Pro_Node, CR Prompt Text, LTXAVTextEncoderLoader, CLIPTextEncode, PrimitiveFloat, LTXVEmptyLatentAudio, ImageScaleBy, PrimitiveInt, CM_IntToFloat, PrimitiveInt, CR Prompt Text, easy int, easy int, SimpleMath+, Note, easy showAnything, LatentUpscaleModelLoader]
patterns: []
missing: [SimpleMath+, easy int, easy int, CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 877239004040496, "steps": 4, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `CFGGuider`
- `LTXVScheduler`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `Note`
- `Note`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `PrimitiveInt`
- `CM_IntToFloat`
- `PrimitiveInt`
- `CR Prompt Text`
- `easy int`
- `easy int`
- `SimpleMath+`
- `Note`
- `easy showAnything`
- `LatentUpscaleModelLoader`

## 关键参数

- `seed` = `877239004040496`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（35/49）

**有卡**：`LTXVAudioVAELoader`、`CLIPTextEncode`、`TextGenerateLTX2Prompt`、`CFGGuider`、`LTXVScheduler`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`KSampler`、`LTXVSeparateAVLatent`、`CreateVideo`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConditioning`、`RandomNoise`、`VAEDecodeTiled`、`VAEDecode`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`EmptyImage`、`EmptyLTXVLatentVideo`、`GetImageSize`、`SaveVideo`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`RH_LLMAPI_Pro_Node`、`LTXAVTextEncoderLoader`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`CM_IntToFloat`、`LatentUpscaleModelLoader`

**缺卡**（6）：`SimpleMath+`、`easy int`、`easy int`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
