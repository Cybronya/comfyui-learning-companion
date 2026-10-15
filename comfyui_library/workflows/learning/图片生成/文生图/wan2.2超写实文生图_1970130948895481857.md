---
key: 图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json
name: wan2.2超写实文生图_1970130948895481857
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json
hash: 60cea33b7befb1ca
coverage: 0.9
learned_at: 2026-10-10 20:59:27
nodes: [LayerUtility: PurgeVRAM, EmptyLatentImage, LoraLoaderModelOnly, PathchSageAttentionKJ, CheckpointLoaderSimple, CLIPTextEncode, KSampler, VAEDecode, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: [LayerUtility: PurgeVRAM]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": 1, "height": 1280, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 739786914323188, "steps": 10, "width": 1280}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json`

## 结构

**节点**（10 个）：
- `LayerUtility: PurgeVRAM`
- `EmptyLatentImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple`
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `CLIPTextEncode`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`
- `denoise` = `1`
- `height` = `1280`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `seed` = `739786914323188`
- `steps` = `10`
- `width` = `1280`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`LayerUtility: PurgeVRAM`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`LayerUtility: PurgeVRAM`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
