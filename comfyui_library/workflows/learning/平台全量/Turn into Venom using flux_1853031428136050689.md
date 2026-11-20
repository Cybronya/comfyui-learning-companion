---
key: 平台全量/Turn into Venom using flux_1853031428136050689.json
name: Turn into Venom using flux_1853031428136050689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Turn into Venom using flux_1853031428136050689.json
hash: bb8b6b45002de0e0
coverage: 0.8125
learned_at: 2026-11-14 01:01:58
nodes: [Reroute, Reroute, EmptySD3LatentImage, CLIPTextEncodeFlux, CLIPTextEncodeFlux, SamplerCustomAdvanced, Reroute, KSamplerSelect, VAEDecode, ImageCompositeMasked, RandomNoise, BasicScheduler, CFGGuider, PreviewImage, ControlNetInpaintingAliMamaApply, MaskToImage, ImageCompositeMasked, SaveImage, Get Image Size, Image Comparer (rgthree), DF_Image_scale_to_side, GrowMaskWithBlur, PreviewImage, easy prompt, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, ControlNetLoader, CheckpointLoaderSimple, LayerMask: PersonMaskUltra V2, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "OpenFlux-fp8.safetensors"}
---

# 平台全量/Turn into Venom using flux_1853031428136050689.json

> 来源文件 `comfyui_library/workflows/平台全量/Turn into Venom using flux_1853031428136050689.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Reroute`
- `Reroute`
- `EmptySD3LatentImage`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `ImageCompositeMasked`
- `RandomNoise`
- `BasicScheduler`
- `CFGGuider`
- `PreviewImage`
- `ControlNetInpaintingAliMamaApply`
- `MaskToImage`
- `ImageCompositeMasked`
- `SaveImage`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `DF_Image_scale_to_side`
- `GrowMaskWithBlur`
- `PreviewImage`
- `easy prompt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`

## 关键参数

- `checkpoint` = `OpenFlux-fp8.safetensors`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`EmptySD3LatentImage`、`CLIPTextEncodeFlux`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecode`、`ImageCompositeMasked`、`RandomNoise`、`BasicScheduler`、`CFGGuider`、`ControlNetInpaintingAliMamaApply`、`MaskToImage`、`SaveImage`、`Get Image Size`、`DF_Image_scale_to_side`、`GrowMaskWithBlur`、`easy prompt`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`ControlNetLoader`、`CheckpointLoaderSimple`、`LayerMask: PersonMaskUltra V2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader、CFGGuider
