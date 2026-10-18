---
key: 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json
name: Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json
hash: c36a5b99221db3e2
coverage: 0.809524
learned_at: 2026-10-17 22:18:56
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, QwenImage21Cache, UNETLoader, VAELoader, SaveImage, ResolutionSelector, LoadImage, TextEncodeQwenImage21, Text Multiline, TextCombinerSix, PreviewAny, KSampler, TextGenerateLTX2Prompt, JjkText, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 641027526640711, "steps": 50, "width": 1024}
---

# 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `ResolutionSelector`
- `LoadImage`
- `TextEncodeQwenImage21`
- `Text Multiline`
- `TextCombinerSix`
- `PreviewAny`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `JjkText`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `641027526640711`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`TextEncodeQwenImage21`、`Text Multiline`、`TextCombinerSix`、`KSampler`、`TextGenerateLTX2Prompt`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
