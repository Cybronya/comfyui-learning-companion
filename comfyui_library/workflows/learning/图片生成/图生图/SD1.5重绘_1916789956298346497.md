---
key: 图片生成/图生图/SD1.5重绘_1916789956298346497.json
name: SD1.5重绘_1916789956298346497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5重绘_1916789956298346497.json
hash: 55dd3d27ee0ad5a3
coverage: 0.791667
learned_at: 2026-10-23 11:23:42
nodes: [PreviewImage, InvertMask (segment anything), MaskToImage, InpaintPreprocessor, AIO_Preprocessor, PreviewImage, VAEEncodeForInpaint, PreviewImage, SAM2ModelLoader (segment anything2), GroundingDinoModelLoader (segment anything2), GroundingDinoSAM2Segment (segment anything2), CR Multi-ControlNet Stack, KSampler (Efficient), SaveImage, VAEEncode, ImageUpscaleWithModel, ImageScaleBy, KSampler (Efficient), LoadImage, ImageConcanate, Efficient Loader, UpscaleModelLoader, PreviewImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1082987700242900, "steps": 30}
---

# 图片生成/图生图/SD1.5重绘_1916789956298346497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5重绘_1916789956298346497.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Process → Output → Other

**节点**（24 个）：
- `PreviewImage`
- `InvertMask (segment anything)`
- `MaskToImage`
- `InpaintPreprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEEncodeForInpaint` ★核心
- `PreviewImage`
- `SAM2ModelLoader (segment anything2)`
- `GroundingDinoModelLoader (segment anything2)`
- `GroundingDinoSAM2Segment (segment anything2)`
- `CR Multi-ControlNet Stack`
- `KSampler (Efficient)` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `KSampler (Efficient)` ★核心
- `LoadImage`
- `ImageConcanate`
- `Efficient Loader`
- `UpscaleModelLoader`
- `PreviewImage`
- `PreviewImage`

## 关键参数

- `seed` = `1082987700242900`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`InvertMask (segment anything)`、`MaskToImage`、`InpaintPreprocessor`、`AIO_Preprocessor`、`VAEEncodeForInpaint`、`SAM2ModelLoader (segment anything2)`、`GroundingDinoModelLoader (segment anything2)`、`GroundingDinoSAM2Segment (segment anything2)`、`CR Multi-ControlNet Stack`、`KSampler (Efficient)`、`SaveImage`、`VAEEncode`、`ImageUpscaleWithModel`、`ImageScaleBy`、`LoadImage`、`ImageConcanate`、`Efficient Loader`、`UpscaleModelLoader`

**用到的条目**：LoadImage、CR Multi-ControlNet Stack、KSampler (Efficient)、VAEEncode、VAEEncodeForInpaint、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader
