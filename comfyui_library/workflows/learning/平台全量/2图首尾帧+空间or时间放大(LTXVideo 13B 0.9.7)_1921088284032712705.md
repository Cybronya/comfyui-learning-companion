---
key: 平台全量/2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705.json
name: 2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705.json
hash: 2b31ccd3f9f92638
coverage: 0.979592
learned_at: 2026-11-14 00:11:43
nodes: [VAEDecodeTiled, LTXVConditioning, CLIPTextEncode, ImageResizeKJ, LTXVFilmGrain, STGGuiderAdvanced, BasicScheduler, KSamplerSelect, STGAdvancedPresets, LTXVLatentUpsampler, LTXVAdainLatent, RandomNoise, SplitSigmas, STGGuiderAdvanced, STGAdvancedPresets, ImageResizeKJv2, easy int, easy int, ImageBatch, ImageResizeKJv2, LTXVBaseSampler, LTXVLatentUpsamplerModelLoader, Set VAE Decoder Noise, RandomNoise, PrimitiveNode, VAEDecodeTiled, ImageResizeKJ, LTXVLatentUpsampler, LTXVAdainLatent, RandomNoise, SplitSigmas, STGGuiderAdvanced, STGAdvancedPresets, LTXVLatentUpsamplerModelLoader, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, CLIPTextEncode, CLIPLoader, VAEDecode, LayerUtility: PurgeVRAM V2, JWInteger, LTXVTiledSampler, LTXVFilmGrain, LTXVTiledSampler, LTXQ8Patch, CheckpointLoaderSimple, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.7-dev.safetensors"}
---

# 平台全量/2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705.json

> 来源文件 `comfyui_library/workflows/平台全量/2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `LTXVFilmGrain`
- `STGGuiderAdvanced`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `STGAdvancedPresets`
- `LTXVLatentUpsampler` ★核心
- `LTXVAdainLatent`
- `RandomNoise`
- `SplitSigmas`
- `STGGuiderAdvanced`
- `STGAdvancedPresets`
- `ImageResizeKJv2`
- `easy int`
- `easy int`
- `ImageBatch`
- `ImageResizeKJv2`
- `LTXVBaseSampler` ★核心
- `LTXVLatentUpsamplerModelLoader` ★核心
- `Set VAE Decoder Noise`
- `RandomNoise`
- `PrimitiveNode`
- `VAEDecodeTiled` ★核心
- `ImageResizeKJ`
- `LTXVLatentUpsampler` ★核心
- `LTXVAdainLatent`
- `RandomNoise`
- `SplitSigmas`
- `STGGuiderAdvanced`
- `STGAdvancedPresets`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `JWInteger`
- `LTXVTiledSampler` ★核心
- `LTXVFilmGrain`
- `LTXVTiledSampler` ★核心
- `LTXQ8Patch`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.7-dev.safetensors`

## 知识

覆盖率 **98%**（48/49）

**有卡**：`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`ImageResizeKJ`、`LTXVFilmGrain`、`STGGuiderAdvanced`、`BasicScheduler`、`KSamplerSelect`、`STGAdvancedPresets`、`LTXVLatentUpsampler`、`LTXVAdainLatent`、`RandomNoise`、`SplitSigmas`、`ImageResizeKJv2`、`easy int`、`ImageBatch`、`LTXVBaseSampler`、`LTXVLatentUpsamplerModelLoader`、`Set VAE Decoder Noise`、`VHS_VideoCombine`、`LoadImage`、`CLIPLoader`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`LTXVTiledSampler`、`LTXQ8Patch`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerSelect、LTXVBaseSampler、LTXVLatentUpsampler
