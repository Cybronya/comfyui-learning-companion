---
key: 图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json
name: Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json
hash: e179ff90db03c8ed
coverage: 0.90625
learned_at: 2026-10-15 22:27:37
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, CLIPTextEncode, CR Text Concatenate, VAELoader, CLIPLoader, easy showAnything, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, Note, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, CFGZeroStarAndInit, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, CFGZeroStarAndInit, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VAEDecode, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), CFGZeroStarAndInit, LoraLoaderModelOnly, SaveImage, UNETLoader, Image Comparer (rgthree), UNETLoader, RH_LLMAPI_NODE, ImpactSwitch, ImpactInt, ImpactInt, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（64 个）：
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `ImpactInt`
- `ImpactInt`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **91%**（58/64）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`CR Text Concatenate`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CFGZeroStarAndInit`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`SaveImage`、`UNETLoader`、`RH_LLMAPI_NODE`、`ImpactInt`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStarAndInit
