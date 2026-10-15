---
key: 图片生成/文生图/Flux.1Krea文生图_1951794471434399745.json
name: Flux.1Krea文生图_1951794471434399745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1Krea文生图_1951794471434399745.json
hash: 5a3d181e8f1592ac
coverage: 1
learned_at: 2026-10-10 20:58:36
nodes: [SaveImage, CLIPTextEncode, ConditioningZeroOut, VAELoader, DualCLIPLoader, KSampler, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, VAEDecode, RH_Translator]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 294507246359010, "steps": 20, "width": 1024}
---

# 图片生成/文生图/Flux.1Krea文生图_1951794471434399745.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1Krea文生图_1951794471434399745.json`

## 结构

**节点**（11 个）：
- `SaveImage`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `VAELoader`
- `DualCLIPLoader`
- `KSampler`
- `EmptyLatentImage`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `RH_Translator`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1536`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `294507246359010`
- `steps` = `20`
- `width` = `1024`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`DualCLIPLoader`、`KSampler`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`RH_Translator`
