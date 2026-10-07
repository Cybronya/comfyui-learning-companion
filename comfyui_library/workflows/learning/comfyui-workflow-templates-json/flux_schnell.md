---
key: comfyui-workflow-templates-json/flux_schnell.json
name: flux_schnell
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/flux_schnell.json
hash: 912fe178607a2c0e
official: true
coverage: 0.777778
learned_at: 2026-10-07 21:35:27
nodes: [CLIPTextEncode, EmptySD3LatentImage, VAEDecode, SaveImage, KSampler, CheckpointLoaderSimple, CLIPTextEncode, Note, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "flux1-schnell-fp8.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 173805153958730, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/flux_schnell.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/flux_schnell.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（9 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `MarkdownNote`

## 关键参数

- `seed` = `173805153958730`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `flux1-schnell-fp8.safetensors`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、EmptySD3LatentImage、sd15-t2i-basic、sd15-t2i-lora

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
