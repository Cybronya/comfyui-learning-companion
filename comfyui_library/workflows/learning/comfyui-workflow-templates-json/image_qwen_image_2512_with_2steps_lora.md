---
key: comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json
name: image_qwen_image_2512_with_2steps_lora
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json
hash: 3a95c94c18872d88
official: true
coverage: 0.846154
learned_at: 2026-10-10 22:48:28
nodes: [CLIPLoader, UNETLoader, VAELoader, EmptySD3LatentImage, MarkdownNote, VAEDecode, LoraLoaderModelOnly, KSampler, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPTextEncode, SaveImage, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 318036859179089, "steps": 2}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptySD3LatentImage`
- `MarkdownNote`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `seed` = `318036859179089`
- `steps` = `2`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`EmptySD3LatentImage`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
