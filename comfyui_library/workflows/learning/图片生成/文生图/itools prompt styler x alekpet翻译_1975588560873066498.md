---
key: 图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json
name: itools prompt styler x alekpet翻译_1975588560873066498.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json
hash: 21669c9dc954ff51
coverage: 0.9
learned_at: 2026-10-09 19:50:53
nodes: [SaveImage, VAEDecode, KSampler, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, CheckpointLoaderSimple, easy showAnything, GoogleTranslateTextNode, iToolsPromptStyler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 12, "checkpoint": "juggernautXL_v9Rundiffusionphoto2.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1068272135587956, "steps": 30, "width": 1024}
---

# 图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1975588560873066498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `easy showAnything`
- `GoogleTranslateTextNode`
- `iToolsPromptStyler`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1068272135587956`
- `steps` = `30`
- `cfg` = `12`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `juggernautXL_v9Rundiffusionphoto2.safetensors`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`GoogleTranslateTextNode`、`iToolsPromptStyler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、iToolsPromptStyler、SaveImage、GoogleTranslateTextNode
