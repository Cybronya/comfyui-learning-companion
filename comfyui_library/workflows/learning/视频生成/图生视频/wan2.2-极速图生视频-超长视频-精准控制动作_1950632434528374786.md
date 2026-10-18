---
key: 视频生成/图生视频/wan2.2-极速图生视频-超长视频-精准控制动作_1950632434528374786.json
name: wan2.2-极速图生视频-超长视频-精准控制动作_1950632434528374786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-极速图生视频-超长视频-精准控制动作_1950632434528374786.json
hash: dbeb97e19ef5855d
coverage: 0.918919
learned_at: 2026-10-15 22:30:56
nodes: [ModelSamplingSD3, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, GetImageSizeAndCount, ImageFromBatch, WanImageToVideo, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PathchSageAttentionKJ, PathchSageAttentionKJ, LoadImage, CLIPLoader, VAELoader, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, Text Load Line From File, easy showAnything, easy batchAnything, VHS_VideoCombine, Int, KSamplerAdvanced, KSamplerAdvanced, MathExpression|pysssss, CLIPTextEncode, Text Multiline, Int, ImageSmartSharpen+, VAEDecode, easy forLoopStart, easy showAnything, easy forLoopEnd, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-极速图生视频-超长视频-精准控制动作_1950632434528374786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950632434528374786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `WanImageToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `Text Load Line From File`
- `easy showAnything`
- `easy batchAnything`
- `VHS_VideoCombine`
- `Int`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `Int`
- `ImageSmartSharpen+`
- `VAEDecode` ★核心
- `easy forLoopStart`
- `easy showAnything`
- `easy forLoopEnd`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`LoraLoaderModelOnly`、`GetImageSizeAndCount`、`ImageFromBatch`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`LoadImage`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`Text Load Line From File`、`easy batchAnything`、`VHS_VideoCombine`、`Int`、`KSamplerAdvanced`、`MathExpression|pysssss`、`Text Multiline`、`ImageSmartSharpen+`、`VAEDecode`、`easy forLoopStart`、`easy forLoopEnd`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
