---
key: 图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json
name: z-image-turbo-union2.1控制_2011994282508423170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json
hash: 593578ed651de381
coverage: 0.9
learned_at: 2026-10-19 22:01:15
nodes: [BasicGuider, KSamplerSelect, BasicScheduler, RandomNoise, SamplerCustomAdvanced, VAEDecode, SaveImage, PreviewImage, ModelPatchLoader, LazyCache, QwenImageDiffsynthControlnet, CLIPTextEncode, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveStringMultiline, CLIPLoader, VAELoader, UNETLoader, AIO_Preprocessor]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 2048, "width": 2048}
---

# 图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image-turbo-union2.1控制_2011994282508423170.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `ModelPatchLoader`
- `LazyCache`
- `QwenImageDiffsynthControlnet`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `AIO_Preprocessor`

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ModelPatchLoader`、`LazyCache`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`AIO_Preprocessor`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、QwenImageDiffsynthControlnet
