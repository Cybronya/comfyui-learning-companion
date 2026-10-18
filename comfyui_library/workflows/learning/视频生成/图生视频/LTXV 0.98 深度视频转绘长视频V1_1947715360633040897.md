---
key: 视频生成/图生视频/LTXV 0.98 深度视频转绘长视频V1_1947715360633040897.json
name: LTXV 0.98 深度视频转绘长视频V1_1947715360633040897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTXV 0.98 深度视频转绘长视频V1_1947715360633040897.json
hash: 16f53f8fedadbda4
coverage: 0.631579
learned_at: 2026-10-15 22:30:46
nodes: [VAEDecode, KSamplerSelect, Reroute, Reroute, FloatToSigmas, StringToFloatList, RandomNoise, Reroute, VHS_VideoCombine, STGAdvancedPresets, Set VAE Decoder Noise, Reroute, STGGuiderAdvanced, StringToFloatList, STGGuiderAdvanced, LTXVLoopingSampler, LTXVTiledVAEDecode, Reroute, Reroute, Reroute, LTXVConditioning, CLIPLoader, PrintSigmas, FloatToSigmas, Reroute, Reroute, Note, Reroute, KSamplerSelect, Set VAE Decoder Noise, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, VAEEncode, STGAdvancedPresets, VHS_VideoCombine, RandomNoise, LTXVLatentUpsamplerModelLoader, LTXVLatentUpsampler, Reroute, Reroute, Reroute, LTXVLoopingSampler, PrimitiveInt, PrimitiveInt, Note, GetImageSizeAndCount, Reroute, CheckpointLoaderSimple, Reroute, LoraLoaderModelOnly, Reroute, MultiPromptProvider, Reroute, LoraLoaderModelOnly, VHS_LoadVideo, ImageResizeKJ]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/LTXV 0.98 深度视频转绘长视频V1_1947715360633040897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947715360633040897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `FloatToSigmas`
- `StringToFloatList`
- `RandomNoise`
- `Reroute`
- `VHS_VideoCombine`
- `STGAdvancedPresets`
- `Set VAE Decoder Noise`
- `Reroute`
- `STGGuiderAdvanced`
- `StringToFloatList`
- `STGGuiderAdvanced`
- `LTXVLoopingSampler` ★核心
- `LTXVTiledVAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `CLIPLoader`
- `PrintSigmas`
- `FloatToSigmas`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `KSamplerSelect` ★核心
- `Set VAE Decoder Noise`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `STGAdvancedPresets`
- `VHS_VideoCombine`
- `RandomNoise`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVLoopingSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `Note`
- `GetImageSizeAndCount`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `MultiPromptProvider`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `ImageResizeKJ`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **63%**（36/57）

**有卡**：`VAEDecode`、`KSamplerSelect`、`FloatToSigmas`、`StringToFloatList`、`RandomNoise`、`VHS_VideoCombine`、`STGAdvancedPresets`、`Set VAE Decoder Noise`、`STGGuiderAdvanced`、`LTXVLoopingSampler`、`LTXVTiledVAEDecode`、`LTXVConditioning`、`CLIPLoader`、`PrintSigmas`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`VAEEncode`、`LTXVLatentUpsamplerModelLoader`、`LTXVLatentUpsampler`、`GetImageSizeAndCount`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`MultiPromptProvider`、`VHS_LoadVideo`、`ImageResizeKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、KSamplerSelect、LTXVLatentUpsampler、LTXVLatentUpsamplerModelLoader
