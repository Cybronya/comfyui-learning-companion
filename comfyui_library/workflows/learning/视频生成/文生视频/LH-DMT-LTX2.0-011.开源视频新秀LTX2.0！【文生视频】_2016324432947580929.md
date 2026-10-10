---
key: 视频生成/文生视频/LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929.json
name: LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929.json
hash: 812862f0cd7126f1
coverage: 0.72
learned_at: 2026-10-11 03:07:08
nodes: [easy int, easy int, easy int, CR Text, PrimitiveNode, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, ImageScaleBy, GetImageSize, PrimitiveInt, PrimitiveFloat, MarkdownNote, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, CFGGuider, KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, Reroute, LoraLoaderModelOnly, LatentUpscaleModelLoader, RandomNoise, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, CFGGuider, CreateVideo, VAEDecodeTiled, VAEDecode, LTXVAudioVAEDecode, SimpleMath+, SaveVideo, MarkdownNote, MarkdownNote]
patterns: []
missing: [CR Text, SimpleMath+, easy int, easy int, easy int]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `easy int`
- `easy int`
- `easy int`
- `CR Text`
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `PrimitiveInt`
- `PrimitiveFloat`
- `MarkdownNote`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SimpleMath+`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（36/50）

**有卡**：`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`ManualSigmas`、`CreateVideo`、`VAEDecodeTiled`、`VAEDecode`、`LTXVAudioVAEDecode`、`SaveVideo`

**缺卡**（5）：`CR Text`、`SimpleMath+`、`easy int`、`easy int`、`easy int`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
