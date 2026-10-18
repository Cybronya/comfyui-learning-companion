---
key: 视频生成/图生视频/Wan2.2 SVIPro多图分镜官方流循环版_2006938927231406082.json
name: Wan2.2 SVIPro多图分镜官方流循环版_2006938927231406082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 SVIPro多图分镜官方流循环版_2006938927231406082.json
hash: 89c498888233f7c5
coverage: 0.838235
learned_at: 2026-10-15 22:34:03
nodes: [UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, easy indexAnything, easy int, easy mathInt, easy indexAnything, StringToFloatList, easy lengthAnything, easy forLoopStart, easy forLoopEnd, ModelPatchTorchSettings, SaveVideoRGBA, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, easy indexAnything, easy mathInt, easy ifElse, MathExpression|pysssss, easy convertAnything, easy mathInt, easy mathInt, MathExpression|pysssss, easy compare, easy mathInt, CLIPTextEncode, easy indexAnything, ProcessString, easy promptLine, easy lengthAnything, easy compare, easy ifElse, VAEDecode, ImageBatchExtendWithOverlap, easy forLoopEnd, easy blocker, easy indexAnything, SaveImage, PrimitiveInt, UNETLoader, MathExpression|pysssss, WanMoeKSampler, PrimitiveInt, PrimitiveFloat, PrimitiveInt, PrimitiveInt, easy int, WanImageToVideoSVIPro, easy forLoopStart, PrimitiveInt, MarkdownNote, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, easy mathInt, easy indexAnything, ImageResizeKJv2, VAEEncode, MathExpression|pysssss, MathExpression|pysssss, ImageBatchMulti, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 SVIPro多图分镜官方流循环版_2006938927231406082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006938927231406082.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy indexAnything`
- `easy int`
- `easy mathInt`
- `easy indexAnything`
- `StringToFloatList`
- `easy lengthAnything`
- `easy forLoopStart`
- `easy forLoopEnd`
- `ModelPatchTorchSettings`
- `SaveVideoRGBA`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `easy indexAnything`
- `easy mathInt`
- `easy ifElse`
- `MathExpression|pysssss`
- `easy convertAnything`
- `easy mathInt`
- `easy mathInt`
- `MathExpression|pysssss`
- `easy compare`
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `ProcessString`
- `easy promptLine`
- `easy lengthAnything`
- `easy compare`
- `easy ifElse`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `easy forLoopEnd`
- `easy blocker`
- `easy indexAnything`
- `SaveImage`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `WanMoeKSampler` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy int`
- `WanImageToVideoSVIPro`
- `easy forLoopStart`
- `PrimitiveInt`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `easy mathInt`
- `easy indexAnything`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageBatchMulti`
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **84%**（57/68）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`easy indexAnything`、`easy int`、`easy mathInt`、`StringToFloatList`、`easy lengthAnything`、`easy forLoopStart`、`easy forLoopEnd`、`ModelPatchTorchSettings`、`SaveVideoRGBA`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`easy convertAnything`、`easy compare`、`ProcessString`、`easy promptLine`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`easy blocker`、`SaveImage`、`WanMoeKSampler`、`WanImageToVideoSVIPro`、`LoadImage`、`ImageResizeKJv2`、`VAEEncode`、`ImageBatchMulti`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
