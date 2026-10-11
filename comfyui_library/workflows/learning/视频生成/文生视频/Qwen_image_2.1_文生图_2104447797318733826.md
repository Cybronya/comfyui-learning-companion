---
key: 视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json
name: Qwen_image_2.1_文生图_2104447797318733826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json
hash: a5f6338f55f9b647
coverage: 0.866667
learned_at: 2026-10-11 22:12:46
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, easy showAnything, SaveImageAdvanced, ResolutionSelector, SaveImage, TextGenerateLTX2Prompt, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImageAdvanced`、`ResolutionSelector`、`SaveImage`、`TextGenerateLTX2Prompt`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
