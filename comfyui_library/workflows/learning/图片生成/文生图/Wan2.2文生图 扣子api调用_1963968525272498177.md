---
key: Wan2.2文生图 扣子api调用_1963968525272498177.json
name: Wan2.2文生图 扣子api调用_1963968525272498177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json
hash: 8be20ff811f265ec
coverage: 0.641026
learned_at: 2026-10-10 20:59:14
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, PathchSageAttentionKJ, KSamplerAdvanced, PathchSageAttentionKJ, ModelSamplingSD3, Any Switch (rgthree), KSamplerAdvanced, Any Switch (rgthree), CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, SimpleMath+, easy showAnything, UnetLoaderGGUF, UnetLoaderGGUF, easy negative, Int, easy int, PlaySound|pysssss, easy int, VAEDecode, UNETLoader, UNETLoader, Int, Note, Fast Groups Bypasser (rgthree), Wan_video_prompt_generator, Any Switch (rgthree), SaveImage, Any Switch (rgthree), RunningHub SeedXPro Translator, easy positive]
patterns: []
missing: [PlaySound|pysssss, SimpleMath+, easy int, easy int, easy positive, RunningHub SeedXPro Translator, easy negative]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 2.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub SeedXPro Translator` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy negative` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# Wan2.2文生图 扣子api调用_1963968525272498177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（39 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Any Switch (rgthree)`
- `KSamplerAdvanced` ★核心
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `easy showAnything`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `easy negative`
- `Int`
- `easy int`
- `PlaySound|pysssss`
- `easy int`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Int`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Wan_video_prompt_generator`
- `Any Switch (rgthree)`
- `SaveImage`
- `Any Switch (rgthree)`
- `RunningHub SeedXPro Translator`
- `easy positive`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `2.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **64%**（25/39）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`UnetLoaderGGUF`、`Int`、`VAEDecode`、`UNETLoader`、`Wan_video_prompt_generator`、`SaveImage`

**缺卡**（7）：`PlaySound|pysssss`、`SimpleMath+`、`easy int`、`easy int`、`easy positive`、`RunningHub SeedXPro Translator`、`easy negative`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub SeedXPro Translator` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy negative` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
