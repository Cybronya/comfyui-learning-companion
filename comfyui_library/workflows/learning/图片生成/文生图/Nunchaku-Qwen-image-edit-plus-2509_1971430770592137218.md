---
key: Nunchaku-Qwen-image-edit-plus-2509_1971430770592137218.json
name: Nunchaku-Qwen-image-edit-plus-2509_1971430770592137218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku-Qwen-image-edit-plus-2509_1971430770592137218.json
hash: 2bfa9169cac11b7f
coverage: 0.888889
learned_at: 2026-10-10 20:58:48
nodes: [LoadImage, CLIPLoader, VAELoader, LoadImage, TextEncodeQwenImageEditPlus, NunchakuQwenImageDiTLoader, KSampler, LoadImage, ModelSamplingAuraFlow, CFGNorm, EmptySD3LatentImage, ImageScaleToTotalPixels, DWPreprocessor, GetImageSize, LoadImage, SaveImage, VAEDecode, ImageScaleToTotalPixels, ImageStitch, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Reroute, PreviewImage, SaveImage, ImageStitch, TextEncodeQwenImageEditPlus, JjkText]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 671, "steps": 50}
---

# Nunchaku-Qwen-image-edit-plus-2509_1971430770592137218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku-Qwen-image-edit-plus-2509_1971430770592137218.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `NunchakuQwenImageDiTLoader`
- `KSampler` ★核心
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `DWPreprocessor`
- `GetImageSize`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Reroute`
- `PreviewImage`
- `SaveImage`
- `ImageStitch`
- `TextEncodeQwenImageEditPlus`
- `JjkText`

## 关键参数

- `seed` = `671`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`NunchakuQwenImageDiTLoader`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`EmptySD3LatentImage`、`ImageScaleToTotalPixels`、`DWPreprocessor`、`GetImageSize`、`SaveImage`、`VAEDecode`、`ImageStitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEditPlus、EmptySD3LatentImage
