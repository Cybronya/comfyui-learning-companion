---
key: 平台全量/老照片修复 Old Photo Restoration XL_1844779688131727362.json
name: 老照片修复 Old Photo Restoration XL_1844779688131727362
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/老照片修复 Old Photo Restoration XL_1844779688131727362.json
hash: 5f2bc5e04a5bc669
coverage: 0.755556
learned_at: 2026-11-14 02:29:57
nodes: [CLIPTextEncode, PreviewImage, VAEEncode, CLIPTextEncode, Automatic CFG, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetApplyAdvanced, DepthAnythingV2Preprocessor, Florence2Run, DisplayText_Zho, DownloadAndLoadFlorence2Model, ControlNetLoader, ControlNetLoader, ControlNetLoader, ImageScaleToMegapixels, PreviewImage, KSampler, DWPreprocessor, PreviewImage, ComfyUI_Image_Round__ImageCropAdvanced, PreviewImage, CheckpointLoaderSimple, Reroute, workflow/Overlay, ReActorFaceSwap, LoadImage, SaveImage, PreviewImage, ComfyUI_Image_Round__ImageRoundAdvanced, BOPBTL_LoadScratchMaskModel, BOPBTL_LoadRestoreOldPhotosModel, ImageResizeKJ, PreviewImage, BOPBTL_RestoreOldPhotos, PreviewImage, PreviewImage, ImageToMask, BOPBTL_ScratchMask, MaskToImage, PreviewImage, easy cleanGpuUsed, ImageResizeKJ, PreviewImage, VAEDecode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.6, "denoise": 0.8, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 58060710795618, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/老照片修复 Old Photo Restoration XL_1844779688131727362.json

> 来源文件 `comfyui_library/workflows/平台全量/老照片修复 Old Photo Restoration XL_1844779688131727362.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Automatic CFG`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `DepthAnythingV2Preprocessor`
- `Florence2Run`
- `DisplayText_Zho`
- `DownloadAndLoadFlorence2Model`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ImageScaleToMegapixels`
- `PreviewImage`
- `KSampler` ★核心
- `DWPreprocessor`
- `PreviewImage`
- `ComfyUI_Image_Round__ImageCropAdvanced`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `workflow/Overlay`
- `ReActorFaceSwap`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `ComfyUI_Image_Round__ImageRoundAdvanced`
- `BOPBTL_LoadScratchMaskModel`
- `BOPBTL_LoadRestoreOldPhotosModel`
- `ImageResizeKJ`
- `PreviewImage`
- `BOPBTL_RestoreOldPhotos`
- `PreviewImage`
- `PreviewImage`
- `ImageToMask`
- `BOPBTL_ScratchMask`
- `MaskToImage`
- `PreviewImage`
- `easy cleanGpuUsed`
- `ImageResizeKJ`
- `PreviewImage`
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.6`
- `seed` = `58060710795618`
- `steps` = `6`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.8`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`Automatic CFG`、`ControlNetApplyAdvanced`、`DepthAnythingV2Preprocessor`、`Florence2Run`、`DisplayText_Zho`、`DownloadAndLoadFlorence2Model`、`ControlNetLoader`、`ImageScaleToMegapixels`、`KSampler`、`DWPreprocessor`、`ComfyUI_Image_Round__ImageCropAdvanced`、`CheckpointLoaderSimple`、`workflow/Overlay`、`ReActorFaceSwap`、`LoadImage`、`SaveImage`、`ComfyUI_Image_Round__ImageRoundAdvanced`、`BOPBTL_LoadScratchMaskModel`、`BOPBTL_LoadRestoreOldPhotosModel`、`ImageResizeKJ`、`BOPBTL_RestoreOldPhotos`、`ImageToMask`、`BOPBTL_ScratchMask`、`MaskToImage`、`easy cleanGpuUsed`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、DepthAnythingV2Preprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
