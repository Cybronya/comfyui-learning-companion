---
key: 图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json
name: Anima Base any-test-like控制生图_2073323335081095169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json
hash: cd0af45d167d7b59
coverage: 1
learned_at: 2026-10-20 00:01:03
nodes: [VAELoader, CLIPLoader, LoadImage, UNETLoader, EmptyLatentImage, VAEDecode, KSampler, CLIPTextEncode, CLIPTextEncode, AnimaLLLiteApply, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 42, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AnimaLLLiteApply`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAELoader`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`AnimaLLLiteApply`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
