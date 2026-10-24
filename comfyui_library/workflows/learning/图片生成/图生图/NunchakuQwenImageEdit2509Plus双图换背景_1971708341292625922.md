---
key: 图片生成/图生图/NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922.json
name: NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922.json
hash: c6e9afd5fb39be71
coverage: 1
learned_at: 2026-10-23 11:10:04
nodes: [EmptySD3LatentImage, TextEncodeQwenImageEditPlus, KSampler, NunchakuQwenImageDiTLoader, CLIPLoader, GetImageSize, ImageScaleToTotalPixels, VAELoader, ImageScaleToTotalPixels, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, CFGNorm, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 671, "steps": 50}
---

# 图片生成/图生图/NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `671`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlus`、`KSampler`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`GetImageSize`、`ImageScaleToTotalPixels`、`VAELoader`、`LoadImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEditPlus、EmptySD3LatentImage
