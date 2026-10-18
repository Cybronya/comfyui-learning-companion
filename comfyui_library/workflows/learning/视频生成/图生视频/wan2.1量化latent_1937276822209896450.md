---
key: 视频生成/图生视频/wan2.1量化latent_1937276822209896450.json
name: wan2.1量化latent_1937276822209896450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1量化latent_1937276822209896450.json
hash: c6b7aab4222ad717
coverage: 1
learned_at: 2026-10-15 22:30:28
nodes: [CLIPVisionEncode, CLIPVisionLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, UnetLoaderGGUF, LoadImage, KSampler, VAELoader, WanImageToVideo, SaveLatent, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 883005815599328, "steps": 25}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.1量化latent_1937276822209896450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937276822209896450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Output → Other

**节点**（13 个）：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `WanImageToVideo`
- `SaveLatent`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `883005815599328`
- `steps` = `25`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPLoader`、`CLIPTextEncode`、`UnetLoaderGGUF`、`LoadImage`、`KSampler`、`VAELoader`、`WanImageToVideo`、`SaveLatent`、`SaveImage`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、SaveLatent、CLIPVisionEncode、CLIPVisionLoader

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
