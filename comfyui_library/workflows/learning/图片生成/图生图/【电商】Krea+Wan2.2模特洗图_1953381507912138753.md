---
key: 图片生成/图生图/【电商】Krea+Wan2.2模特洗图_1953381507912138753.json
name: 【电商】Krea+Wan2.2模特洗图_1953381507912138753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【电商】Krea+Wan2.2模特洗图_1953381507912138753.json
hash: b78a91f5da27c74f
coverage: 0.9
learned_at: 2026-10-23 11:50:58
nodes: [PulidFluxOptions, PulidFluxInsightFaceLoader, RandomNoise, PulidFluxEvaClipLoader, KSamplerSelect, PreviewImage, PulidFluxFaceDetector, DualCLIPLoader, LoraLoaderModelOnly, ImpactSwitch, BasicScheduler, PulidFluxModelLoader, BasicGuider, FluxGuidance, ConditioningZeroOut, VAELoader, EmptySD3LatentImage, VAEDecode, ShowText, RH_Translator, CR Text Concatenate, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, VAEDecode, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPLoader, SaveImage, ModelSamplingSD3, ModelSamplingSD3, KSampler, Bjornulf_TextToStringAndSeed, LayerUtility: ImageReelComposit, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, PDIMAGE_LongerSize, OpenposePreprocessor, SetUnionControlNetType, SetUnionControlNetType, ImpactSwitch, ControlNetLoader, JWInteger, ControlNetApplyAdvanced, LayerUtility: PurgeVRAM, UNETLoader, ApplyPulidFlux, SaveImage, SaveImage, PreviewImage, LoraLoaderModelOnly, LoadImage, LayerUtility: ImageReel, PreviewImage, PreviewImage, SaveImage, LoadImage, easy imageSize, KSampler, CLIPTextEncode, SamplerCustomAdvanced, CLIPTextEncode, RHHiddenNodes, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10}
---

# 图片生成/图生图/【电商】Krea+Wan2.2模特洗图_1953381507912138753.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【电商】Krea+Wan2.2模特洗图_1953381507912138753.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `PulidFluxOptions`
- `PulidFluxInsightFaceLoader`
- `RandomNoise`
- `PulidFluxEvaClipLoader`
- `KSamplerSelect` ★核心
- `PreviewImage`
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
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `ShowText`
- `RH_Translator`
- `CR Text Concatenate`
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
- `DownloadAndLoadDepthAnythingV2Model`
- `PDIMAGE_LongerSize`
- `OpenposePreprocessor`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `ImpactSwitch`
- `ControlNetLoader`
- `JWInteger`
- `ControlNetApplyAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `ApplyPulidFlux`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LayerUtility: ImageReel`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `easy imageSize`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `Note`

## 关键参数

- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **90%**（63/70）

**有卡**：`PulidFluxOptions`、`PulidFluxInsightFaceLoader`、`RandomNoise`、`PulidFluxEvaClipLoader`、`KSamplerSelect`、`PulidFluxFaceDetector`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`PulidFluxModelLoader`、`BasicGuider`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`EmptySD3LatentImage`、`VAEDecode`、`ShowText`、`RH_Translator`、`CR Text Concatenate`、`UNETLoader`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`CLIPLoader`、`SaveImage`、`ModelSamplingSD3`、`KSampler`、`Bjornulf_TextToStringAndSeed`、`LayerUtility: ImageReelComposit`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`PDIMAGE_LongerSize`、`OpenposePreprocessor`、`SetUnionControlNetType`、`ControlNetLoader`、`JWInteger`、`ControlNetApplyAdvanced`、`ApplyPulidFlux`、`LoadImage`、`LayerUtility: ImageReel`、`easy imageSize`、`SamplerCustomAdvanced`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
