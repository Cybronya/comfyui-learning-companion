---
key: 图片生成/图生图/Flux_Fill+Redux_small_object_swap20250518_1924079817816199170.json
name: Flux_Fill+Redux_small_object_swap20250518_1924079817816199170
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux_Fill+Redux_small_object_swap20250518_1924079817816199170.json
hash: ced402341805622a
coverage: 0.852459
learned_at: 2026-10-23 11:01:43
nodes: [LayerMask: BiRefNetUltraV2, Reroute, Reroute, InpaintModelConditioning, CLIPTextEncode, easy imageSize, VAEEncode, ImpactImageBatchToImageList, VAEDecodeTiled, TTP_Tile_image_size, SetNode, SetNode, GrowMask, SaveImage, DualCLIPLoader, CLIPTextEncode, StyleModelLoader, CLIPVisionLoader, LayerUtility: ImageRemoveAlpha, LayerUtility: ColorImage V2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ReduxAdvanced, ModelSamplingFlux, VAEDecode, easy imageSplitGrid, ImageFromBatch+, FluxGuidance, TTP_Image_Tile_Batch, KSampler, KSampler, ImageListToImageBatch, CLIPTextEncode, CLIPTextEncode, GetNode, TTP_Image_Assy, ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageConcanate, ImageToMask, MaskToImage, MaskToImage, ImageToMask, ImageConcanate, PreviewImage, InpaintCrop, LayerMask: LoadFlorence2Model, LayerMask: Florence2Ultra, UNETLoader, VAELoader, LayerMask: LoadBiRefNetModelV2, LoadImage, LoadImage, LoraLoader|pysssss, CheckpointLoaderSimple, ImageUpscaleWithModel, UpscaleModelLoader, GetNode, InpaintStitch, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "denoise": 1, "lora_name": "None", "sampler_name": "euler", "scheduler": "simple", "seed": 1047159944444414, "steps": 20, "strength_clip": 1, "strength_model": 0.8}
---

# 图片生成/图生图/Flux_Fill+Redux_small_object_swap20250518_1924079817816199170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux_Fill+Redux_small_object_swap20250518_1924079817816199170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `LayerMask: BiRefNetUltraV2`
- `Reroute`
- `Reroute`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `VAEEncode` ★核心
- `ImpactImageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `TTP_Tile_image_size`
- `SetNode`
- `SetNode`
- `GrowMask`
- `SaveImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ColorImage V2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ReduxAdvanced`
- `ModelSamplingFlux`
- `VAEDecode` ★核心
- `easy imageSplitGrid`
- `ImageFromBatch+`
- `FluxGuidance`
- `TTP_Image_Tile_Batch`
- `KSampler` ★核心
- `KSampler` ★核心
- `ImageListToImageBatch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `TTP_Image_Assy`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageConcanate`
- `ImageToMask`
- `MaskToImage`
- `MaskToImage`
- `ImageToMask`
- `ImageConcanate`
- `PreviewImage`
- `InpaintCrop`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: Florence2Ultra`
- `UNETLoader` ★核心
- `VAELoader`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LoadImage`
- `LoraLoader|pysssss` ★核心
- `CheckpointLoaderSimple` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetNode`
- `InpaintStitch`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1047159944444414`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `None`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `checkpoint` = `flux1-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（52/61）

**有卡**：`LayerMask: BiRefNetUltraV2`、`InpaintModelConditioning`、`CLIPTextEncode`、`easy imageSize`、`VAEEncode`、`ImpactImageBatchToImageList`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`GrowMask`、`SaveImage`、`DualCLIPLoader`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ReduxAdvanced`、`ModelSamplingFlux`、`VAEDecode`、`easy imageSplitGrid`、`ImageFromBatch+`、`FluxGuidance`、`TTP_Image_Tile_Batch`、`KSampler`、`ImageListToImageBatch`、`TTP_Image_Assy`、`ImageScaleBy`、`ImageConcanate`、`ImageToMask`、`MaskToImage`、`InpaintCrop`、`LayerMask: LoadFlorence2Model`、`LayerMask: Florence2Ultra`、`UNETLoader`、`VAELoader`、`LayerMask: LoadBiRefNetModelV2`、`LoadImage`、`LoraLoader|pysssss`、`CheckpointLoaderSimple`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`InpaintStitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
