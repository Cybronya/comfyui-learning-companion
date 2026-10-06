---
key: 图片生成/文生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json
name: Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json
hash: f97f0087fa2eea53
coverage: 0.9
learned_at: 2026-10-06 21:49:57
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, SaveImage, SaveImageAdvanced, KSampler, UNETLoader, TextEncodeQwenImage21, LoadImage]
patterns: []
missing: [SaveImageAdvanced]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1029469300658431, "steps": 25}
discoveries: [次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`

## 关键参数

- `seed` = `1029469300658431`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`KSampler`、`UNETLoader`、`TextEncodeQwenImage21`、`LoadImage`

**缺卡**（1）：`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

## 学习发现

- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
