---
key: 视频生成/图生视频/wan2.2首-中-尾循环（补帧）_1989252232006742017.json
name: wan2.2首-中-尾循环（补帧）_1989252232006742017.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2首-中-尾循环（补帧）_1989252232006742017.json
hash: ca8814919603b1bd
coverage: 0.521127
learned_at: 2026-10-15 22:33:06
nodes: [SetNode, SetNode, GetNode, GetNode, PrimitiveInt, SetNode, SetNode, ModelSamplingSD3, GetNode, GetNode, SetNode, PrimitiveInt, SetNode, ModelSamplingSD3, SetNode, VAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, easy batchAnything, MathExpression|pysssss, easy showAnything, easy showAnything, Int, Int, GetNode, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, easy int, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, CLIPLoader, UNETLoader, UNETLoader, GetImageRangeFromBatch, KSamplerAdvanced, KSamplerAdvanced, ColorMatch, WanAdvancedI2V, easy forLoopStart, MathExpression|pysssss, easy forLoopEnd, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode, PrimitiveInt, PrimitiveInt, easy int, LoadImage, TrimVideoLatent, VAEDecode, ImageFromBatch, PrimitiveFloat, VHS_LoadVideo, VHS_VideoCombine, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2首-中-尾循环（补帧）_1989252232006742017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989252232006742017.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `easy batchAnything`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `Int`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetImageRangeFromBatch`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ColorMatch`
- `WanAdvancedI2V`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `easy forLoopEnd`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `easy int`
- `LoadImage`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `RIFE VFI`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **52%**（37/71）

**有卡**：`ModelSamplingSD3`、`VAELoader`、`easy cleanGpuUsed`、`easy batchAnything`、`MathExpression|pysssss`、`Int`、`easy int`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`GetImageRangeFromBatch`、`KSamplerAdvanced`、`ColorMatch`、`WanAdvancedI2V`、`easy forLoopStart`、`easy forLoopEnd`、`LoadImage`、`CLIPTextEncode`、`TrimVideoLatent`、`VAEDecode`、`ImageFromBatch`、`VHS_LoadVideo`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
