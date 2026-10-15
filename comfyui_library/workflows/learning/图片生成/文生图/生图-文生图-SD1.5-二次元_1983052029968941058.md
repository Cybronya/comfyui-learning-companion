---
key: 图片生成/文生图/生图-文生图-SD1.5-二次元_1983052029968941058.json
name: 生图-文生图-SD1.5-二次元_1983052029968941058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图-文生图-SD1.5-二次元_1983052029968941058.json
hash: bc624ed090fb6a18
coverage: 0.777778
learned_at: 2026-10-15 22:28:58
nodes: [VAEDecode, Reroute, Reroute, CLIPTextEncode, Reroute, Lora Loader Stack (rgthree), Reroute, KSampler, SaveImage, CLIPTextEncode, easy int, StringFunction|pysssss, easy seed, EmptyLatentImage, easy int, easy int, CheckpointLoaderSimple, easy positive]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "Colorful Anime Kawa 彩璃二次元 _v3.0.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "karras", "seed": 894900997266870, "steps": 20, "width": 768}
---

# 图片生成/文生图/生图-文生图-SD1.5-二次元_1983052029968941058.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/生图-文生图-SD1.5-二次元_1983052029968941058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Lora Loader Stack (rgthree)`
- `Reroute`
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `easy int`
- `StringFunction|pysssss`
- `easy seed`
- `EmptyLatentImage` ★核心
- `easy int`
- `easy int`
- `CheckpointLoaderSimple` ★核心
- `easy positive`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `894900997266870`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `768`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `Colorful Anime Kawa 彩璃二次元 _v3.0.safetensors`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`Lora Loader Stack (rgthree)`、`KSampler`、`SaveImage`、`easy int`、`StringFunction|pysssss`、`easy seed`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`easy positive`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、easy seed、Lora Loader Stack (rgthree)、SaveImage
