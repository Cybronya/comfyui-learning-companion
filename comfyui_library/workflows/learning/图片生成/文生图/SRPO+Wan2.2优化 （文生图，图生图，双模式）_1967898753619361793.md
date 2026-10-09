---
key: 图片生成/文生图/SRPO+Wan2.2优化 （文生图，图生图，双模式）_1967898753619361793.json
name: SRPO+Wan2.2优化 （文生图，图生图，双模式）_1967898753619361793.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SRPO+Wan2.2优化 （文生图，图生图，双模式）_1967898753619361793.json
hash: 6a14af04fe3fc057
coverage: 0.7625
learned_at: 2026-10-09 02:01:38
nodes: [DualCLIPLoader, VAELoader, UNETLoader, DualCLIPLoader, BasicGuider, FluxGuidance, UNETLoader, KSamplerSelect, ModelSamplingFlux, SamplerCustomAdvanced, VAELoader, VAEEncode, CLIPTextEncode, FluxGuidance, CLIPTextEncode, ModelSamplingFlux, SaveImage, EmptySD3LatentImage, RH_Translator, easy showAnything, VAELoader, CLIPLoader, ModelSamplingSD3, CLIPTextEncode, PreviewImage, PreviewImage, VAEEncode, ImageScaleToMegapixels, LayerUtility: LoadJoyCaptionBeta1Model, VAEEncode, Reroute, RandomNoise, RandomNoise, VAEDecode, KSamplerSelect, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, ImpactInt, BasicScheduler, BasicGuider, CLIPLoader, ModelSamplingSD3, LoraLoaderModelOnly, KSampler, KSampler, VAELoader, BasicScheduler, Text, ShowText|pysssss, CLIPTextEncode, CLIPTextEncode, PreviewImage, PreviewImage, SaveImage, PreviewImage, ImpactInt, easy cleanGpuUsed, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, UpscaleModelLoader, SeedVR2, SeedVR2BlockSwap, SeedVR2, SeedVR2BlockSwap, UNETLoader, UNETLoader, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, ImageScaleToMegapixels, ImageScaleToMegapixels, Image Comparer (rgthree), Image Comparer (rgthree)]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1038, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/SRPO+Wan2.2优化 （文生图，图生图，双模式）_1967898753619361793.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1967898753619361793.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `BasicGuider`
- `FluxGuidance`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ModelSamplingFlux`
- `SaveImage`
- `EmptySD3LatentImage`
- `RH_Translator`
- `easy showAnything`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `ImageScaleToMegapixels`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `VAEEncode` ★核心
- `Reroute`
- `RandomNoise`
- `RandomNoise`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1`
- `ImpactInt`
- `BasicScheduler`
- `BasicGuider`
- `CLIPLoader`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAELoader`
- `BasicScheduler`
- `Text`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `ImpactInt`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToMegapixels`
- `ImageScaleToMegapixels`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1038`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **76%**（61/80）

**有卡**：`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`BasicGuider`、`FluxGuidance`、`KSamplerSelect`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`VAEEncode`、`CLIPTextEncode`、`SaveImage`、`EmptySD3LatentImage`、`RH_Translator`、`CLIPLoader`、`ModelSamplingSD3`、`ImageScaleToMegapixels`、`RandomNoise`、`VAEDecode`、`LoadImage`、`ImpactInt`、`BasicScheduler`、`LoraLoaderModelOnly`、`KSampler`、`Text`、`UpscaleModelLoader`、`SeedVR2`、`SeedVR2BlockSwap`

**缺卡**（9）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
