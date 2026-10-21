---
key: 图片生成/图生图/Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050.json
name: Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050.json
hash: fddf2bfe13e93b35
coverage: 0.422222
learned_at: 2026-10-21 00:43:13
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPLoader, SetNode, ImageScaleToTotalPixels, MarkdownNote, GetNode, GetNode, SetNode, GetNode, GetNode, Any Switch (rgthree), GetNode, GetNode, KSampler, VAEDecode, TextEncodeQwenImage21, easy imageSizeByLongerSide, GetNode, SetNode, PrimitiveFloat, LoadImage, SaveImage, PreviewImage, GetNode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, DapaoImagePadDirectionNode, TextGenerateLTX2Prompt, RHHiddenNodes, QwenImage21Cache, Any Switch (rgthree), GetNode, GetNode, GetNode, Image Comparer (rgthree), SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SetNode, GetNode, SetNode, GetNode, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 9988438819167, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SetNode`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `easy imageSizeByLongerSide`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `DapaoImagePadDirectionNode`
- `TextGenerateLTX2Prompt`
- `RHHiddenNodes`
- `QwenImage21Cache`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `9988438819167`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（19/45）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`easy imageSizeByLongerSide`、`LoadImage`、`SaveImage`、`DapaoImagePadDirectionNode`、`TextGenerateLTX2Prompt`、`RHHiddenNodes`、`QwenImage21Cache`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
