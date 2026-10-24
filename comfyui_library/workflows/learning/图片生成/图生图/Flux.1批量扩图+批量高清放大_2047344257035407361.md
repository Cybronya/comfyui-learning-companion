---
key: 图片生成/图生图/Flux.1批量扩图+批量高清放大_2047344257035407361.json
name: Flux.1批量扩图+批量高清放大_2047344257035407361
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1批量扩图+批量高清放大_2047344257035407361.json
hash: e1c311cb07db70db
coverage: 0.852273
learned_at: 2026-10-23 10:58:44
nodes: [VAELoader, KSampler, UNETLoader, DualCLIPLoader, FluxGuidance, ConditioningZeroOut, InpaintModelConditioning, PreviewImage, RHBatchImages:, easy imageCount, Bjornulf_ShowInt, easy cleanGpuUsed, VAEDecode, SaveImage, ImagePadForOutpaint, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), easy batchAnything, easy forLoopStart, easy joinImageBatch, easy showAnything, easy forLoopEnd, RHExtractImage, PreviewImage, RHUploadZip, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, LayerUtility: PurgeVRAM V2, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, VAEDecode, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, PreviewAny, JDCN_StringToList, PreviewImage, UNETLoader, NunchakuFluxLoraLoader, DualCLIPLoader, CLIPTextEncode, KSampler, ConditioningZeroOut, VAELoader, ReferenceLatent, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEDecode, FluxGuidance, LayerUtility: PurgeVRAM V2, VAELoader, VHS_VAEEncodeBatched, NunchakuFluxDiTLoader, RHBatchImages:, easy imageCount, Bjornulf_ShowInt, easy cleanGpuUsed, easy forLoopStart, easy joinImageBatch, easy showAnything, easy forLoopEnd, RHUploadZip, CompressImages, CompressImages, RHExtractImage, PreviewImage, ImpactSwitch, SeedVR2VideoUpscaler, easy batchAnything, Image Comparer (rgthree), CLIPTextEncode, LayerUtility: PurgeVRAM V2, Qwen3VL_Advanced, SeedVR2LoadDiTModel, SaveImage, LoadImage, easy int, Float, ImpactSwitch, LoraLoaderModelOnly, DifferentialDiffusion, LoadImage, Int, Int, Int, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 39369066744103, "steps": 10}
---

# 图片生成/图生图/Flux.1批量扩图+批量高清放大_2047344257035407361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1批量扩图+批量高清放大_2047344257035407361.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `PreviewImage`
- `RHBatchImages:`
- `easy imageCount`
- `Bjornulf_ShowInt`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `ImagePadForOutpaint`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `easy batchAnything`
- `easy forLoopStart`
- `easy joinImageBatch`
- `easy showAnything`
- `easy forLoopEnd`
- `RHExtractImage`
- `PreviewImage`
- `RHUploadZip`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `JDCN_StringToList`
- `PreviewImage`
- `UNETLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `FluxGuidance`
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `VHS_VAEEncodeBatched` ★核心
- `NunchakuFluxDiTLoader`
- `RHBatchImages:`
- `easy imageCount`
- `Bjornulf_ShowInt`
- `easy cleanGpuUsed`
- `easy forLoopStart`
- `easy joinImageBatch`
- `easy showAnything`
- `easy forLoopEnd`
- `RHUploadZip`
- `CompressImages`
- `CompressImages`
- `RHExtractImage`
- `PreviewImage`
- `ImpactSwitch`
- `SeedVR2VideoUpscaler`
- `easy batchAnything`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `Qwen3VL_Advanced`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `LoadImage`
- `easy int`
- `Float`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `DifferentialDiffusion`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `39369066744103`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（75/88）

**有卡**：`VAELoader`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`FluxGuidance`、`ConditioningZeroOut`、`InpaintModelConditioning`、`RHBatchImages:`、`easy imageCount`、`Bjornulf_ShowInt`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`ImagePadForOutpaint`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy batchAnything`、`easy forLoopStart`、`easy joinImageBatch`、`easy forLoopEnd`、`RHExtractImage`、`RHUploadZip`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadVAEModel`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`JDCN_StringToList`、`NunchakuFluxLoraLoader`、`ReferenceLatent`、`VAEEncode`、`VHS_VAEEncodeBatched`、`NunchakuFluxDiTLoader`、`CompressImages`、`SeedVR2VideoUpscaler`、`Qwen3VL_Advanced`、`SeedVR2LoadDiTModel`、`LoadImage`、`easy int`、`Float`、`DifferentialDiffusion`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
