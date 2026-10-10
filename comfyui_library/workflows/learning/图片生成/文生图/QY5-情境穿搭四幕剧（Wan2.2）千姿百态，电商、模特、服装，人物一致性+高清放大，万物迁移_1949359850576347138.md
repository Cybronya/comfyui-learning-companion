---
key: QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138.json
name: QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138.json
hash: 023c1b578b3549ab
coverage: 0.659091
learned_at: 2026-10-10 20:58:50
nodes: [easy bookmark, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UnetLoaderGGUF, UnetLoaderGGUF, PathchSageAttentionKJ, ModelSamplingSD3, Any Switch (rgthree), Any Switch (rgthree), SimpleMath+, easy showAnything, EmptyHunyuanLatentVideo, CLIPTextEncode, PathchSageAttentionKJ, KSamplerAdvanced, ModelSamplingSD3, Int, easy negative, CLIPTextEncode, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, Int, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UpscaleModelLoader, Note, Note, easy cleanGpuUsed, VAEDecode, easy positive, easy positive, easy positive, easy positive, easy positive, SaveImage, SaveImage, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: [SimpleMath+, easy bookmark, easy cleanGpuUsed, easy positive, easy positive, easy positive, easy positive, easy positive, easy negative]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy bookmark` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy negative` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（44 个）：
- `easy bookmark`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SimpleMath+`
- `easy showAnything`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `Int`
- `easy negative`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy positive`
- `easy positive`
- `easy positive`
- `easy positive`
- `easy positive`
- `SaveImage`
- `SaveImage`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **66%**（29/44）

**有卡**：`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`Int`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`UpscaleModelLoader`、`VAEDecode`、`SaveImage`、`RHHiddenNodes`

**缺卡**（9）：`SimpleMath+`、`easy bookmark`、`easy cleanGpuUsed`、`easy positive`、`easy positive`、`easy positive`、`easy positive`、`easy positive`、`easy negative`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy bookmark` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy negative` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
