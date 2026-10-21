---
key: 图片生成/图生图/表情迁移 qwen_image_2.1_2105577290787807234.json
name: 表情迁移 qwen_image_2.1_2105577290787807234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/表情迁移 qwen_image_2.1_2105577290787807234.json
hash: efd73c3cae29b491
coverage: 0.75
learned_at: 2026-10-21 00:56:07
nodes: [LayerUtility: ColorImage V2, ImageToMask, LayerUtility: ImageBlendAdvance, MaskPreview, LayerMask: PersonMaskUltra V2, FaceAnalysisModels, CLIPLoader, VAELoader, LayerMask: PersonMaskUltra V2, PreviewImage, PreviewImage, FaceBoundingBox, GrowMaskWithBlur, MaskPreview, Reroute, VAEDecode, Image Comparer (rgthree), KSampler, SaveImage, UNETLoader, Int, LayerUtility: CropByMask V2, Image Overlay, LayerUtility: ColorImage V2, MathExpression|pysssss, easy showAnything, LayerUtility: CropByMask V2, PreviewImage, PreviewImage, TextEncodeQwenImage21, PreviewImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, JjkText, LayerUtility: RestoreCropBox, LayerMask: MaskGrow, GetImageSize, GetImageSize, PreviewImage, ImageScale, LoraLoaderModelOnly, QwenImage21Cache, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 180996334284821, "steps": 25}
---

# 图片生成/图生图/表情迁移 qwen_image_2.1_2105577290787807234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/表情迁移 qwen_image_2.1_2105577290787807234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LayerUtility: ColorImage V2`
- `ImageToMask`
- `LayerUtility: ImageBlendAdvance`
- `MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `FaceAnalysisModels`
- `CLIPLoader`
- `VAELoader`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `PreviewImage`
- `FaceBoundingBox`
- `GrowMaskWithBlur`
- `MaskPreview`
- `Reroute`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `Int`
- `LayerUtility: CropByMask V2`
- `Image Overlay`
- `LayerUtility: ColorImage V2`
- `MathExpression|pysssss`
- `easy showAnything`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JjkText`
- `LayerUtility: RestoreCropBox`
- `LayerMask: MaskGrow`
- `GetImageSize`
- `GetImageSize`
- `PreviewImage`
- `ImageScale`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `180996334284821`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（33/44）

**有卡**：`LayerUtility: ColorImage V2`、`ImageToMask`、`LayerUtility: ImageBlendAdvance`、`MaskPreview`、`LayerMask: PersonMaskUltra V2`、`FaceAnalysisModels`、`CLIPLoader`、`VAELoader`、`FaceBoundingBox`、`GrowMaskWithBlur`、`VAEDecode`、`KSampler`、`SaveImage`、`UNETLoader`、`Int`、`LayerUtility: CropByMask V2`、`Image Overlay`、`MathExpression|pysssss`、`TextEncodeQwenImage21`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: RestoreCropBox`、`LayerMask: MaskGrow`、`GetImageSize`、`ImageScale`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
