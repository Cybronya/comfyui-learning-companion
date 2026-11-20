---
key: 平台全量/ControlNet通用-Flex.2-preview_1917163629534449665.json
name: ControlNet通用-Flex.2-preview_1917163629534449665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ControlNet通用-Flex.2-preview_1917163629534449665.json
hash: 15ba02227f4aa9a0
coverage: 0.923077
learned_at: 2026-11-14 00:22:56
nodes: [CLIPTextEncode, Flex2Conditioner, UNETLoader, VAELoader, DualCLIPLoader, VAEDecode, CLIPTextEncode, UNETLoader, VAELoader, DualCLIPLoader, ImageScaleToTotalPixels, VAEDecode, CLIPTextEncode, UNETLoader, VAELoader, DualCLIPLoader, KSampler, VAEDecode, DepthAnythingPreprocessor, CLIPTextEncode, Flex2Conditioner, AIO_Preprocessor, KSampler, AIO_Preprocessor, ImageScaleToTotalPixels, CLIPTextEncode, Flex2Conditioner, CLIPTextEncode, ImageScaleToTotalPixels, KSampler, SaveImage, SaveImage, SaveImage, PreviewImage, PreviewImage, PreviewImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 4736601899011, "steps": 25}
---

# 平台全量/ControlNet通用-Flex.2-preview_1917163629534449665.json

> 来源文件 `comfyui_library/workflows/平台全量/ControlNet通用-Flex.2-preview_1917163629534449665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPTextEncode` ★核心
- `Flex2Conditioner`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `DepthAnythingPreprocessor`
- `CLIPTextEncode` ★核心
- `Flex2Conditioner`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `Flex2Conditioner`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `4736601899011`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`CLIPTextEncode`、`Flex2Conditioner`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`VAEDecode`、`ImageScaleToTotalPixels`、`KSampler`、`DepthAnythingPreprocessor`、`AIO_Preprocessor`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、DepthAnythingPreprocessor、SaveImage
