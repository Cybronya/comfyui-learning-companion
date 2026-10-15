---
key: 视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json
name: 🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json
hash: fbc1877d08ac8df1
coverage: 0.796296
learned_at: 2026-10-15 22:49:14
nodes: [LTXVScheduler, LTXAVTextEncoderLoader, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, ImageScaleBy, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, RandomNoise, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, PrimitiveNode, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, KSamplerSelect, MarkdownNote, CLIPTextEncode, MarkdownNote, LTXVLatentUpsampler, EmptyImage, CreateVideo, GetImageSize, SimpleMath+, easy int, easy int, CLIPTextEncode, Note Plus (mtb), MarkdownNote, MarkdownNote, MarkdownNote, SaveVideo, MarkdownNote, CR Text, RH_LLMAPI_NODE, easy showAnything, easy int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `ImageScaleBy`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `PrimitiveNode`
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LTXVLatentUpsampler` ★核心
- `EmptyImage`
- `CreateVideo`
- `GetImageSize`
- `SimpleMath+`
- `easy int`
- `easy int`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `MarkdownNote`
- `CR Text`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `easy int`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **80%**（43/54）

**有卡**：`LTXVScheduler`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`EmptyImage`、`CreateVideo`、`GetImageSize`、`SimpleMath+`、`easy int`、`Note Plus (mtb)`、`SaveVideo`、`CR Text`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
