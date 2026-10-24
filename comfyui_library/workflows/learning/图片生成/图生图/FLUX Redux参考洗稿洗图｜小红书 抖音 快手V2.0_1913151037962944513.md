---
key: 图片生成/图生图/FLUX Redux参考洗稿洗图｜小红书 抖音 快手V2.0_1913151037962944513.json
name: FLUX Redux参考洗稿洗图｜小红书 抖音 快手V2.0_1913151037962944513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Redux参考洗稿洗图｜小红书 抖音 快手V2.0_1913151037962944513.json
hash: 4306a89fbf0733fa
coverage: 0.75
learned_at: 2026-10-23 10:53:32
nodes: [BasicGuider, BasicScheduler, PulidFluxInsightFaceLoader, GetNode, ModelSamplingFlux, Anything Everywhere, Anything Everywhere3, SetNode, ConstrainImage|pysssss, GetNode, GetNode, VAEDecode, ApplyPulidFlux, FaceAnalysisModels, LoadImage, PreviewImage, SetNode, SetNode, KSamplerSelect, CLIPTextEncode, SamplerCustomAdvanced, RandomNoise, Seed Everywhere, GetNode, Batch Make (mtb), ConditioningZeroOut, SAMLoader, EmptySD3LatentImage, ImageBatchMulti, FaceBoundingBox, LoadImage, PulidFluxEvaClipLoader, LoadImage, FaceBoundingBox, FaceAnalysisModels, LoadImage, FaceBoundingBox, FaceAnalysisModels, FaceBoundingBox, Fast Groups Bypasser (rgthree), GetNode, CR Text Concatenate, Anything Everywhere, LayerFilter: HDREffects, LayerFilter: AddGrain, LayerFilter: MotionBlur, LoadImage, DepthAnythingV2Preprocessor, LayerFilter: FilmV2, VAELoader, LayerUtility: GetImageSize, CLIPTextEncode, ShowText|pysssss, ReduxAdvanced, LoadImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, TextInput_, LoraLoaderModelOnly, DualCLIPLoader, Joy_caption_two_load, StyleModelLoader, CLIPVisionLoader, UltralyticsDetectorProvider, FaceAnalysisModels, PulidFluxModelLoader, UNETLoader, Joy_caption_two, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SaveImage, SaveImage, FaceDetailer]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX Redux参考洗稿洗图｜小红书 抖音 快手V2.0_1913151037962944513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Redux参考洗稿洗图｜小红书 抖音 快手V2.0_1913151037962944513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `BasicGuider`
- `BasicScheduler`
- `PulidFluxInsightFaceLoader`
- `GetNode`
- `ModelSamplingFlux`
- `Anything Everywhere`
- `Anything Everywhere3`
- `SetNode`
- `ConstrainImage|pysssss`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ApplyPulidFlux`
- `FaceAnalysisModels`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Seed Everywhere`
- `GetNode`
- `Batch Make (mtb)`
- `ConditioningZeroOut`
- `SAMLoader`
- `EmptySD3LatentImage`
- `ImageBatchMulti`
- `FaceBoundingBox`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `LoadImage`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `LoadImage`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `CR Text Concatenate`
- `Anything Everywhere`
- `LayerFilter: HDREffects`
- `LayerFilter: AddGrain`
- `LayerFilter: MotionBlur`
- `LoadImage`
- `DepthAnythingV2Preprocessor`
- `LayerFilter: FilmV2`
- `VAELoader`
- `LayerUtility: GetImageSize`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ReduxAdvanced`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `TextInput_`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `Joy_caption_two_load`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `UltralyticsDetectorProvider`
- `FaceAnalysisModels`
- `PulidFluxModelLoader`
- `UNETLoader` ★核心
- `Joy_caption_two`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SaveImage`
- `SaveImage`
- `FaceDetailer`

## 知识

覆盖率 **75%**（57/76）

**有卡**：`BasicGuider`、`BasicScheduler`、`PulidFluxInsightFaceLoader`、`ModelSamplingFlux`、`ConstrainImage|pysssss`、`VAEDecode`、`ApplyPulidFlux`、`FaceAnalysisModels`、`LoadImage`、`KSamplerSelect`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`Seed Everywhere`、`Batch Make (mtb)`、`ConditioningZeroOut`、`SAMLoader`、`EmptySD3LatentImage`、`ImageBatchMulti`、`FaceBoundingBox`、`PulidFluxEvaClipLoader`、`CR Text Concatenate`、`LayerFilter: HDREffects`、`LayerFilter: AddGrain`、`LayerFilter: MotionBlur`、`DepthAnythingV2Preprocessor`、`LayerFilter: FilmV2`、`VAELoader`、`LayerUtility: GetImageSize`、`ReduxAdvanced`、`TextInput_`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`Joy_caption_two_load`、`StyleModelLoader`、`CLIPVisionLoader`、`UltralyticsDetectorProvider`、`PulidFluxModelLoader`、`UNETLoader`、`Joy_caption_two`、`SaveImage`、`FaceDetailer`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、DepthAnythingV2Preprocessor
