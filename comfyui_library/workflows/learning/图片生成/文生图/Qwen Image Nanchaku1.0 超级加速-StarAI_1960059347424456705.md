---
key: 图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json
name: Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json
hash: 0cf8929504a6d983
coverage: 0.857143
learned_at: 2026-10-10 20:58:55
nodes: [Note Plus (mtb), NunchakuQwenImageDiTLoader, CLIPLoader, VAELoader, ModelSamplingAuraFlow, Int, CLIPTextEncode, EmptySD3LatentImage, KSampler, VAEDecode, Int, SaveImage, MarkdownNote, CLIPTextEncode]
patterns: []
missing: [Note Plus (mtb)]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 998491117779248, "steps": 20}
discoveries: [次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json`

## 结构

**节点**（14 个）：
- `Note Plus (mtb)`
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `Int`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `VAEDecode`
- `Int`
- `SaveImage`
- `MarkdownNote`
- `CLIPTextEncode`

## 关键参数

- `cfg` = `2.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `998491117779248`
- `steps` = `20`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`Note Plus (mtb)`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`Int`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`Note Plus (mtb)`

## 学习发现

- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
