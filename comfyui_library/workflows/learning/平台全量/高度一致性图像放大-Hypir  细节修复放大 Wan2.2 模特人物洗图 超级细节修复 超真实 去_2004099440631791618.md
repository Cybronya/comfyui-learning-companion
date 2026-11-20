---
key: 平台全量/高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618.json
name: 高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618.json
hash: 151cb70260ded549
coverage: 0.857143
learned_at: 2026-11-14 02:51:35
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, CLIPTextEncode, VAEEncode, CLIPTextEncode, Joy_caption_two, ConstrainImage|pysssss, VAEDecode, SaveImage, Image Comparer (rgthree), KSampler, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Anything Everywhere3, Joy_caption_two_load, VAELoader, CLIPLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.2, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 420388973281832, "steps": 20}
---

# 平台全量/高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618.json

> 来源文件 `comfyui_library/workflows/平台全量/高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Joy_caption_two`
- `ConstrainImage|pysssss`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `Joy_caption_two_load`
- `VAELoader`
- `CLIPLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `420388973281832`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.2`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEEncode`、`Joy_caption_two`、`ConstrainImage|pysssss`、`VAEDecode`、`SaveImage`、`KSampler`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`Joy_caption_two_load`、`VAELoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
