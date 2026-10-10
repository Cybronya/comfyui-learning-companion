---
key: FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json
name: FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json
hash: 9349ff5c16fc0253
coverage: 0.88
learned_at: 2026-10-10 20:58:31
nodes: [DualCLIPLoader, KSamplerSelect, FluxGuidance, EmptyLatentImage, CLIPTextEncode, BasicGuider, BasicScheduler, VAELoader, DualCLIPLoader, KSamplerSelect, FluxGuidance, EmptyLatentImage, CLIPTextEncode, BasicGuider, IPAdapterFluxLoader, BasicScheduler, VAELoader, SamplerCustomAdvanced, VAEEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, IPAdapterFluxLoader, SamplerCustomAdvanced, ApplyIPAdapterFlux, VAEDecode, SetUnionControlNetType, AIO_Preprocessor, ControlNetApplyAdvanced, SetUnionControlNetType, AIO_Preprocessor, ControlNetApplyAdvanced, CLIPTextEncode, CLIPTextEncode, ControlNetLoader, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ControlNetLoader, VAEDecode, PreviewImage, SaveImage, PreviewImage, easy cleanGpuUsed, easy cleanGpuUsed, ApplyIPAdapterFlux, RandomNoise]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "controlnet_strength": 0.8000000000000002, "height": 1024, "width": 768}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json

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

覆盖率 **88%**（44/50）

**有卡**：`DualCLIPLoader`、`KSamplerSelect`、`FluxGuidance`、`EmptyLatentImage`、`CLIPTextEncode`、`BasicGuider`、`BasicScheduler`、`VAELoader`、`IPAdapterFluxLoader`、`SamplerCustomAdvanced`、`VAEEncode`、`ApplyIPAdapterFlux`、`VAEDecode`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`RandomNoise`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
