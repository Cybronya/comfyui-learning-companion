---
key: 图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json
name: Boogu-Image 0.1 单图编辑_2067856537388933122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json
hash: d6cb26e57597c263
coverage: 0.928571
learned_at: 2026-10-19 23:21:16
nodes: [UNETLoader, EmptyLatentImage, ModelSamplingAuraFlow, CLIPLoader, SamplerCustom, PreviewImage, KSamplerSelect, VAELoader, LoadImage, BasicScheduler, VAEDecode, SaveImage, TextEncodeBooguEdit, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `SamplerCustom` ★核心
- `PreviewImage`
- `KSamplerSelect` ★核心
- `VAELoader`
- `LoadImage`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeBooguEdit`
- `Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`UNETLoader`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`CLIPLoader`、`SamplerCustom`、`KSamplerSelect`、`VAELoader`、`LoadImage`、`BasicScheduler`、`VAEDecode`、`SaveImage`、`TextEncodeBooguEdit`、`Text`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
