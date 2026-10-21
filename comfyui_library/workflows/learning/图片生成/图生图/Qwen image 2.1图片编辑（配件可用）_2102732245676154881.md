---
key: 图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json
name: Qwen image 2.1图片编辑（配件可用）_2102732245676154881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json
hash: eac355be9583f238
coverage: 0.75
learned_at: 2026-10-21 00:42:59
nodes: [VAELoader, CLIPLoader, QwenImage21Cache, KSampler, VAEDecode, easy showAnything, easy showAnything, LoadImage, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, UNETLoader, Image Comparer (rgthree), LoadImage, JjkText, LoadImage, SaveImage, QwenImage21PromptEnhancerT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 4449515722969, "steps": 50, "width": 2048}
---

# 图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `JjkText`
- `LoadImage`
- `SaveImage`
- `QwenImage21PromptEnhancerT8`

## 关键参数

- `seed` = `4449515722969`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`UNETLoader`、`SaveImage`、`QwenImage21PromptEnhancerT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
