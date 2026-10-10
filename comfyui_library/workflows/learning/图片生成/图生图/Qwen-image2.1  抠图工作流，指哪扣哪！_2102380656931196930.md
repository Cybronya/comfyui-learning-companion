---
key: 图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json
name: Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json
hash: 59411a240e558f9c
coverage: 0.769231
learned_at: 2026-10-10 20:48:09
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, SaveImage, KSampler, 孤海注释, VAEDecode, CR Text, LoadImage, EmptyLatentImage, ComfySwitchNode]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 560, "sampler_name": "euler", "scheduler": "simple", "seed": 766356591687185, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImage`
- `KSampler` ★核心
- `孤海注释`
- `VAEDecode` ★核心
- `CR Text`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`

## 关键参数

- `seed` = `766356591687185`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `560`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`VAEDecode`、`LoadImage`、`EmptyLatentImage`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
