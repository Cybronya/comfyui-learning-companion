---
key: 视频生成/图生视频/图生视频+空间or时间放大(LTXVideo 13B 0.9.7)_1920645310174138370.json
name: 图生视频+空间or时间放大(LTXVideo 13B 0.9.7)_1920645310174138370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频+空间or时间放大(LTXVideo 13B 0.9.7)_1920645310174138370.json
hash: d0f023a7f4a08228
coverage: 0.954545
learned_at: 2026-10-15 22:29:42
nodes: [LTXVFilmGrain, BasicScheduler, KSamplerSelect, SplitSigmas, easy showAnything, VAEDecodeTiled, VHS_VideoCombine, STGAdvancedPresets, LTXVLatentUpsampler, VAEDecode, ImageResizeKJ, SplitSigmas, VAEDecodeTiled, STGAdvancedPresets, LTXVAdainLatent, STGGuiderAdvanced, VHS_VideoCombine, LTXVLatentUpsampler, ImageResizeKJ, Set VAE Decoder Noise, RandomNoise, LTXVBaseSampler, LoadImage, PrimitiveNode, LTXVFilmGrain, LTXVTiledSampler, LayerUtility: PurgeVRAM V2, STGGuiderAdvanced, LTXVLatentUpsamplerModelLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, RH_Captioner, LTXVConditioning, LTXQ8Patch, CheckpointLoaderSimple, STGAdvancedPresets, STGGuiderAdvanced, LTXVAdainLatent, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, VHS_VideoCombine, ImageResizeKJv2, JWInteger]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.7-dev.safetensors"}
---

# 视频生成/图生视频/图生视频+空间or时间放大(LTXVideo 13B 0.9.7)_1920645310174138370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1920645310174138370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（44 个）：
- `LTXVFilmGrain`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `easy showAnything`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `STGAdvancedPresets`
- `LTXVLatentUpsampler` ★核心
- `VAEDecode` ★核心
- `ImageResizeKJ`
- `SplitSigmas`
- `VAEDecodeTiled` ★核心
- `STGAdvancedPresets`
- `LTXVAdainLatent`
- `STGGuiderAdvanced`
- `VHS_VideoCombine`
- `LTXVLatentUpsampler` ★核心
- `ImageResizeKJ`
- `Set VAE Decoder Noise`
- `RandomNoise`
- `LTXVBaseSampler` ★核心
- `LoadImage`
- `PrimitiveNode`
- `LTXVFilmGrain`
- `LTXVTiledSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `STGGuiderAdvanced`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `LTXVConditioning`
- `LTXQ8Patch`
- `CheckpointLoaderSimple` ★核心
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `LTXVAdainLatent`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LTXVTiledSampler` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `JWInteger`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.7-dev.safetensors`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`LTXVFilmGrain`、`BasicScheduler`、`KSamplerSelect`、`SplitSigmas`、`VAEDecodeTiled`、`VHS_VideoCombine`、`STGAdvancedPresets`、`LTXVLatentUpsampler`、`VAEDecode`、`ImageResizeKJ`、`LTXVAdainLatent`、`STGGuiderAdvanced`、`Set VAE Decoder Noise`、`RandomNoise`、`LTXVBaseSampler`、`LoadImage`、`LTXVTiledSampler`、`LayerUtility: PurgeVRAM V2`、`LTXVLatentUpsamplerModelLoader`、`CLIPLoader`、`CLIPTextEncode`、`RH_Captioner`、`LTXVConditioning`、`LTXQ8Patch`、`CheckpointLoaderSimple`、`ImageResizeKJv2`、`JWInteger`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、LTXVLatentUpsampler、LTXVBaseSampler
