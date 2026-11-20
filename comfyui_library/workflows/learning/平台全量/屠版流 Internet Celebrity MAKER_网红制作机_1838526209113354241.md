---
key: 平台全量/屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241.json
name: 屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241.json
hash: 06467e266aacde6e
coverage: 0.848739
learned_at: 2026-11-14 02:02:08
nodes: [PreviewImage, MaskToImage, PreviewImage, VAEEncode, MeshGraphormer-DepthMapPreprocessor, KSampler, FluxGuidance, ImageScaleToTotalPixels, TTP_Image_Tile_Batch, TTP_CoordinateSplitter, TTP_condsetarea_merge, CLIPTextEncode, VAEEncode, TTP_condtobatch, BasicGuider, FluxGuidance, Constant Number, ConditioningAverage, ImageSharpen, ImageScaleBy, Reroute, ImpactImageBatchToImageList, ModelSamplingFlux, Get Image Size, CLIPTextEncode, RandomNoise, TTP_Tile_image_size, RandomNoise, KSamplerSelect, ShowText|pysssss, SplitSigmasDenoise, DisableNoise, BasicGuider, SamplerCustomAdvanced, VAELoader, VAEEncode, IPAdapterUnifiedLoaderFaceID, IPAdapterFaceID, IPAdapterNoise, UltralyticsDetectorProvider, SAMLoader, PrepImageForClipVision, ControlNetApplyAdvanced, SamplerCustomAdvanced, CR SDXL Aspect Ratio, FaceDetailer, PrepImageForClipVision, PrepImageForClipVision, Note, Reroute, smZ Settings, smZ CLIPTextEncode, Anything Everywhere, KSamplerAdvanced, PhotoMakerStyles, smZ CLIPTextEncode, Note, VAELoader, CLIPSetLastLayer, PhotoMakerLoaderPlus, PhotoMakerInsightFaceLoader, PrimitiveNode, PhotoMakerEncodePlus, TextCombinerTwo, TextCombinerTwo, KSampler, VAEDecode, VAEDecode, VAEDecode, LatentUpscaleBy, BasicScheduler, KSamplerSelect, TextInput_, BasicScheduler, VAEDecode, Seed Everywhere, CheckpointLoaderSimple, UNETLoader, DualCLIPLoader, Note, Note, ControlNetLoader, SaveImage, SaveImage, KSamplerAdvanced, Image Inset Crop (rgthree), Text Concatenate, CR Prompt Text, Florence2Run, DownloadAndLoadFlorence2Model, Florence2Run, DownloadAndLoadFlorence2Model, DownloadAndLoadFlorence2Model, TextInput_, Florence2Run, Florence2Run, DownloadAndLoadFlorence2Model, ShowText|pysssss, VAEDecodeTiled, LoadImage, LoadImage, SaveImage, SaveImage, Image Comparer (rgthree), CLIPTextEncode, LoraLoaderModelOnly, SaveImage, PreviewImage, Reroute, Reroute, PrepImageForClipVision, ImageBatch, Reroute, Reroute, ImageBatch, LoadImage, SamplerCustomAdvanced, easy cleanGpuUsed, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 25, "checkpoint": "whitePonyDiffusion4_whitepony4lite.safetensors", "controlnet_strength": 1, "denoise": "karras", "sampler_name": 5, "scheduler": "dpmpp_2m", "seed": "disable", "steps": "fixed"}
---

# 平台全量/屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241.json

> 来源文件 `comfyui_library/workflows/平台全量/屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（119 个）：
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `MeshGraphormer-DepthMapPreprocessor`
- `KSampler` ★核心
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `TTP_Image_Tile_Batch`
- `TTP_CoordinateSplitter`
- `TTP_condsetarea_merge`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `TTP_condtobatch`
- `BasicGuider`
- `FluxGuidance`
- `Constant Number`
- `ConditioningAverage`
- `ImageSharpen`
- `ImageScaleBy`
- `Reroute`
- `ImpactImageBatchToImageList`
- `ModelSamplingFlux`
- `Get Image Size`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `TTP_Tile_image_size`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `DisableNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `IPAdapterUnifiedLoaderFaceID`
- `IPAdapterFaceID`
- `IPAdapterNoise`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `PrepImageForClipVision`
- `ControlNetApplyAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CR SDXL Aspect Ratio`
- `FaceDetailer`
- `PrepImageForClipVision`
- `PrepImageForClipVision`
- `Note`
- `Reroute`
- `smZ Settings`
- `smZ CLIPTextEncode` ★核心
- `Anything Everywhere`
- `KSamplerAdvanced` ★核心
- `PhotoMakerStyles`
- `smZ CLIPTextEncode` ★核心
- `Note`
- `VAELoader`
- `CLIPSetLastLayer`
- `PhotoMakerLoaderPlus`
- `PhotoMakerInsightFaceLoader`
- `PrimitiveNode`
- `PhotoMakerEncodePlus`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LatentUpscaleBy`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `TextInput_`
- `BasicScheduler`
- `VAEDecode` ★核心
- `Seed Everywhere`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Note`
- `Note`
- `ControlNetLoader`
- `SaveImage`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `Image Inset Crop (rgthree)`
- `Text Concatenate`
- `CR Prompt Text`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadFlorence2Model`
- `TextInput_`
- `Florence2Run`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `ShowText|pysssss`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `PrepImageForClipVision`
- `ImageBatch`
- `Reroute`
- `Reroute`
- `ImageBatch`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `25`
- `sampler_name` = `5`
- `scheduler` = `dpmpp_2m`
- `denoise` = `karras`
- `controlnet_strength` = `1`
- `checkpoint` = `whitePonyDiffusion4_whitepony4lite.safetensors`

## 知识

覆盖率 **85%**（101/119）

**有卡**：`MaskToImage`、`VAEEncode`、`MeshGraphormer-DepthMapPreprocessor`、`KSampler`、`FluxGuidance`、`ImageScaleToTotalPixels`、`TTP_Image_Tile_Batch`、`TTP_CoordinateSplitter`、`TTP_condsetarea_merge`、`CLIPTextEncode`、`TTP_condtobatch`、`BasicGuider`、`Constant Number`、`ConditioningAverage`、`ImageSharpen`、`ImageScaleBy`、`ImpactImageBatchToImageList`、`ModelSamplingFlux`、`Get Image Size`、`RandomNoise`、`TTP_Tile_image_size`、`KSamplerSelect`、`SplitSigmasDenoise`、`DisableNoise`、`SamplerCustomAdvanced`、`VAELoader`、`IPAdapterUnifiedLoaderFaceID`、`IPAdapterFaceID`、`IPAdapterNoise`、`UltralyticsDetectorProvider`、`SAMLoader`、`PrepImageForClipVision`、`ControlNetApplyAdvanced`、`CR SDXL Aspect Ratio`、`FaceDetailer`、`smZ Settings`、`smZ CLIPTextEncode`、`KSamplerAdvanced`、`PhotoMakerStyles`、`CLIPSetLastLayer`、`PhotoMakerLoaderPlus`、`PhotoMakerInsightFaceLoader`、`PhotoMakerEncodePlus`、`TextCombinerTwo`、`VAEDecode`、`LatentUpscaleBy`、`BasicScheduler`、`TextInput_`、`Seed Everywhere`、`CheckpointLoaderSimple`、`UNETLoader`、`DualCLIPLoader`、`ControlNetLoader`、`SaveImage`、`Image Inset Crop (rgthree)`、`Text Concatenate`、`CR Prompt Text`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`VAEDecodeTiled`、`LoadImage`、`LoraLoaderModelOnly`、`ImageBatch`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage
