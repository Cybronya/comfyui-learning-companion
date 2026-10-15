---
key: 图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json
name: Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json
hash: 37ba621a8ad9ab57
coverage: 0.955556
learned_at: 2026-10-15 22:27:06
nodes: [CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy promptConcat, easy setNode, easy setNode, easy textIndexSwitch, easy setNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy textIndexSwitch, easy textIndexSwitch, CR Prompt Text, easy getNode, easy getNode, easy getNode, easy promptConcat, CLIPLoader, VAELoader, CR Prompt Text, UNETLoader, KSampler, easy seed, EmptyLatentImage, ResolutionSelector, TextEncodeQwenImage21, PreviewAny, SaveImageAdvanced, PreviewImage, VAEDecode, SaveImage, CR Prompt Text, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy promptConcat`
- `easy setNode`
- `easy setNode`
- `easy textIndexSwitch`
- `easy setNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy textIndexSwitch`
- `easy textIndexSwitch`
- `CR Prompt Text`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy promptConcat`
- `CLIPLoader`
- `VAELoader`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `easy seed`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `SaveImageAdvanced`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `CR Prompt Text`
- `INTConstant`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（43/45）

**有卡**：`CR Prompt Text`、`easy promptConcat`、`easy setNode`、`easy textIndexSwitch`、`easy getNode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`easy seed`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`INTConstant`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
