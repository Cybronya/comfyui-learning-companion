---
key: 图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json
name: itools prompt styler x alekpet翻译_1975588560873066498
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json
hash: 21669c9dc954ff51
coverage: 0.9
learned_at: 2026-10-10 20:59:21
nodes: [SaveImage, VAEDecode, KSampler, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, CheckpointLoaderSimple, easy showAnything, GoogleTranslateTextNode, iToolsPromptStyler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 12, "checkpoint": "juggernautXL_v9Rundiffusionphoto2.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1068272135587956, "steps": 30, "width": 1024}
---

# 图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json`

## 结构

**节点**（10 个）：
- `SaveImage`
- `VAEDecode`
- `KSampler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `easy showAnything`
- `GoogleTranslateTextNode`
- `iToolsPromptStyler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `12`
- `checkpoint` = `juggernautXL_v9Rundiffusionphoto2.safetensors`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `seed` = `1068272135587956`
- `steps` = `30`
- `width` = `1024`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`easy showAnything`、`GoogleTranslateTextNode`
