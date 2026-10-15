---
key: 图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json
name: Wan2.2终极写实文生图双噪流_1950564507682787330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json
hash: c48ac1e3008d72a4
coverage: 0.909091
learned_at: 2026-10-15 22:27:37
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, CFGZeroStarAndInit, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStarAndInit, UNETLoader, CLIPTextEncode, CR Text Concatenate, VAELoader, CLIPLoader, SaveImage, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SaveImage, VAEDecode, ModelSamplingSD3, ImpactInt, ImpactInt, ImpactSwitch, Note, VAEDecode, CR Text, RH_LLMAPI_NODE, CR Text, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStarAndInit`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `ImpactSwitch`
- `Note`
- `VAEDecode` ★核心
- `CR Text`
- `RH_LLMAPI_NODE`
- `CR Text`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`CFGZeroStarAndInit`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CR Text Concatenate`、`VAELoader`、`CLIPLoader`、`SaveImage`、`KSamplerAdvanced`、`VAEDecode`、`ImpactInt`、`CR Text`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStarAndInit
