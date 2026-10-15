---
key: 图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json
name: Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json
hash: 0cf8929504a6d983
coverage: 0.928571
learned_at: 2026-10-15 22:27:04
nodes: [Note Plus (mtb), NunchakuQwenImageDiTLoader, CLIPLoader, VAELoader, ModelSamplingAuraFlow, Int, CLIPTextEncode, EmptySD3LatentImage, KSampler, VAEDecode, Int, SaveImage, MarkdownNote, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 998491117779248, "steps": 20}
---

# 图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `Note Plus (mtb)`
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `Int`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Int`
- `SaveImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `998491117779248`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`Note Plus (mtb)`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`Int`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、EmptySD3LatentImage、Int
