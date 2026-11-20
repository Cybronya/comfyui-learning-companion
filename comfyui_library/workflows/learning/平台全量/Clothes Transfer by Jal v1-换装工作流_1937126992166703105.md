---
key: 平台全量/Clothes Transfer by Jal v1-换装工作流_1937126992166703105.json
name: Clothes Transfer by Jal v1-换装工作流_1937126992166703105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Clothes Transfer by Jal v1-换装工作流_1937126992166703105.json
hash: cc1695f178222bb1
coverage: 0.804878
learned_at: 2026-11-14 00:22:14
nodes: [MaskToImage, PreviewImage, SaveImage, LayerMask: MaskPreview, LayerMask: MaskPreview, ImageConcanate, PreviewImage, PreviewImage, PreviewImage, MaskComposite, ImageToMask, ImageConcanate, ImageToMask, EmptyImage, EmptyImage, PreviewBridge, EmptyImage, RandomNoise, KSamplerSelect, BasicGuider, CLIPTextEncode, CLIPTextEncode, FluxGuidance, CLIPVisionEncode, StyleModelApply, StyleModelLoader, InpaintModelConditioning, BasicScheduler, ImageConcanate, Get Image Size, VAEDecode, SamplerCustomAdvanced, InpaintStitchImproved, MathExpression|pysssss, ETN_CropImage, ImageConcanate, ImageResize+, VAELoader, DualCLIPLoaderGGUF, CLIPVisionLoader, UnetLoaderGGUF, MaskToImage, MaskToImage, LoadImage, MaskToImage, InpaintCropImproved, GrowMaskWithBlur, easy humanSegmentation, LayerMask: HumanPartsUltra, PreviewImage, ImpactSwitch, PreviewImage, PreviewImage, LoadImage, Fast Groups Muter (rgthree), GrowMaskWithBlur, ImpactSwitch, PrimitiveNode, BiRefNetRMBG, Sam2Segmentation, DownloadAndLoadSAM2Model, easy humanSegmentation, Color (RGB), MaskToImage, DownloadAndLoadSAM2Model, Sam2Segmentation, LayerMask: HumanPartsUltra, PreviewImage, MaskToImage, PreviewImage, ImageResize+, easy imageSize, ImageResize+, PreviewImage, JWMaskResize, easy imageSize, ImageConcanate, JWMaskResize, ImageResize+, PreviewImage, PreviewImage, SaveImage]
patterns: []
missing: []
---

# 平台全量/Clothes Transfer by Jal v1-换装工作流_1937126992166703105.json

> 来源文件 `comfyui_library/workflows/平台全量/Clothes Transfer by Jal v1-换装工作流_1937126992166703105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `ImageConcanate`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MaskComposite`
- `ImageToMask`
- `ImageConcanate`
- `ImageToMask`
- `EmptyImage`
- `EmptyImage`
- `PreviewBridge`
- `EmptyImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPVisionEncode`
- `StyleModelApply`
- `StyleModelLoader`
- `InpaintModelConditioning`
- `BasicScheduler`
- `ImageConcanate`
- `Get Image Size`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `InpaintStitchImproved`
- `MathExpression|pysssss`
- `ETN_CropImage`
- `ImageConcanate`
- `ImageResize+`
- `VAELoader`
- `DualCLIPLoaderGGUF`
- `CLIPVisionLoader`
- `UnetLoaderGGUF` ★核心
- `MaskToImage`
- `MaskToImage`
- `LoadImage`
- `MaskToImage`
- `InpaintCropImproved`
- `GrowMaskWithBlur`
- `easy humanSegmentation`
- `LayerMask: HumanPartsUltra`
- `PreviewImage`
- `ImpactSwitch`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `GrowMaskWithBlur`
- `ImpactSwitch`
- `PrimitiveNode`
- `BiRefNetRMBG`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `easy humanSegmentation`
- `Color (RGB)`
- `MaskToImage`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `LayerMask: HumanPartsUltra`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `ImageResize+`
- `easy imageSize`
- `ImageResize+`
- `PreviewImage`
- `JWMaskResize`
- `easy imageSize`
- `ImageConcanate`
- `JWMaskResize`
- `ImageResize+`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`

## 知识

覆盖率 **80%**（66/82）

**有卡**：`MaskToImage`、`SaveImage`、`LayerMask: MaskPreview`、`ImageConcanate`、`MaskComposite`、`ImageToMask`、`EmptyImage`、`PreviewBridge`、`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`CLIPTextEncode`、`FluxGuidance`、`CLIPVisionEncode`、`StyleModelApply`、`StyleModelLoader`、`InpaintModelConditioning`、`BasicScheduler`、`Get Image Size`、`VAEDecode`、`SamplerCustomAdvanced`、`InpaintStitchImproved`、`MathExpression|pysssss`、`ETN_CropImage`、`ImageResize+`、`VAELoader`、`DualCLIPLoaderGGUF`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`LoadImage`、`InpaintCropImproved`、`GrowMaskWithBlur`、`easy humanSegmentation`、`LayerMask: HumanPartsUltra`、`BiRefNetRMBG`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`Color (RGB)`、`easy imageSize`、`JWMaskResize`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、CLIPVisionEncode
