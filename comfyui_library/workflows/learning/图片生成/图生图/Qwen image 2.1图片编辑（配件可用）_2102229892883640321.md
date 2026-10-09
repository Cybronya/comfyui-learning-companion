---
key: 图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json
name: Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json
hash: ba9625d0c0ef58ce
coverage: 0.727273
learned_at: 2026-10-09 22:19:27
nodes: [VAELoader, CLIPLoader, UNETLoader, QwenImage21Cache, KSampler, VAEDecode, Image Comparer (rgthree), easy showAnything, easy showAnything, LoadImage, LoadImage, LoadImage, LoadImage, JjkText, EmptyLatentImage, TextEncodeQwenImage21, JjkText, QwenImage21PromptEnhancerT8, SaveImage, ResolutionSelector, LoadImage, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 957178147004617, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102229892883640321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `JjkText`
- `QwenImage21PromptEnhancerT8`
- `SaveImage`
- `ResolutionSelector`
- `LoadImage`
- `ComfySwitchNode`

## 关键参数

- `seed` = `957178147004617`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`LoadImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`QwenImage21PromptEnhancerT8`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
