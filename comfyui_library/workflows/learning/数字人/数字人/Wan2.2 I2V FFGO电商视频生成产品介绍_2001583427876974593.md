---
key: 数字人/数字人/Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593.json
name: Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593.json
hash: 8b79d8e614234f54
coverage: 0.530303
learned_at: 2026-10-26 01:57:53
nodes: [SetNode, SetNode, CLIPLoader, GetNode, ModelSamplingSD3, GetNode, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, WanVideoNAG, CLIPTextEncode, VAELoader, ModelSamplingSD3, GetNode, UNETLoader, RMBG, GetImageRangeFromBatch, ImageResizeKJv2, SetNode, PreviewImage, CLIPVisionLoader, UNETLoader, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, RMBG, CFGZeroStar, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, KSamplerAdvanced, SetNode, ImageStitch, ImageStitch, SetNode, LoadImage, LoadImage, LoadImage, KSamplerAdvanced, VHS_VideoCombine, SimpleMath+, PrimitiveInt, CLIPTextEncode, PrimitiveStringMultiline, CR SDXL Aspect Ratio, TrimVideoLatent, PainterI2V, PrimitiveFloat]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 数字人/数字人/Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `GetNode`
- `UNETLoader` ★核心
- `RMBG`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `RMBG`
- `CFGZeroStar`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `ImageStitch`
- `ImageStitch`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `CR SDXL Aspect Ratio`
- `TrimVideoLatent`
- `PainterI2V`
- `PrimitiveFloat`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **53%**（35/66）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`VAEDecode`、`WanVideoNAG`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`RMBG`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`CFGZeroStar`、`PathchSageAttentionKJ`、`CLIPVisionEncode`、`KSamplerAdvanced`、`ImageStitch`、`LoadImage`、`VHS_VideoCombine`、`SimpleMath+`、`CR SDXL Aspect Ratio`、`TrimVideoLatent`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced
