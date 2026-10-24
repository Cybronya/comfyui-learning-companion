---
key: 图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json
name: 千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json
hash: c1aa758f54be303a
coverage: 0.944444
learned_at: 2026-10-23 12:31:20
nodes: [CLIPLoader, UNETLoader, SaveImage, SaveImage, VAEDecode, ImageStitch, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, CLIPTextEncode, ModelPatchLoader, QwenImageDiffsynthControlnet, PreviewImage, ImageAndMaskPreview, LoadImage, VAELoader, VAEEncode, Text Multiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1050072684993636, "steps": 20}
---

# 图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问局部重绘Inpaint控制-QWen-Image-ComfyUI官方_1958745627586879490.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageStitch`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `PreviewImage`
- `ImageAndMaskPreview`
- `LoadImage`
- `VAELoader`
- `VAEEncode` ★核心
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1050072684993636`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`UNETLoader`、`SaveImage`、`VAEDecode`、`ImageStitch`、`ModelSamplingAuraFlow`、`KSampler`、`CLIPTextEncode`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`ImageAndMaskPreview`、`LoadImage`、`VAELoader`、`VAEEncode`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet
