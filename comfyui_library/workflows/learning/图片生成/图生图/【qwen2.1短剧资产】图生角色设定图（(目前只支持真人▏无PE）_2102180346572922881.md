---
key: 图片生成/图生图/【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881.json
name: 【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881.json
hash: d54042f6ba916a2f
coverage: 0.666667
learned_at: 2026-10-10 20:48:13
nodes: [CLIPLoader, SaveImageAdvanced, VAELoader, UNETLoader, QwenImage21Cache, VAEDecode, ImageConcatMulti, KSampler, CR Prompt Text, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage, LoadImage, CR Prompt Text, CR Prompt Text, ComfySwitchNode, CR Text Concatenate, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, easy boolean, easy float]
patterns: []
missing: [CR Text Concatenate, easy boolean, easy float, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 770510674092, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `SaveImageAdvanced`
- `VAELoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `KSampler` ★核心
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `ComfySwitchNode`
- `CR Text Concatenate`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `easy boolean`
- `easy float`

## 关键参数

- `seed` = `770510674092`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（16/24）

**有卡**：`CLIPLoader`、`SaveImageAdvanced`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`ImageConcatMulti`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`

**缺卡**（6）：`CR Text Concatenate`、`easy boolean`、`easy float`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
