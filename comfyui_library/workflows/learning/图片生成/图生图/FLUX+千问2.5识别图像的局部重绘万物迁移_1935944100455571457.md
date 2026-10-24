---
key: 图片生成/图生图/FLUX+千问2.5识别图像的局部重绘万物迁移_1935944100455571457.json
name: FLUX+千问2.5识别图像的局部重绘万物迁移_1935944100455571457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX+千问2.5识别图像的局部重绘万物迁移_1935944100455571457.json
hash: 02265758fb046b19
coverage: 0.795918
learned_at: 2026-10-23 10:53:42
nodes: [VAELoader, DualCLIPLoader, CLIPVisionLoader, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, DifferentialDiffusion, StyleModelLoader, FluxGuidance, KSampler, VAEDecode, CLIPTextEncode, PreviewImage, PreviewImage, ImageCrop+, ReduxAdvanced, PreviewImage, easy makeImageForICLora, Image Comparer (rgthree), InpaintModelConditioning, MaskToImage, QwenVLDetection, PreviewImage, InpaintStitch, SaveImage, LayerMask: SegmentAnythingUltra V2, ArgosTranslateTextNode, InpaintCrop, MaskPreview+, PreviewImage, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage, LayerMask: LoadSAM2Model, BBoxesToSAM2, CR Prompt Text, easy showAnything, PreviewImage, LayerUtility: PurgeVRAM, DownloadAndLoadQwenModel, PreviewImage, MaskPreview+, PreviewImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: SAM2UltraV2, LayerUtility: CropByMask V2, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 875137528324116, "steps": 30}
---

# 图片生成/图生图/FLUX+千问2.5识别图像的局部重绘万物迁移_1935944100455571457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX+千问2.5识别图像的局部重绘万物迁移_1935944100455571457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAELoader`
- `DualCLIPLoader`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `StyleModelLoader`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `ImageCrop+`
- `ReduxAdvanced`
- `PreviewImage`
- `easy makeImageForICLora`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `MaskToImage`
- `QwenVLDetection`
- `PreviewImage`
- `InpaintStitch`
- `SaveImage`
- `LayerMask: SegmentAnythingUltra V2`
- `ArgosTranslateTextNode`
- `InpaintCrop`
- `MaskPreview+`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`
- `LayerMask: LoadSAM2Model`
- `BBoxesToSAM2`
- `CR Prompt Text`
- `easy showAnything`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadQwenModel`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: CropByMask V2`
- `LoadImage`

## 关键参数

- `seed` = `875137528324116`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **80%**（39/49）

**有卡**：`VAELoader`、`DualCLIPLoader`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`UNETLoader`、`DifferentialDiffusion`、`StyleModelLoader`、`FluxGuidance`、`KSampler`、`VAEDecode`、`ImageCrop+`、`ReduxAdvanced`、`easy makeImageForICLora`、`InpaintModelConditioning`、`MaskToImage`、`QwenVLDetection`、`InpaintStitch`、`SaveImage`、`LayerMask: SegmentAnythingUltra V2`、`ArgosTranslateTextNode`、`InpaintCrop`、`MaskPreview+`、`LayerUtility: ImageRemoveAlpha`、`LoadImage`、`LayerMask: LoadSAM2Model`、`BBoxesToSAM2`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`DownloadAndLoadQwenModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: SAM2UltraV2`、`LayerUtility: CropByMask V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
