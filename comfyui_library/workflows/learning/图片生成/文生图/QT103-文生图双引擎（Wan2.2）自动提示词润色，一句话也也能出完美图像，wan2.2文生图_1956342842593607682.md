---
key: 图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json
name: QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json
hash: c2f1261c3dd51333
coverage: 0.604651
learned_at: 2026-10-10 20:58:49
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, PathchSageAttentionKJ, KSamplerAdvanced, PathchSageAttentionKJ, ModelSamplingSD3, Any Switch (rgthree), KSamplerAdvanced, Any Switch (rgthree), CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, SimpleMath+, easy showAnything, UnetLoaderGGUF, UnetLoaderGGUF, easy negative, easy bookmark, Note, Int, easy int, CR Text, CR Text, PlaySound|pysssss, easy int, VAEDecode, RH_LLMAPI_NODE, UNETLoader, UNETLoader, SaveImage, Int, easy positive, Note, Fast Groups Bypasser (rgthree), Wan_video_prompt_generator, Any Switch (rgthree), Any Switch (rgthree)]
patterns: []
missing: [CR Text, CR Text, PlaySound|pysssss, SimpleMath+, easy bookmark, easy int, easy int, easy positive, easy negative]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 2.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy bookmark` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy negative` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json`

## 结构

**节点**（43 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Any Switch (rgthree)`
- `KSamplerAdvanced`
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `easy showAnything`
- `UnetLoaderGGUF`
- `UnetLoaderGGUF`
- `easy negative`
- `easy bookmark`
- `Note`
- `Int`
- `easy int`
- `CR Text`
- `CR Text`
- `PlaySound|pysssss`
- `easy int`
- `VAEDecode`
- `RH_LLMAPI_NODE`
- `UNETLoader`
- `UNETLoader`
- `SaveImage`
- `Int`
- `easy positive`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Wan_video_prompt_generator`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`

## 关键参数

- `cfg` = `12`
- `denoise` = `simple`
- `sampler_name` = `2.5`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `randomize`

## 知识

覆盖率 **60%**（26/43）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`Any Switch (rgthree)`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`SimpleMath+`、`easy showAnything`、`UnetLoaderGGUF`、`easy negative`、`easy bookmark`、`Note`、`Int`

**缺卡**（9）：`CR Text`、`CR Text`、`PlaySound|pysssss`、`SimpleMath+`、`easy bookmark`、`easy int`、`easy int`、`easy positive`、`easy negative`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy bookmark` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy negative` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
