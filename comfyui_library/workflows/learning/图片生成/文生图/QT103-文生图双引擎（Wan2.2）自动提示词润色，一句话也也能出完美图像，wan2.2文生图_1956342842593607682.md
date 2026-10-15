---
key: 图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json
name: QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json
hash: c2f1261c3dd51333
coverage: 0.813953
learned_at: 2026-10-15 22:26:54
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, PathchSageAttentionKJ, KSamplerAdvanced, PathchSageAttentionKJ, ModelSamplingSD3, Any Switch (rgthree), KSamplerAdvanced, Any Switch (rgthree), CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, SimpleMath+, easy showAnything, UnetLoaderGGUF, UnetLoaderGGUF, easy negative, easy bookmark, Note, Int, easy int, CR Text, CR Text, PlaySound|pysssss, easy int, VAEDecode, RH_LLMAPI_NODE, UNETLoader, UNETLoader, SaveImage, Int, easy positive, Note, Fast Groups Bypasser (rgthree), Wan_video_prompt_generator, Any Switch (rgthree), Any Switch (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 2.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（43 个）：
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
- `easy bookmark`
- `Note`
- `Int`
- `easy int`
- `CR Text`
- `CR Text`
- `PlaySound|pysssss`
- `easy int`
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `Int`
- `easy positive`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Wan_video_prompt_generator`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `2.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`SimpleMath+`、`UnetLoaderGGUF`、`easy negative`、`easy bookmark`、`Int`、`easy int`、`CR Text`、`PlaySound|pysssss`、`VAEDecode`、`RH_LLMAPI_NODE`、`UNETLoader`、`SaveImage`、`easy positive`、`Wan_video_prompt_generator`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
