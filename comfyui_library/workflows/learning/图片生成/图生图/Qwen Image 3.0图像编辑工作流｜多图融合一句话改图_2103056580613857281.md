---
key: 图片生成/图生图/Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281.json
name: Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281.json
hash: 6dfb29984acf4e90
coverage: 0.857143
learned_at: 2026-10-10 20:48:08
nodes: [LoadImage, LoadImage, SaveImage, Note, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, KSampler, VAEDecode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 24}
---

# 图片生成/图生图/Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `Note`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `42`
- `steps` = `24`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`LoadImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`VAEEncode`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus
