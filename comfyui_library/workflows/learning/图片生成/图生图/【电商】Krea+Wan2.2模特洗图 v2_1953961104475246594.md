---
key: 图片生成/图生图/【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594.json
name: 【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594.json
hash: 3d686c87c9778c89
coverage: 0.905882
learned_at: 2026-10-23 11:50:57
nodes: [PulidFluxOptions, PulidFluxInsightFaceLoader, RandomNoise, PulidFluxEvaClipLoader, KSamplerSelect, PulidFluxFaceDetector, DualCLIPLoader, LoraLoaderModelOnly, ImpactSwitch, BasicScheduler, PulidFluxModelLoader, BasicGuider, FluxGuidance, ConditioningZeroOut, VAELoader, VAEDecode, ShowText, RH_Translator, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, VAEDecode, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPLoader, SaveImage, ModelSamplingSD3, ModelSamplingSD3, KSampler, Bjornulf_TextToStringAndSeed, LayerUtility: ImageReelComposit, DepthAnything_V2, PDIMAGE_LongerSize, OpenposePreprocessor, SetUnionControlNetType, SetUnionControlNetType, ImpactSwitch, ControlNetLoader, JWInteger, ControlNetApplyAdvanced, UNETLoader, ApplyPulidFlux, SaveImage, SaveImage, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageReel, KSampler, CLIPTextEncode, SamplerCustomAdvanced, CLIPTextEncode, EmptySD3LatentImage, ConditioningZeroOut, TeaCache, VAELoader, CLIPTextEncode, FluxGuidance, UNETLoader, PDIMAGE_LongerSize, DF_Get_image_size, EmptySD3LatentImage, DualCLIPLoader, LoadImage, CR Text Concatenate, easy imageSize, PreviewImage, PreviewImage, PreviewImage, SaveImage, VAEDecode, KSampler, Fast Groups Bypasser (rgthree), SaveImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, DownloadAndLoadDepthAnythingV2Model, LoadImage, RHHiddenNodes, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 804891250178970, "steps": 30}
---

# 图片生成/图生图/【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `PulidFluxOptions`
- `PulidFluxInsightFaceLoader`
- `RandomNoise`
- `PulidFluxEvaClipLoader`
- `KSamplerSelect` ★核心
- `PulidFluxFaceDetector`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ImpactSwitch`
- `BasicScheduler`
- `PulidFluxModelLoader`
- `BasicGuider`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecode` ★核心
- `ShowText`
- `RH_Translator`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SaveImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `Bjornulf_TextToStringAndSeed`
- `LayerUtility: ImageReelComposit`
- `DepthAnything_V2`
- `PDIMAGE_LongerSize`
- `OpenposePreprocessor`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `ImpactSwitch`
- `ControlNetLoader`
- `JWInteger`
- `ControlNetApplyAdvanced` ★核心
- `UNETLoader` ★核心
- `ApplyPulidFlux`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReel`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `TeaCache`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `PDIMAGE_LongerSize`
- `DF_Get_image_size`
- `EmptySD3LatentImage`
- `DualCLIPLoader`
- `LoadImage`
- `CR Text Concatenate`
- `easy imageSize`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadDepthAnythingV2Model`
- `LoadImage`
- `RHHiddenNodes`
- `Note`

## 关键参数

- `seed` = `804891250178970`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **91%**（77/85）

**有卡**：`PulidFluxOptions`、`PulidFluxInsightFaceLoader`、`RandomNoise`、`PulidFluxEvaClipLoader`、`KSamplerSelect`、`PulidFluxFaceDetector`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`PulidFluxModelLoader`、`BasicGuider`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`ShowText`、`RH_Translator`、`UNETLoader`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`CLIPLoader`、`SaveImage`、`ModelSamplingSD3`、`KSampler`、`Bjornulf_TextToStringAndSeed`、`LayerUtility: ImageReelComposit`、`DepthAnything_V2`、`PDIMAGE_LongerSize`、`OpenposePreprocessor`、`SetUnionControlNetType`、`ControlNetLoader`、`JWInteger`、`ControlNetApplyAdvanced`、`ApplyPulidFlux`、`LayerUtility: ImageReel`、`SamplerCustomAdvanced`、`EmptySD3LatentImage`、`TeaCache`、`DF_Get_image_size`、`LoadImage`、`CR Text Concatenate`、`easy imageSize`、`DownloadAndLoadDepthAnythingV2Model`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
