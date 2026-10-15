---
key: 图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json
name: Wan2.2终极写实文生图双噪流_1950564507682787330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json
hash: c48ac1e3008d72a4
coverage: 0.818182
learned_at: 2026-10-10 20:59:14
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, CFGZeroStarAndInit, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, UNETLoader, CLIPTextEncode, CR Text Concatenate, VAELoader, CLIPLoader, SaveImage, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SaveImage, VAEDecode, ModelSamplingSD3, ImpactInt, ImpactInt, ImpactSwitch, Note, VAEDecode, CR Text, RH_LLMAPI_NODE, CR Text, easy showAnything]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate]
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json`

## 结构

**节点**（33 个）：
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CFGZeroStarAndInit`
- `UNETLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `UNETLoader`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `SaveImage`
- `VAEDecode`
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `ImpactSwitch`
- `Note`
- `VAEDecode`
- `CR Text`
- `RH_LLMAPI_NODE`
- `CR Text`
- `easy showAnything`

## 关键参数

- `cfg` = `10`
- `denoise` = `beta`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `disable`
- `steps` = `randomize`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`CFGZeroStarAndInit`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CR Text Concatenate`、`VAELoader`、`CLIPLoader`、`SaveImage`、`KSamplerAdvanced`、`VAEDecode`、`ImpactInt`、`ImpactSwitch`

**缺卡**（3）：`CR Text`、`CR Text`、`CR Text Concatenate`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
