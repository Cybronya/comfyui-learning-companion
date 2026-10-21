---
key: 图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json
name: Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json
hash: 26773d087409e388
coverage: 0.461538
learned_at: 2026-10-21 00:43:23
nodes: [SetNode, SetNode, SetNode, LoadImage, GetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, VAELoader, GetNode, MarkdownNote, LoadImage, UNETLoader, CLIPLoader, QwenImage21Cache, LoadImage, TextEncodeQwenImage21, SetNode, GetNode, SetNode, GetNode, 忽略多组孤海, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, VAEDecode, SaveImage, SetNode, SetNode, LoadImage, Text, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 742126940675529, "steps": 35, "width": 1024}
---

# 图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
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
- `MarkdownNote`
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
- `忽略多组孤海`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `742126940675529`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（18/39）

**有卡**：`LoadImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`忽略多组孤海`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`Text`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
