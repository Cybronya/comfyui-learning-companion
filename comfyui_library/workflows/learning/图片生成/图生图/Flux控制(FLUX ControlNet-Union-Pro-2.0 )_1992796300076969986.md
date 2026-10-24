---
key: 图片生成/图生图/Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986.json
name: Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986.json
hash: 04b9ef4fe2366773
coverage: 0.96
learned_at: 2026-10-23 11:02:10
nodes: [BasicGuider, VAEEncode, RandomNoise, KSamplerSelect, easy cleanGpuUsed, VAEDecode, FluxGuidance, SamplerCustomAdvanced, PreviewImage, BasicScheduler, SaveImage, SetUnionControlNetType, DualCLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ApplyFBCacheOnModel, EmptyLatentImage, LoraLoaderModelOnly, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, AIO_Preprocessor, LoadImage, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.8000000000000002, "height": 1024, "width": 768}
---

# 图片生成/图生图/Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `BasicGuider`
- `VAEEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `BasicScheduler`
- `SaveImage`
- `SetUnionControlNetType`
- `DualCLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ApplyFBCacheOnModel`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`BasicGuider`、`VAEEncode`、`RandomNoise`、`KSamplerSelect`、`easy cleanGpuUsed`、`VAEDecode`、`FluxGuidance`、`SamplerCustomAdvanced`、`BasicScheduler`、`SaveImage`、`SetUnionControlNetType`、`DualCLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ApplyFBCacheOnModel`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`AIO_Preprocessor`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
