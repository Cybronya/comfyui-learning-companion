---
key: 图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json
name: Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json
hash: 37631bdc20496f1d
coverage: 0.916667
learned_at: 2026-10-15 22:27:03
nodes: [CR Prompt Text, RH_QwenImagePromptEnhancer, SaveImage, Note, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, TextEncodeQwenImageEditPlus, EmptySD3LatentImage, KSampler, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 24}
---

# 图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CR Prompt Text`
- `RH_QwenImagePromptEnhancer`
- `SaveImage`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `42`
- `steps` = `24`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CR Prompt Text`、`RH_QwenImagePromptEnhancer`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`TextEncodeQwenImageEditPlus`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、TextEncodeQwenImageEditPlus、RH_QwenImagePromptEnhancer
