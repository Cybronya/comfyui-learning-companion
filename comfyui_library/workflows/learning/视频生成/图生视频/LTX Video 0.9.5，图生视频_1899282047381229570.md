---
key: 视频生成/图生视频/LTX Video 0.9.5，图生视频_1899282047381229570.json
name: LTX Video 0.9.5，图生视频_1899282047381229570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX Video 0.9.5，图生视频_1899282047381229570.json
hash: b49c377f64e884bf
coverage: 0.711111
learned_at: 2026-10-15 22:29:21
nodes: [SetNode, String Replace (mtb), String Replace (mtb), String Replace (mtb), String Replace (mtb), SetNode, Int, SetNode, SetNode, MathExpression|pysssss, SetNode, Note Plus (mtb), PathchSageAttentionKJ, PatchModelPatcherOrder, ApplyFBCacheOnModel, ConvertAny2Float, Note, VHS_VideoCombine, SetNode, GetNode, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, GetNode, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, ArgosTranslateTextNode, LTXVConditioning, LTXVScheduler, GetNode, GetNode, GetNode, GetNode, ImageResizeKJ, LTXVImgToVideo, StringFunction|pysssss, SamplerCustom, KSamplerSelect, Int, LoadImage, SeargePromptText, VAEDecodeTiled, PlaySound|pysssss, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.5.safetensors"}
---

# 视频生成/图生视频/LTX Video 0.9.5，图生视频_1899282047381229570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899282047381229570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
- `SetNode`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Note Plus (mtb)`
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `ApplyFBCacheOnModel`
- `ConvertAny2Float`
- `Note`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `ArgosTranslateTextNode`
- `LTXVConditioning`
- `LTXVScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `LTXVImgToVideo`
- `StringFunction|pysssss`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `Int`
- `LoadImage`
- `SeargePromptText`
- `VAEDecodeTiled` ★核心
- `PlaySound|pysssss`
- `easy cleanGpuUsed`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.5.safetensors`

## 知识

覆盖率 **71%**（32/45）

**有卡**：`String Replace (mtb)`、`Int`、`MathExpression|pysssss`、`Note Plus (mtb)`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`ApplyFBCacheOnModel`、`ConvertAny2Float`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LayerMask: LoadFlorence2Model`、`LayerUtility: Florence2Image2Prompt`、`ArgosTranslateTextNode`、`LTXVConditioning`、`LTXVScheduler`、`ImageResizeKJ`、`LTXVImgToVideo`、`StringFunction|pysssss`、`SamplerCustom`、`KSamplerSelect`、`LoadImage`、`SeargePromptText`、`VAEDecodeTiled`、`PlaySound|pysssss`、`easy cleanGpuUsed`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、VAEDecodeTiled、LTXVConditioning
