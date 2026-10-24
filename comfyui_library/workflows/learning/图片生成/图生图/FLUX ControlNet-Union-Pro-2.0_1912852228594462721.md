---
key: 图片生成/图生图/FLUX ControlNet-Union-Pro-2.0_1912852228594462721.json
name: FLUX ControlNet-Union-Pro-2.0_1912852228594462721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX ControlNet-Union-Pro-2.0_1912852228594462721.json
hash: 0fcc32d4e4491045
coverage: 0.966667
learned_at: 2026-10-23 10:53:19
nodes: [EmptyLatentImage, BasicGuider, VAEEncode, VAELoader, RandomNoise, KSamplerSelect, easy cleanGpuUsed, CLIPTextEncode, VAEDecode, Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: LoadFlorence2Model, DualCLIPLoader, CLIPTextEncode, String, FluxGuidance, SamplerCustomAdvanced, ControlNetLoader, LayerUtility: Florence2Image2Prompt, JjkShowText, LoadImage, PreviewImage, SetUnionControlNetType, AIO_Preprocessor, BasicScheduler, UNETLoader, ApplyFBCacheOnModel, LoraLoaderModelOnly, ControlNetApplyAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.8000000000000002, "height": 1024, "width": 768}
---

# 图片生成/图生图/FLUX ControlNet-Union-Pro-2.0_1912852228594462721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX ControlNet-Union-Pro-2.0_1912852228594462721.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `EmptyLatentImage` ★核心
- `BasicGuider`
- `VAEEncode` ★核心
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: LoadFlorence2Model`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `String`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `ControlNetLoader`
- `LayerUtility: Florence2Image2Prompt`
- `JjkShowText`
- `LoadImage`
- `PreviewImage`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `BasicScheduler`
- `UNETLoader` ★核心
- `ApplyFBCacheOnModel`
- `LoraLoaderModelOnly` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SaveImage`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`EmptyLatentImage`、`BasicGuider`、`VAEEncode`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`easy cleanGpuUsed`、`CLIPTextEncode`、`VAEDecode`、`Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: LoadFlorence2Model`、`DualCLIPLoader`、`String`、`FluxGuidance`、`SamplerCustomAdvanced`、`ControlNetLoader`、`LayerUtility: Florence2Image2Prompt`、`JjkShowText`、`LoadImage`、`SetUnionControlNetType`、`AIO_Preprocessor`、`BasicScheduler`、`UNETLoader`、`ApplyFBCacheOnModel`、`LoraLoaderModelOnly`、`ControlNetApplyAdvanced`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
