---
key: 平台全量/FLUX.3D绘画场景生成及产品摄影_1899390554772295682.json
name: FLUX.3D绘画场景生成及产品摄影_1899390554772295682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.3D绘画场景生成及产品摄影_1899390554772295682.json
hash: 978215491ef33d40
coverage: 0.867925
learned_at: 2026-11-14 00:25:13
nodes: [VAEDecode, LayerUtility: ColorImage, ConditioningZeroOut, InpaintModelConditioning, ImageToMask, ImageConcanate, Replace Text _O, MaskToImage, ImageCrop+, PreviewImage, GetImageSize+, KSampler, PreviewImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, TextInput_, CLIPTextEncodeFlux, InpaintCrop, ImageConcanate, EmptyLatentImage, ConditioningZeroOut, CLIPTextEncodeFlux, LoraLoaderModelOnly, VAEDecode, DualCLIPLoader, VAELoader, UNETLoader, KSampler, SaveImage, PreviewImage, LoadImage, LoadImage, Joy_caption_two_load, ShowText|pysssss, GetImageSize+, Fast Groups Muter (rgthree), Joy_caption_two, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, VAELoader, StyleModelLoader, CLIPVisionLoader, ReduxAdvanced, SUPIR_Upscale, SaveImage, InpaintStitch, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "normal", "seed": 124516963193271, "steps": 25, "width": 1440}
---

# 平台全量/FLUX.3D绘画场景生成及产品摄影_1899390554772295682.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.3D绘画场景生成及产品摄影_1899390554772295682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `VAEDecode` ★核心
- `LayerUtility: ColorImage`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `ImageToMask`
- `ImageConcanate`
- `Replace Text _O`
- `MaskToImage`
- `ImageCrop+`
- `PreviewImage`
- `GetImageSize+`
- `KSampler` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `TextInput_`
- `CLIPTextEncodeFlux` ★核心
- `InpaintCrop`
- `ImageConcanate`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncodeFlux` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `Joy_caption_two_load`
- `ShowText|pysssss`
- `GetImageSize+`
- `Fast Groups Muter (rgthree)`
- `Joy_caption_two`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `SUPIR_Upscale`
- `SaveImage`
- `InpaintStitch`
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `124516963193271`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（46/53）

**有卡**：`VAEDecode`、`LayerUtility: ColorImage`、`ConditioningZeroOut`、`InpaintModelConditioning`、`ImageToMask`、`ImageConcanate`、`Replace Text _O`、`MaskToImage`、`ImageCrop+`、`GetImageSize+`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`InspyrenetRembg`、`LayerUtility: ImageRemoveAlpha`、`TextInput_`、`CLIPTextEncodeFlux`、`InpaintCrop`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`、`LoadImage`、`Joy_caption_two_load`、`Joy_caption_two`、`StyleModelLoader`、`CLIPVisionLoader`、`ReduxAdvanced`、`SUPIR_Upscale`、`InpaintStitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
