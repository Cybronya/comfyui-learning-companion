---
key: 图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json
name: z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json
hash: d654841f29a0e284
coverage: 0.878788
learned_at: 2026-10-23 11:47:03
nodes: [SeedVR2ExtraArgs, BasicGuider, UpscaleModelLoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, PrimitiveStringMultiline, SeedVR2, PrimitiveStringMultiline, CLIPTextEncode, easy promptConcat, ImageResize+, RandomNoise, KSamplerSelect, VAELoader, SeedVR2BlockSwap, LatentPixelScale, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, VAEEncode, VAEDecode, easy cleanGpuUsed, SamplerCustomAdvanced, PreviewImage, LatentPixelScale, BasicScheduler, LoadImage, Qwen2.5VL, RandomNoise, SaveImage, PlaySound|pysssss, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `SeedVR2ExtraArgs`
- `BasicGuider`
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `SeedVR2`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `easy promptConcat`
- `ImageResize+`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `SeedVR2BlockSwap`
- `LatentPixelScale`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `LatentPixelScale`
- `BasicScheduler`
- `LoadImage`
- `Qwen2.5VL`
- `RandomNoise`
- `SaveImage`
- `PlaySound|pysssss`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`SeedVR2ExtraArgs`、`BasicGuider`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`SeedVR2`、`CLIPTextEncode`、`easy promptConcat`、`ImageResize+`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`SeedVR2BlockSwap`、`LatentPixelScale`、`SamplerCustomAdvanced`、`VAEEncode`、`VAEDecode`、`easy cleanGpuUsed`、`BasicScheduler`、`LoadImage`、`Qwen2.5VL`、`SaveImage`、`PlaySound|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect
