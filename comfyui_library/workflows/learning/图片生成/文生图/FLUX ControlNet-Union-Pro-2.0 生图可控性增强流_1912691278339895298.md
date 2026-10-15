---
key: 图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json
name: FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json
hash: 9349ff5c16fc0253
coverage: 0.96
learned_at: 2026-10-15 22:26:16
nodes: [DualCLIPLoader, KSamplerSelect, FluxGuidance, EmptyLatentImage, CLIPTextEncode, BasicGuider, BasicScheduler, VAELoader, DualCLIPLoader, KSamplerSelect, FluxGuidance, EmptyLatentImage, CLIPTextEncode, BasicGuider, IPAdapterFluxLoader, BasicScheduler, VAELoader, SamplerCustomAdvanced, VAEEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, IPAdapterFluxLoader, SamplerCustomAdvanced, ApplyIPAdapterFlux, VAEDecode, SetUnionControlNetType, AIO_Preprocessor, ControlNetApplyAdvanced, SetUnionControlNetType, AIO_Preprocessor, ControlNetApplyAdvanced, CLIPTextEncode, CLIPTextEncode, ControlNetLoader, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ControlNetLoader, VAEDecode, PreviewImage, SaveImage, PreviewImage, easy cleanGpuUsed, easy cleanGpuUsed, ApplyIPAdapterFlux, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.8000000000000002, "height": 1024, "width": 768}
---

# 图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `BasicScheduler`
- `VAELoader`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `IPAdapterFluxLoader`
- `BasicScheduler`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `IPAdapterFluxLoader`
- `SamplerCustomAdvanced` ★核心
- `ApplyIPAdapterFlux`
- `VAEDecode` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ApplyIPAdapterFlux`
- `RandomNoise`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **96%**（48/50）

**有卡**：`DualCLIPLoader`、`KSamplerSelect`、`FluxGuidance`、`EmptyLatentImage`、`CLIPTextEncode`、`BasicGuider`、`BasicScheduler`、`VAELoader`、`IPAdapterFluxLoader`、`SamplerCustomAdvanced`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ApplyIPAdapterFlux`、`VAEDecode`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`easy cleanGpuUsed`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
