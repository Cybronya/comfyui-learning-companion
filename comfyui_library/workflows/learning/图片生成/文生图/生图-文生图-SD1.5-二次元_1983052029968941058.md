---
key: 生图-文生图-SD1.5-二次元_1983052029968941058.json
name: 生图-文生图-SD1.5-二次元_1983052029968941058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图-文生图-SD1.5-二次元_1983052029968941058.json
hash: bc624ed090fb6a18
coverage: 0.388889
learned_at: 2026-10-10 20:59:53
nodes: [VAEDecode, Reroute, Reroute, CLIPTextEncode, Reroute, Lora Loader Stack (rgthree), Reroute, KSampler, SaveImage, CLIPTextEncode, easy int, StringFunction|pysssss, easy seed, EmptyLatentImage, easy int, easy int, CheckpointLoaderSimple, easy positive]
patterns: [text_to_image]
missing: [StringFunction|pysssss, easy int, easy int, easy int, easy positive, Lora Loader Stack (rgthree), easy seed]
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "Colorful Anime Kawa 彩璃二次元 _v3.0.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "karras", "seed": 894900997266870, "steps": 20, "width": 768}
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 生图-文生图-SD1.5-二次元_1983052029968941058.json

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

覆盖率 **39%**（7/18）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`CheckpointLoaderSimple`

**缺卡**（7）：`StringFunction|pysssss`、`easy int`、`easy int`、`easy int`、`easy positive`、`Lora Loader Stack (rgthree)`、`easy seed`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
