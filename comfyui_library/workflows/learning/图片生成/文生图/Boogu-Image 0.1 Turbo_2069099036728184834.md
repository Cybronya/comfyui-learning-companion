---
key: 图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json
name: Boogu-Image 0.1 Turbo_2069099036728184834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json
hash: 9a0af111cc4b83bf
coverage: 0.9
learned_at: 2026-10-19 23:21:16
nodes: [ConditioningZeroOut, CLIPLoader, PreviewImage, UNETLoader, EmptyLatentImage, KSampler, VAELoader, VAEDecode, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 0, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（10 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `PreviewImage`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
