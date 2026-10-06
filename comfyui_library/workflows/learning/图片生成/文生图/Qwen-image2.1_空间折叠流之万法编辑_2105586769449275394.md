---
key: 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json
name: Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json
hash: eb4c449807f36cd8
coverage: 0.421053
learned_at: 2026-10-06 21:50:07
nodes: [SetNode, SetNode, SetNode, LoadImage, GetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, VAELoader, GetNode, LoadImage, UNETLoader, CLIPLoader, QwenImage21Cache, LoadImage, TextEncodeQwenImage21, SetNode, GetNode, SetNode, GetNode, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, VAEDecode, SaveImage, SetNode, SetNode, LoadImage, Text, ResolutionSelector, 忽略多组孤海]
patterns: []
missing: [Text, 忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 286759499462852, "steps": 35, "width": 1024}
discoveries: [次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `VAELoader`
- `GetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `Text`
- `ResolutionSelector`
- `忽略多组孤海`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `286759499462852`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（16/38）

**有卡**：`LoadImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ResolutionSelector`

**缺卡**（2）：`Text`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Text` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
