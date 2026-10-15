---
key: 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json
name: qwen2.1基础工作流  i2v  t2v_2102578292409847810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json
hash: af6fa27c2f822fe5
coverage: 0.766667
learned_at: 2026-10-10 20:59:25
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, MarkdownNote, MarkdownNote, Seed (rgthree), UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImageAdvanced, Seed (rgthree), LoadImage, LoadImage, LoadImage, SaveImageAdvanced, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, VAEDecode, SaveImage]
patterns: []
missing: [Seed (rgthree), Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 626015987317164, "steps": 25, "width": 1024}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json`

## 结构

**节点**（30 个）：
- `ResolutionSelector`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `MarkdownNote`
- `MarkdownNote`
- `Seed (rgthree)`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `Seed (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `626015987317164`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`MarkdownNote`、`Seed (rgthree)`、`ComfySwitchNode`、`QwenImage21Cache`、`SaveImageAdvanced`、`LoadImage`

**缺卡**（2）：`Seed (rgthree)`、`Seed (rgthree)`

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
