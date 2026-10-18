---
key: 视频生成/图生视频/Wan2.2 SVIPro 单图长视频官方流循环版_2006023297154158593.json
name: Wan2.2 SVIPro 单图长视频官方流循环版_2006023297154158593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 SVIPro 单图长视频官方流循环版_2006023297154158593.json
hash: 427fe0bc901f2218
coverage: 0.825397
learned_at: 2026-10-15 22:34:00
nodes: [UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, easy indexAnything, easy int, easy mathInt, easy indexAnything, StringToFloatList, easy lengthAnything, easy forLoopStart, easy forLoopEnd, VAEEncode, ModelPatchTorchSettings, SaveVideoRGBA, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, easy mathInt, easy indexAnything, easy mathInt, easy ifElse, MathExpression|pysssss, easy convertAnything, easy mathInt, easy mathInt, MathExpression|pysssss, easy compare, easy mathInt, CLIPTextEncode, easy forLoopStart, easy indexAnything, ImageResizeKJv2, easy int, ProcessString, easy promptLine, easy lengthAnything, MathExpression|pysssss, MathExpression|pysssss, easy compare, easy ifElse, VAEDecode, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro, easy forLoopEnd, easy blocker, easy indexAnything, SaveImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, UNETLoader, MathExpression|pysssss, WanMoeKSampler, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 SVIPro 单图长视频官方流循环版_2006023297154158593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006023297154158593.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
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
- `VAEEncode` ★核心
- `ModelPatchTorchSettings`
- `SaveVideoRGBA`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `easy mathInt`
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
- `easy forLoopStart`
- `easy indexAnything`
- `ImageResizeKJv2`
- `easy int`
- `ProcessString`
- `easy promptLine`
- `easy lengthAnything`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy compare`
- `easy ifElse`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `WanImageToVideoSVIPro`
- `easy forLoopEnd`
- `easy blocker`
- `easy indexAnything`
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `WanMoeKSampler` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **83%**（52/63）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`easy indexAnything`、`easy int`、`easy mathInt`、`StringToFloatList`、`easy lengthAnything`、`easy forLoopStart`、`easy forLoopEnd`、`VAEEncode`、`ModelPatchTorchSettings`、`SaveVideoRGBA`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`easy convertAnything`、`easy compare`、`ImageResizeKJv2`、`ProcessString`、`easy promptLine`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`WanImageToVideoSVIPro`、`easy blocker`、`SaveImage`、`LoadImage`、`WanMoeKSampler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
