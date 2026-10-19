---
key: 图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json
name: Magic-Wan2.2-V2文生图工作流_1993696801660354561
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json
hash: 3880905d38087ccf
coverage: 1
learned_at: 2026-10-19 21:32:37
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, VAELoader, CLIPTextEncode, SaveImage, UNETLoader, LoraLoaderModelOnly, KSampler, EmptyLatentImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta", "seed": 18359506268823, "steps": 6, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `18359506268823`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
