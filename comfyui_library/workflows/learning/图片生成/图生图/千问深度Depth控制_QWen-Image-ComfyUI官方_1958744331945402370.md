---
key: 图片生成/图生图/千问深度Depth控制_QWen-Image-ComfyUI官方_1958744331945402370.json
name: 千问深度Depth控制_QWen-Image-ComfyUI官方_1958744331945402370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问深度Depth控制_QWen-Image-ComfyUI官方_1958744331945402370.json
hash: f3f74a6d07fe2a82
coverage: 0.95
learned_at: 2026-10-23 12:31:38
nodes: [VAELoader, CLIPLoader, UNETLoader, SaveImage, SaveImage, VAEDecode, ImageStitch, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, CLIPTextEncode, QwenImageDiffsynthControlnet, EmptySD3LatentImage, GetImageSize, LoadImage, ImageScaleDownToSize, PreviewImage, Text Multiline, ModelPatchLoader, AIO_Preprocessor]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 27405536985927, "steps": 20}
---

# 图片生成/图生图/千问深度Depth控制_QWen-Image-ComfyUI官方_1958744331945402370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问深度Depth控制_QWen-Image-ComfyUI官方_1958744331945402370.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
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
- `QwenImageDiffsynthControlnet`
- `EmptySD3LatentImage`
- `GetImageSize`
- `LoadImage`
- `ImageScaleDownToSize`
- `PreviewImage`
- `Text Multiline`
- `ModelPatchLoader`
- `AIO_Preprocessor`

## 关键参数

- `seed` = `27405536985927`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`SaveImage`、`VAEDecode`、`ImageStitch`、`ModelSamplingAuraFlow`、`KSampler`、`CLIPTextEncode`、`QwenImageDiffsynthControlnet`、`EmptySD3LatentImage`、`GetImageSize`、`LoadImage`、`ImageScaleDownToSize`、`Text Multiline`、`ModelPatchLoader`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet
