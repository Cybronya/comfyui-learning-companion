---
key: 图片生成/图生图/开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930.json
name: 开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930.json
hash: 0a8474ebfcfdbab4
coverage: 0.736842
learned_at: 2026-10-10 20:48:17
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, 孤海注释, MarkdownNote, Note Plus (mtb), LoadImage, CLIPLoader, CR Text, TextGenerateLTX2Prompt, KSampler, VAEDecode, TextEncodeQwenImage21, LoadImage, SaveImage]
patterns: []
missing: [CR Text, Note Plus (mtb)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 890474792921099, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `孤海注释`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `CLIPLoader`
- `CR Text`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `890474792921099`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`TextGenerateLTX2Prompt`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImage`

**缺卡**（2）：`CR Text`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
