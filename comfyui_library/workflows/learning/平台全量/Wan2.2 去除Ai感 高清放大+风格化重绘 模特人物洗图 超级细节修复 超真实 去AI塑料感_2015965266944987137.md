---
key: 平台全量/Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137.json
name: Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137.json
hash: 1d07e2a80ff908af
coverage: 0.826087
learned_at: 2026-11-14 01:05:42
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, CLIPTextEncode, CLIPTextEncode, VAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ConstrainImage|pysssss, CLIPLoader, VAEDecode, Joy_caption_two, Joy_caption_two_load, SaveImage, LoadImage, Image Comparer (rgthree), Anything Everywhere3, VAELoader, Joy_caption_two_load, KSampler, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 22662960157876, "steps": 20}
---

# 平台全量/Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConstrainImage|pysssss`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Joy_caption_two`
- `Joy_caption_two_load`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `VAELoader`
- `Joy_caption_two_load`
- `KSampler` ★核心
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `22662960157876`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`ConstrainImage|pysssss`、`CLIPLoader`、`VAEDecode`、`Joy_caption_two`、`Joy_caption_two_load`、`SaveImage`、`LoadImage`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
