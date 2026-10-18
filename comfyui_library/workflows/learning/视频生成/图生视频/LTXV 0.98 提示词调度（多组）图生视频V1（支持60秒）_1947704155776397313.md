---
key: 视频生成/图生视频/LTXV 0.98 提示词调度（多组）图生视频V1（支持60秒）_1947704155776397313.json
name: LTXV 0.98 提示词调度（多组）图生视频V1（支持60秒）_1947704155776397313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTXV 0.98 提示词调度（多组）图生视频V1（支持60秒）_1947704155776397313.json
hash: 01d2ccc8d5683100
coverage: 0.622951
learned_at: 2026-10-15 22:30:46
nodes: [KSamplerSelect, Reroute, Reroute, FloatToSigmas, StringToFloatList, RandomNoise, Reroute, STGAdvancedPresets, Set VAE Decoder Noise, Reroute, StringToFloatList, STGGuiderAdvanced, LTXVLoopingSampler, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPLoader, PrintSigmas, Reroute, Reroute, Note, KSamplerSelect, Reroute, VHS_VideoCombine, RandomNoise, Note, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, STGGuiderAdvanced, ImageResizeKJ, VAEEncode, LTXVLatentUpsampler, Reroute, Reroute, Reroute, Reroute, STGAdvancedPresets, Reroute, Reroute, LTXVLoopingSampler, Reroute, Set VAE Decoder Noise, LTXVTiledVAEDecode, LTXVTiledVAEDecode, Reroute, LTXVLatentUpsamplerModelLoader, LoadImage, LoraLoaderModelOnly, CheckpointLoaderSimple, FloatToSigmas, VHS_VideoCombine, MultiPromptProvider, PrimitiveInt, CR Prompt Text, EmptyLTXVLatentVideo, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/LTXV 0.98 提示词调度（多组）图生视频V1（支持60秒）_1947704155776397313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947704155776397313.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `FloatToSigmas`
- `StringToFloatList`
- `RandomNoise`
- `Reroute`
- `STGAdvancedPresets`
- `Set VAE Decoder Noise`
- `Reroute`
- `StringToFloatList`
- `STGGuiderAdvanced`
- `LTXVLoopingSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `PrintSigmas`
- `Reroute`
- `Reroute`
- `Note`
- `KSamplerSelect` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `RandomNoise`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `STGGuiderAdvanced`
- `ImageResizeKJ`
- `VAEEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `STGAdvancedPresets`
- `Reroute`
- `Reroute`
- `LTXVLoopingSampler` ★核心
- `Reroute`
- `Set VAE Decoder Noise`
- `LTXVTiledVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `Reroute`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `FloatToSigmas`
- `VHS_VideoCombine`
- `MultiPromptProvider`
- `PrimitiveInt`
- `CR Prompt Text`
- `EmptyLTXVLatentVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **62%**（38/61）

**有卡**：`KSamplerSelect`、`FloatToSigmas`、`StringToFloatList`、`RandomNoise`、`STGAdvancedPresets`、`Set VAE Decoder Noise`、`STGGuiderAdvanced`、`LTXVLoopingSampler`、`CLIPLoader`、`PrintSigmas`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVConditioning`、`ImageResizeKJ`、`VAEEncode`、`LTXVLatentUpsampler`、`LTXVTiledVAEDecode`、`LTXVLatentUpsamplerModelLoader`、`LoadImage`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`MultiPromptProvider`、`CR Prompt Text`、`EmptyLTXVLatentVideo`、`JWInteger`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、LTXVLatentUpsampler、LTXVLatentUpsamplerModelLoader
