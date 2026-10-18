---
key: 视频生成/图生视频/Wan2.2：图生视频新纪元，静态图像的动态复活！万相图生视频_Wan2.2_图生视频_1953469978659966978.json
name: Wan2.2：图生视频新纪元，静态图像的动态复活！万相图生视频_Wan2.2_图生视频_1953469978659966978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2：图生视频新纪元，静态图像的动态复活！万相图生视频_Wan2.2_图生视频_1953469978659966978.json
hash: ae62d249cb2ef58f
coverage: 0.96875
learned_at: 2026-10-15 22:31:05
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CFGZeroStarAndInit, Seed Everywhere, VAEDecode, ModelSamplingSD3, ImpactInt, SaveVideo, CreateVideo, KSamplerAdvanced, KSamplerAdvanced, LoadImage, WanImageToVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImpactInt, ImpactInt, ImpactInt, MathExpression|pysssss, LoraLoaderModelOnly, ModelSamplingSD3, Wan_video_prompt_generator, CR Text, CR Text, CR Text Concatenate, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAELoader, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 16, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2：图生视频新纪元，静态图像的动态复活！万相图生视频_Wan2.2_图生视频_1953469978659966978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953469978659966978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（32 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `Seed Everywhere`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ImpactInt`
- `SaveVideo`
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `Wan_video_prompt_generator`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `16`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`PathchSageAttentionKJ`、`CFGZeroStarAndInit`、`Seed Everywhere`、`VAEDecode`、`ModelSamplingSD3`、`ImpactInt`、`SaveVideo`、`CreateVideo`、`KSamplerAdvanced`、`LoadImage`、`WanImageToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`MathExpression|pysssss`、`Wan_video_prompt_generator`、`CR Text`、`CR Text Concatenate`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
