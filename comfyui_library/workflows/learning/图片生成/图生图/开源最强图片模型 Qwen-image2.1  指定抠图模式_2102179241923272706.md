---
key: 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102179241923272706.json
name: 开源最强图片模型 Qwen-image2.1  指定抠图模式_2102179241923272706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102179241923272706.json
hash: f69ba5cf2ef4eb86
coverage: 0.666667
learned_at: 2026-10-09 22:27:09
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, 孤海注释, MarkdownNote, Note Plus (mtb), LoadImage, VAEDecode, CR Text, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: [CR Text, Note Plus (mtb)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 739076692602264, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102179241923272706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102179241923272706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `孤海注释`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `VAEDecode` ★核心
- `CR Text`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `739076692602264`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`

**缺卡**（2）：`CR Text`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
