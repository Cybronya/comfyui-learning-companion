---
key: 视频生成/图生视频/wan2.2-超长视频-一镜到底（VQA+WAN2.2）_1989316745833967618.json
name: wan2.2-超长视频-一镜到底（VQA+WAN2.2）_1989316745833967618.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1989316745833967618.json
hash: 629015cac2ef0a0e
coverage: 0.891892
learned_at: 2026-10-15 22:33:06
nodes: [CLIPTextEncode, WanImageToVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, UNETLoader, VAELoader, CLIPTextEncode, Text Load Line From File, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, ImageSmartSharpen+, VHS_VideoCombine, Int, easy forLoopStart, easy showAnything, easy batchAnything, easy forLoopEnd, GetImageSizeAndCount, ImageFromBatch, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, Qwen3_VQA_Plus, Int, LoadImage, Text Multiline, easy showAnything, easy showAnything, PreviewImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-超长视频-一镜到底（VQA+WAN2.2）_1989316745833967618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989316745833967618.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Text Load Line From File`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageSmartSharpen+`
- `VHS_VideoCombine`
- `Int`
- `easy forLoopStart`
- `easy showAnything`
- `easy batchAnything`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `Qwen3_VQA_Plus`
- `Int`
- `LoadImage`
- `Text Multiline`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`CLIPTextEncode`、`WanImageToVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`Text Load Line From File`、`CLIPLoader`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`、`ImageSmartSharpen+`、`VHS_VideoCombine`、`Int`、`easy forLoopStart`、`easy batchAnything`、`easy forLoopEnd`、`GetImageSizeAndCount`、`ImageFromBatch`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3_VQA_Plus`、`LoadImage`、`Text Multiline`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
