---
key: wan2.2高阶文生图_1950437362914516993.json
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

# wan2.2高阶文生图_1950437362914516993.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2高阶文生图_1950437362914516993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `43037087897890`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`RH_Translator`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`UNETLoader`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
