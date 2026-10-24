---
key: 图片生成/图生图/ltx-0.9.8-长视频生成_1947543467977232385.json
name: ltx-0.9.8-长视频生成_1947543467977232385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ltx-0.9.8-长视频生成_1947543467977232385.json
hash: 0226377b9ce36821
coverage: 0.649007
learned_at: 2026-10-23 11:40:56
nodes: [KSamplerSelect, Reroute, Reroute, FloatToSigmas, StringToFloatList, Reroute, STGAdvancedPresets, Reroute, StringToFloatList, STGGuiderAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPLoader, PrintSigmas, FloatToSigmas, Reroute, Reroute, Note, KSamplerSelect, Reroute, Note, LTXVConditioning, STGGuiderAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVLoopingSampler, Reroute, Set VAE Decoder Noise, LTXVTiledVAEDecode, CheckpointLoaderSimple, VHS_VideoCombine, CLIPTextEncode, RH_Translator, PrimitiveInt, Reroute, RH_Captioner, RandomNoise, RandomNoise, easy seed, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVLoopingSampler, LTXVTiledVAEDecode, Set VAE Decoder Noise, VAEEncode, ImageResizeKJ, PrimitiveInt, PreviewImage, VHS_VideoCombine, LoraLoaderModelOnly, LoadImage, GetImageSizeAndCount, VAEDecode, KSamplerSelect, Reroute, Reroute, FloatToSigmas, StringToFloatList, RandomNoise, Reroute, Reroute, STGAdvancedPresets, Set VAE Decoder Noise, Reroute, STGGuiderAdvanced, StringToFloatList, STGGuiderAdvanced, LTXVLoopingSampler, LTXVTiledVAEDecode, Reroute, Reroute, Reroute, LTXVConditioning, CLIPLoader, PrintSigmas, FloatToSigmas, Reroute, Reroute, Note, Reroute, KSamplerSelect, Set VAE Decoder Noise, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, VAEEncode, STGAdvancedPresets, VHS_VideoCombine, RandomNoise, LTXVLatentUpsampler, Reroute, Reroute, Reroute, Reroute, LTXVLoopingSampler, PrimitiveInt, Note, Reroute, Reroute, ImageResizeKJ, PrimitiveInt, LoraLoaderModelOnly, CheckpointLoaderSimple, CLIPTextEncode, LTXVLatentUpsampler, VAEEncode, LTXVConditioning, Reroute, Reroute, Reroute, STGGuiderAdvanced, StringToFloatList, FloatToSigmas, KSamplerSelect, Reroute, Reroute, ImageConcanate, Note, RandomNoise, DWPreprocessor, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPLoader, MultiPromptProvider, easy seed, VHS_LoadVideo, LTXVTiledVAEDecode, LTXVFilmGrain, easy seed, CLIPTextEncode, VHS_VideoCombine, VHS_LoadVideo, LTXVLoopingSampler, LoraLoaderModelOnly, LTXVLatentUpsamplerModelLoader, LTXVLatentUpsamplerModelLoader, LTXVLatentUpsamplerModelLoader, Reroute, VHS_VideoCombine, CLIPTextEncode, MultiPromptProvider, STGAdvancedPresets, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 图片生成/图生图/ltx-0.9.8-长视频生成_1947543467977232385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ltx-0.9.8-长视频生成_1947543467977232385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（151 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `FloatToSigmas`
- `StringToFloatList`
- `Reroute`
- `STGAdvancedPresets`
- `Reroute`
- `StringToFloatList`
- `STGGuiderAdvanced`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `PrintSigmas`
- `FloatToSigmas`
- `Reroute`
- `Reroute`
- `Note`
- `KSamplerSelect` ★核心
- `Reroute`
- `Note`
- `LTXVConditioning`
- `STGGuiderAdvanced`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVLoopingSampler` ★核心
- `Reroute`
- `Set VAE Decoder Noise`
- `LTXVTiledVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `PrimitiveInt`
- `Reroute`
- `RH_Captioner`
- `RandomNoise`
- `RandomNoise`
- `easy seed`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVLoopingSampler` ★核心
- `LTXVTiledVAEDecode` ★核心
- `Set VAE Decoder Noise`
- `VAEEncode` ★核心
- `ImageResizeKJ`
- `PrimitiveInt`
- `PreviewImage`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `GetImageSizeAndCount`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `FloatToSigmas`
- `StringToFloatList`
- `RandomNoise`
- `Reroute`
- `Reroute`
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
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVLoopingSampler` ★核心
- `PrimitiveInt`
- `Note`
- `Reroute`
- `Reroute`
- `ImageResizeKJ`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `VAEEncode` ★核心
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `Reroute`
- `STGGuiderAdvanced`
- `StringToFloatList`
- `FloatToSigmas`
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `ImageConcanate`
- `Note`
- `RandomNoise`
- `DWPreprocessor`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `MultiPromptProvider`
- `easy seed`
- `VHS_LoadVideo`
- `LTXVTiledVAEDecode` ★核心
- `LTXVFilmGrain`
- `easy seed`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LTXVLoopingSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LTXVLatentUpsamplerModelLoader` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `MultiPromptProvider`
- `STGAdvancedPresets`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **65%**（98/151）

**有卡**：`KSamplerSelect`、`FloatToSigmas`、`StringToFloatList`、`STGAdvancedPresets`、`STGGuiderAdvanced`、`CLIPLoader`、`PrintSigmas`、`LTXVConditioning`、`LTXVLoopingSampler`、`Set VAE Decoder Noise`、`LTXVTiledVAEDecode`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`CLIPTextEncode`、`RH_Translator`、`RH_Captioner`、`RandomNoise`、`easy seed`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEEncode`、`ImageResizeKJ`、`LoraLoaderModelOnly`、`LoadImage`、`GetImageSizeAndCount`、`VAEDecode`、`ImageConcanate`、`DWPreprocessor`、`MultiPromptProvider`、`VHS_LoadVideo`、`LTXVFilmGrain`、`LTXVLatentUpsamplerModelLoader`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、LTXVLatentUpsampler
