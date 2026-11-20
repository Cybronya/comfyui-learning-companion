---
key: 平台全量/Qwen-Image-Edit 懒人版一键OOTD 模特穿搭 V1.0_1965316887640985601.json
name: Qwen-Image-Edit 懒人版一键OOTD 模特穿搭 V1.0_1965316887640985601
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-Edit 懒人版一键OOTD 模特穿搭 V1.0_1965316887640985601.json
hash: e467ff08f0d231ae
coverage: 0.833333
learned_at: 2026-11-14 00:51:39
nodes: [CFGNorm, VAELoader, ImageScaleToTotalPixels, VAEEncode, MarkdownNote, CLIPLoader, TextEncodeQwenImageEdit, VAEDecode, Note, UNETLoader, easy imageConcat, SaveImage, KSampler, PreviewImage, LoraLoaderModelOnly, LoadImage, ModelSamplingAuraFlow, TextEncodeQwenImageEdit]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 490443708818284, "steps": 30}
---

# 平台全量/Qwen-Image-Edit 懒人版一键OOTD 模特穿搭 V1.0_1965316887640985601.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-Edit 懒人版一键OOTD 模特穿搭 V1.0_1965316887640985601.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CFGNorm`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `TextEncodeQwenImageEdit`
- `VAEDecode` ★核心
- `Note`
- `UNETLoader` ★核心
- `easy imageConcat`
- `SaveImage`
- `KSampler` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEdit`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `490443708818284`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CFGNorm`、`VAELoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`CLIPLoader`、`TextEncodeQwenImageEdit`、`VAEDecode`、`UNETLoader`、`easy imageConcat`、`SaveImage`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm
