---
key: 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json
name: CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json
hash: 23911ab6b611edc2
coverage: 0.833333
learned_at: 2026-10-09 22:09:17
nodes: [LoraLoaderModelOnly, VAEDecode, UNETLoader, KSampler, SaveImage, LoadImage, VAELoader, CLIPLoader, PrimitiveStringMultiline, TextEncodeQwenImage21, LoadImage, Get resolution [Crystools]]
patterns: []
missing: [Get resolution [Crystools]]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 343195011140730, "steps": 25}
discoveries: [次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2104392510440304641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `LoadImage`
- `Get resolution [Crystools]`

## 关键参数

- `seed` = `343195011140730`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`KSampler`、`SaveImage`、`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`

**缺卡**（1）：`Get resolution [Crystools]`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明
