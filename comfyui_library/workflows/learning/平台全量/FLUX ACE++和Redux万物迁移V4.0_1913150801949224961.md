---
key: 平台全量/FLUX ACE++和Redux万物迁移V4.0_1913150801949224961.json
name: FLUX ACE++和Redux万物迁移V4.0_1913150801949224961
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX ACE++和Redux万物迁移V4.0_1913150801949224961.json
hash: 2e88e25c6ef91bd4
coverage: 0.7625
learned_at: 2026-11-14 00:24:31
nodes: [VAEDecode, FluxGuidance, ImageResize+, Florence2ModelLoader, ShowText|pysssss, Florence2Run, PreviewImage, easy imageSize, InpaintModelConditioning, ReduxAdvanced, VAEDecode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, LoadImage, Note, PreviewImage, EmptyImage, LayerMask: MaskPreview, PreviewImage, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageRemoveAlpha, LayerMask: MaskGrow, ImageToMask, ImageConcanate, PreviewImage, Image Comparer (rgthree), PreviewImage, CLIPTextEncode, TextInput_, PreviewImage, TextInput_, LayerUtility: TextJoin, CLIPTextEncode, PreviewImage, Reroute, Image Comparer (rgthree), Reroute, LayerUtility: CropByMask V2, ResizeMask, MaskToImage, ImageConcanate, PreviewImage, LayerMask: MaskPreview, LayerMask: MaskPreview, ImageResize+, LoraLoaderModelOnly, KSampler, Note, DifferentialDiffusion, Note, ImageMaskSwitch, ShowText|pysssss, ImageCrop, LayerMask: SegmentAnythingUltra V2, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, StyleModelLoader, CLIPVisionLoader, EmptyImage, ResizeMask, UNETLoader, InpaintCrop, VAEEncode, Reroute, LayerMask: MaskGrow, Reroute, ImageResize+, LayerMask: SegmentAnythingUltra V2, LayerUtility: RestoreCropBox, SaveImage, SaveImage, InpaintStitch, LoadImage, ImageResize+, LayerUtility: CropByMask V2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 180093038225841, "steps": 20}
---

# 平台全量/FLUX ACE++和Redux万物迁移V4.0_1913150801949224961.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX ACE++和Redux万物迁移V4.0_1913150801949224961.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `VAEDecode` ★核心
- `FluxGuidance`
- `ImageResize+`
- `Florence2ModelLoader`
- `ShowText|pysssss`
- `Florence2Run`
- `PreviewImage`
- `easy imageSize`
- `InpaintModelConditioning`
- `ReduxAdvanced`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `LoadImage`
- `Note`
- `PreviewImage`
- `EmptyImage`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageRemoveAlpha`
- `LayerMask: MaskGrow`
- `ImageToMask`
- `ImageConcanate`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `PreviewImage`
- `TextInput_`
- `LayerUtility: TextJoin`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `LayerUtility: CropByMask V2`
- `ResizeMask`
- `MaskToImage`
- `ImageConcanate`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Note`
- `DifferentialDiffusion`
- `Note`
- `ImageMaskSwitch`
- `ShowText|pysssss`
- `ImageCrop`
- `LayerMask: SegmentAnythingUltra V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `EmptyImage`
- `ResizeMask`
- `UNETLoader` ★核心
- `InpaintCrop`
- `VAEEncode` ★核心
- `Reroute`
- `LayerMask: MaskGrow`
- `Reroute`
- `ImageResize+`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: RestoreCropBox`
- `SaveImage`
- `SaveImage`
- `InpaintStitch`
- `LoadImage`
- `ImageResize+`
- `LayerUtility: CropByMask V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `180093038225841`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（61/80）

**有卡**：`VAEDecode`、`FluxGuidance`、`ImageResize+`、`Florence2ModelLoader`、`Florence2Run`、`easy imageSize`、`InpaintModelConditioning`、`ReduxAdvanced`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`LoadImage`、`EmptyImage`、`LayerMask: MaskPreview`、`LayerUtility: ImageBlendAdvance V3`、`LayerUtility: ImageRemoveAlpha`、`LayerMask: MaskGrow`、`ImageToMask`、`ImageConcanate`、`CLIPTextEncode`、`TextInput_`、`LayerUtility: TextJoin`、`LayerUtility: CropByMask V2`、`ResizeMask`、`MaskToImage`、`LoraLoaderModelOnly`、`KSampler`、`DifferentialDiffusion`、`ImageMaskSwitch`、`ImageCrop`、`LayerMask: SegmentAnythingUltra V2`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`StyleModelLoader`、`CLIPVisionLoader`、`InpaintCrop`、`VAEEncode`、`LayerUtility: RestoreCropBox`、`SaveImage`、`InpaintStitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
