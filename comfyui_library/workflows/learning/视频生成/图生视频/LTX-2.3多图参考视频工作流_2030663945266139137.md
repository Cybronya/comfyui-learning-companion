---
key: 视频生成/图生视频/LTX-2.3多图参考视频工作流_2030663945266139137.json
name: LTX-2.3多图参考视频工作流_2030663945266139137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3多图参考视频工作流_2030663945266139137.json
hash: 98aac5860adaad63
coverage: 0.576271
learned_at: 2026-10-15 22:35:27
nodes: [GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, SimpleMath+, SetNode, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, KSamplerSelect, BasicGuider, EmptyLTXVLatentVideo, SetNode, SimpleMath+, CR Float To Integer, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, LTXVChunkFeedForward, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, VHS_VideoCombine, ImageResize+, ManualSigmas, ManualSigmas, RepeatImageBatch, ImageBatchExtendWithOverlap, DiffusionModelLoaderKJ, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveInt, ImpactInt, SetNode, SetNode, PrimitiveFloat, PrimitiveInt, LoraLoaderModelOnly, DualCLIPLoaderGGUF, LTXVAddGuideMulti, LTXVEmptyLatentAudio, LTXVCropGuides, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/图生视频/LTX-2.3多图参考视频工作流_2030663945266139137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030663945266139137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（59 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SimpleMath+`
- `CR Float To Integer`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `LTXVChunkFeedForward`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `ImageResize+`
- `ManualSigmas`
- `ManualSigmas`
- `RepeatImageBatch`
- `ImageBatchExtendWithOverlap`
- `DiffusionModelLoaderKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoaderGGUF`
- `LTXVAddGuideMulti`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `VAEDecode` ★核心

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（34/59）

**有卡**：`LTXVAudioVAEDecode`、`SimpleMath+`、`LTXVConditioning`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`KSamplerSelect`、`BasicGuider`、`EmptyLTXVLatentVideo`、`CR Float To Integer`、`VAELoaderKJ`、`LTXVChunkFeedForward`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`ImageResize+`、`ManualSigmas`、`RepeatImageBatch`、`ImageBatchExtendWithOverlap`、`DiffusionModelLoaderKJ`、`LoadImage`、`ImpactInt`、`LoraLoaderModelOnly`、`DualCLIPLoaderGGUF`、`LTXVAddGuideMulti`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`VAEDecode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
