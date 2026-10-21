---
key: 图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json
name: Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json
hash: 15cab05547a956c0
coverage: 0.9
learned_at: 2026-10-19 22:45:50
nodes: [ConditioningZeroOut, UNETLoader, EmptyLatentImage, VAELoader, CR Prompt Text, CLIPTextEncode, CLIPTextEncode, easy seed, CLIPLoader, VAEDecode, PreviewImage, VAEDecode, PreviewImage, ImageConcanate, SaveImage, AddLabel, AddLabel, CLIPLoaderGGUF, KSampler, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 619460148253726, "steps": 10, "width": 1920}
---

# 图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy seed`
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageConcanate`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `CLIPLoaderGGUF`
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `619460148253726`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`EmptyLatentImage`、`VAELoader`、`CR Prompt Text`、`CLIPTextEncode`、`easy seed`、`CLIPLoader`、`VAEDecode`、`ImageConcanate`、`SaveImage`、`AddLabel`、`CLIPLoaderGGUF`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
