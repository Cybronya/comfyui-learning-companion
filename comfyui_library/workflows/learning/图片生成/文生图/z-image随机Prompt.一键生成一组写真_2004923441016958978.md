---
key: 图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json
name: z-image随机Prompt.一键生成一组写真_2004923441016958978
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json
hash: 63474906c2930402
coverage: 0.875
learned_at: 2026-10-19 22:01:16
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, EmptyLatentImage, VAEDecode, easy forLoopEnd, easy batchAnything, KSampler, DPRandomGenerator, MarkdownNote, MarkdownNote, SaveImage, easy forLoopStart]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "sgm_uniform", "seed": 653432827354203, "steps": 9, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy batchAnything`
- `KSampler` ★核心
- `DPRandomGenerator`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImage`
- `easy forLoopStart`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `653432827354203`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`VAEDecode`、`easy forLoopEnd`、`easy batchAnything`、`KSampler`、`DPRandomGenerator`、`SaveImage`、`easy forLoopStart`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
