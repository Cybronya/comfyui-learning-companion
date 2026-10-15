---
key: 图片生成/文生图/SD1.5使用wildcard随机更换画面元素_1955202232166727682.json
name: SD1.5使用wildcard随机更换画面元素_1955202232166727682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5使用wildcard随机更换画面元素_1955202232166727682.json
hash: 6755735e75c41c0f
coverage: 0.9
learned_at: 2026-10-10 20:59:10
nodes: [KSampler, CheckpointLoaderSimple, LoraLoader, VAEDecode, easy cleanGpuUsed, ImpactWildcardProcessor, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, SaveImage]
patterns: [text_to_image, lora]
missing: [easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "SD1.5 dreamshaper_8.safetensors", "denoise": 1, "height": 768, "lora_name": "YUNY_繁花素雪_v1.1.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 935649230133986, "steps": 20, "strength_clip": 0.8000000000000002, "strength_model": 0.30000000000000004, "width": 512}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/SD1.5使用wildcard随机更换画面元素_1955202232166727682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5使用wildcard随机更换画面元素_1955202232166727682.json`

## 结构

**节点**（10 个）：
- `KSampler`
- `CheckpointLoaderSimple`
- `LoraLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `ImpactWildcardProcessor`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `SaveImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `batch_size` = `1`
- `cfg` = `8`
- `checkpoint` = `SD1.5 dreamshaper_8.safetensors`
- `denoise` = `1`
- `height` = `768`
- `lora_name` = `YUNY_繁花素雪_v1.1.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `935649230133986`
- `steps` = `20`
- `strength_clip` = `0.8000000000000002`
- `strength_model` = `0.30000000000000004`
- `width` = `512`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`KSampler`、`CheckpointLoaderSimple`、`LoraLoader`、`VAEDecode`、`easy cleanGpuUsed`、`ImpactWildcardProcessor`、`CLIPTextEncode`、`EmptyLatentImage`

**缺卡**（1）：`easy cleanGpuUsed`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
