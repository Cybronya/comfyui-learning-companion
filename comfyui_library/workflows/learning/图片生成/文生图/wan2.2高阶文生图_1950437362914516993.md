---
key: 图片生成/文生图/wan2.2高阶文生图_1950437362914516993.json
name: wan2.2高阶文生图_1950437362914516993
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2高阶文生图_1950437362914516993.json
hash: bfbbea31e839842a
coverage: 0.866667
learned_at: 2026-10-10 20:59:27
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, KSampler, LoraLoaderModelOnly, RH_Translator, LoraLoaderModelOnly, VAEDecode, SaveImage, ShowText|pysssss, EmptyLatentImage, UNETLoader]
patterns: [text_to_image]
missing: [easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "beta", "seed": 43037087897890, "steps": 15, "width": 1080}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2高阶文生图_1950437362914516993.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2高阶文生图_1950437362914516993.json`

## 结构

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `easy cleanGpuUsed`
- `KSampler`
- `LoraLoaderModelOnly`
- `RH_Translator`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `SaveImage`
- `ShowText|pysssss`
- `EmptyLatentImage`
- `UNETLoader`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1920`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `43037087897890`
- `steps` = `15`
- `width` = `1080`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`easy cleanGpuUsed`、`KSampler`、`LoraLoaderModelOnly`、`RH_Translator`、`VAEDecode`、`SaveImage`、`ShowText|pysssss`

**缺卡**（1）：`easy cleanGpuUsed`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
