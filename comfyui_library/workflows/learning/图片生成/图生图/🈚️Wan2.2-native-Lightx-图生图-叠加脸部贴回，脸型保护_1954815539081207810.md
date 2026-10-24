---
key: 图片生成/图生图/🈚️Wan2.2-native-Lightx-图生图-叠加脸部贴回，脸型保护_1954815539081207810.json
name: 🈚️Wan2.2-native-Lightx-图生图-叠加脸部贴回，脸型保护_1954815539081207810
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🈚️Wan2.2-native-Lightx-图生图-叠加脸部贴回，脸型保护_1954815539081207810.json
hash: 1a7fb460d3839369
coverage: 0.52795
learned_at: 2026-10-23 13:38:41
nodes: [VAELoader, SetNode, GetNode, SetNode, SetNode, LoadJanusModel, JanusImage2Text, SetNode, GetNode, GetNode, GetNode, ImageFromBatch+, GetNode, SetNode, GetNode, SetNode, CR Text, easy showAnything, LayerUtility: RestoreCropBox, LayerUtility: RestoreCropBox, GetNode, SetNode, SetNode, PreviewImage, GetNode, VAEDecode, GetNode, SetNode, ApplySageAttention, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LayerMask: PersonMaskUltra V2, LayerMask: MaskPreview, LayerUtility: PurgeVRAM V2, SetNode, CLIPTextEncode, CLIPLoader, SetNode, SetNode, GetNode, ImageSmartSharpen+, PreviewImage, SetNode, SetNode, ImageSmartSharpen+, GetNode, PreviewImage, easy seed, UNETLoader, UnetLoaderGGUF, MaskToSEGS, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageAndMaskPreview, LayerUtility: ImageScaleRestore V2, SetNode, GetNode, GetNode, LayerUtility: CropByMask V2, LayerMask: MaskGrow, LayerUtility: TextJoin, GetNode, LayerMask: MaskGrow, SegsToCombinedMask, LayerMask: MaskGrow, LoraLoaderModelOnly, SetNode, CLIPTextEncode, ApplySageAttention, LoraLoaderModelOnly, UNETLoader, UnetLoaderGGUF, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, wanBlockSwap, wanBlockSwap, CLIPTextEncode, VAEEncode, GetNode, GetNode, GetNode, GetNode, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, CLIPTextEncode, easy cleanGpuUsed, SetNode, SetNode, LayerMask: MaskPreview, CLIPTextEncode, GetNode, VAEDecode, GetNode, InpaintModelConditioning, SetNode, GetNode, GetNode, ImageSmartSharpen+, GetNode, InpaintStitch, LayerMask: PersonMaskUltra V2, GetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, easy imageRemBg, LayerMask: PersonMaskUltra V2, InpaintCrop, KSampler, PreviewImage, GetNode, GetNode, PreviewImage, DifferentialDiffusion, DifferentialDiffusion, InpaintModelConditioning, Image Comparer (rgthree), GetNode, ImageSmartSharpen+, SaveImage, SaveImage, ImageSmartSharpen+, SaveImage, GetNode, GetNode, UpscaleModelLoader, KSampler, ModelSamplingSD3, GetNode, VAEDecode, PreviewImage, LatentPixelScale, LoadImage, SaveImage, KSampler, SetNode, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, WanMoeKSampler, InpaintCrop, ImageSmartSharpen+, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "denoise": "heun", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/🈚️Wan2.2-native-Lightx-图生图-叠加脸部贴回，脸型保护_1954815539081207810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🈚️Wan2.2-native-Lightx-图生图-叠加脸部贴回，脸型保护_1954815539081207810.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（161 个）：
- `VAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadJanusModel`
- `JanusImage2Text`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `easy showAnything`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: RestoreCropBox`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `ApplySageAttention`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskPreview`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `PreviewImage`
- `easy seed`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `MaskToSEGS`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageAndMaskPreview`
- `LayerUtility: ImageScaleRestore V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: CropByMask V2`
- `LayerMask: MaskGrow`
- `LayerUtility: TextJoin`
- `GetNode`
- `LayerMask: MaskGrow`
- `SegsToCombinedMask`
- `LayerMask: MaskGrow`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `ApplySageAttention`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `wanBlockSwap`
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `InstantIDModelLoader`
- `DifferentialDiffusion`
- `ApplyInstantID`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `InpaintModelConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `InpaintStitch`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `LayerMask: PersonMaskUltra V2`
- `InpaintCrop`
- `KSampler` ★核心
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `DifferentialDiffusion`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `GetNode`
- `ImageSmartSharpen+`
- `SaveImage`
- `SaveImage`
- `ImageSmartSharpen+`
- `SaveImage`
- `GetNode`
- `GetNode`
- `UpscaleModelLoader`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `GetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `LatentPixelScale`
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心
- `SetNode`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `WanMoeKSampler` ★核心
- `InpaintCrop`
- `ImageSmartSharpen+`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `heun`

## 知识

覆盖率 **53%**（85/161）

**有卡**：`VAELoader`、`LoadJanusModel`、`JanusImage2Text`、`ImageFromBatch+`、`CR Text`、`LayerUtility: RestoreCropBox`、`VAEDecode`、`ApplySageAttention`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: PersonMaskUltra V2`、`LayerMask: MaskPreview`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`CLIPLoader`、`ImageSmartSharpen+`、`easy seed`、`UNETLoader`、`UnetLoaderGGUF`、`MaskToSEGS`、`ImageAndMaskPreview`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: CropByMask V2`、`LayerMask: MaskGrow`、`LayerUtility: TextJoin`、`SegsToCombinedMask`、`wanBlockSwap`、`VAEEncode`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`DifferentialDiffusion`、`ApplyInstantID`、`easy cleanGpuUsed`、`InpaintModelConditioning`、`InpaintStitch`、`easy imageRemBg`、`InpaintCrop`、`KSampler`、`SaveImage`、`UpscaleModelLoader`、`ModelSamplingSD3`、`LatentPixelScale`、`LoadImage`、`Manual XY Entry Info`、`WanMoeKSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
