---
key: 平台全量/FLUX 1.D_Fill+Redux万物迁移（自动）_1906321164938186753.json
name: FLUX 1.D_Fill+Redux万物迁移（自动）_1906321164938186753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX 1.D_Fill+Redux万物迁移（自动）_1906321164938186753.json
hash: 9805918924c1c611
coverage: 0.567308
learned_at: 2026-11-14 00:24:29
nodes: [GetNode, BasicGuider, SamplerCustomAdvanced, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, ImageConcanate, PreviewImage, KSamplerSelect, GetImageSize+, PreviewImage, GetNode, GetNode, InpaintCrop, SetNode, SplitImageWithAlpha, JoinImageWithAlpha, PreviewImage, SetNode, PreviewImage, BasicScheduler, PreviewImage, VAEDecode, RandomNoise, GetNode, SplitImageWithAlpha, MaskPreview+, ArgosTranslateTextNode, ArgosTranslateTextNode, PreviewImage, PreviewImage, PreviewImage, PreviewImage, MaskPreview+, ImageConcanate, GetNode, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, LayerMask: LoadFlorence2Model, SaveImage, LayerMask: ObjectDetectorFL2, GrowMaskWithBlur, ShowText|pysssss, LayerUtility: CropByMask V2, ImageResizeKJ, PreviewImage, SetNode, ImageResizeKJ, SetNode, PreviewImage, CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, LayerMask: DrawBBoxMaskV2, ReduxAdvanced, InpaintModelConditioning, FluxGuidance, LayerUtility: ColorImage, LoadImage, ImpactConditionalBranch, Text Multiline, SiliconflowLLM, ShowText|pysssss, GetNode, GetNode, PreviewImage, MaskPreview+, JoinImageWithAlpha, ImageConcanate, GrowMaskWithBlur, GetNode, GetNode, Mask Fill Holes, GetNode, SetNode, LayerMask: MaskPreview, SetNode, LayerStyle: ColorOverlay V2, Mask Fill Holes, DualCLIPLoader, StyleModelLoader, CLIPVisionLoader, InpaintStitch, SetNode, PreviewImage, LoadImage, Text Multiline, LayerMask: SAM2Ultra, Text Multiline, LoraLoaderModelOnly, UNETLoader, VAELoader, PrimitiveString, CLIPVisionEncode, DifferentialDiffusion, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 平台全量/FLUX 1.D_Fill+Redux万物迁移（自动）_1906321164938186753.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX 1.D_Fill+Redux万物迁移（自动）_1906321164938186753.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `GetImageSize+`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `InpaintCrop`
- `SetNode`
- `SplitImageWithAlpha`
- `JoinImageWithAlpha`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `BasicScheduler`
- `PreviewImage`
- `VAEDecode` ★核心
- `RandomNoise`
- `GetNode`
- `SplitImageWithAlpha`
- `MaskPreview+`
- `ArgosTranslateTextNode`
- `ArgosTranslateTextNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MaskPreview+`
- `ImageConcanate`
- `GetNode`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: LoadFlorence2Model`
- `SaveImage`
- `LayerMask: ObjectDetectorFL2`
- `GrowMaskWithBlur`
- `ShowText|pysssss`
- `LayerUtility: CropByMask V2`
- `ImageResizeKJ`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJ`
- `SetNode`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `LayerMask: DrawBBoxMaskV2`
- `ReduxAdvanced`
- `InpaintModelConditioning`
- `FluxGuidance`
- `LayerUtility: ColorImage`
- `LoadImage`
- `ImpactConditionalBranch`
- `Text Multiline`
- `SiliconflowLLM`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MaskPreview+`
- `JoinImageWithAlpha`
- `ImageConcanate`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `Mask Fill Holes`
- `GetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `LayerStyle: ColorOverlay V2`
- `Mask Fill Holes`
- `DualCLIPLoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `InpaintStitch`
- `SetNode`
- `PreviewImage`
- `LoadImage`
- `Text Multiline`
- `LayerMask: SAM2Ultra`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveString`
- `CLIPVisionEncode`
- `DifferentialDiffusion`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **57%**（59/104）

**有卡**：`BasicGuider`、`SamplerCustomAdvanced`、`ImageConcanate`、`KSamplerSelect`、`GetImageSize+`、`InpaintCrop`、`SplitImageWithAlpha`、`JoinImageWithAlpha`、`BasicScheduler`、`VAEDecode`、`RandomNoise`、`MaskPreview+`、`ArgosTranslateTextNode`、`LayerMask: SAM2Ultra`、`LayerMask: ObjectDetectorFL2`、`LayerMask: LoadFlorence2Model`、`SaveImage`、`GrowMaskWithBlur`、`LayerUtility: CropByMask V2`、`ImageResizeKJ`、`CLIPTextEncode`、`LayerMask: DrawBBoxMaskV2`、`ReduxAdvanced`、`InpaintModelConditioning`、`FluxGuidance`、`LayerUtility: ColorImage`、`LoadImage`、`ImpactConditionalBranch`、`Text Multiline`、`SiliconflowLLM`、`Mask Fill Holes`、`LayerMask: MaskPreview`、`LayerStyle: ColorOverlay V2`、`DualCLIPLoader`、`StyleModelLoader`、`CLIPVisionLoader`、`InpaintStitch`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPVisionEncode`、`DifferentialDiffusion`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
