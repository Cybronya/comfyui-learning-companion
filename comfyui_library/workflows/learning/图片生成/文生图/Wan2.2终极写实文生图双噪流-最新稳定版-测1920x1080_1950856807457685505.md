---
key: 图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json
name: Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json
hash: e179ff90db03c8ed
coverage: 0.859375
learned_at: 2026-10-10 20:59:14
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, CLIPTextEncode, CR Text Concatenate, VAELoader, CLIPLoader, easy showAnything, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, Note, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, CFGZeroStarAndInit, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, CFGZeroStarAndInit, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VAEDecode, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), CFGZeroStarAndInit, LoraLoaderModelOnly, SaveImage, UNETLoader, Image Comparer (rgthree), UNETLoader, RH_LLMAPI_NODE, ImpactSwitch, ImpactInt, ImpactInt, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, SaveImage, SaveImage]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate]
parameters: {"cfg": 10, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json`

## 结构

**节点**（64 个）：
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `Note`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `Image Comparer (rgthree)`
- `UNETLoader`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `ImpactInt`
- `ImpactInt`
- `CR Text`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CR Text`
- `SaveImage`
- `SaveImage`

## 关键参数

- `cfg` = `10`
- `denoise` = `bong_tangent`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `seed` = `disable`
- `steps` = `fixed`

## 知识

覆盖率 **86%**（55/64）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`CR Text Concatenate`、`VAELoader`、`CLIPLoader`、`easy showAnything`、`LoraLoaderModelOnly`、`CFGZeroStarAndInit`、`ModelSamplingSD3`、`Note`、`KSamplerAdvanced`、`VAEDecode`、`Image Comparer (rgthree)`、`SaveImage`、`UNETLoader`、`RH_LLMAPI_NODE`、`ImpactSwitch`

**缺卡**（3）：`CR Text`、`CR Text`、`CR Text Concatenate`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
