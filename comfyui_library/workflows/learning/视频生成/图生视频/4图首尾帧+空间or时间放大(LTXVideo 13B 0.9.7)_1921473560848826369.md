---
key: 视频生成/图生视频/4图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921473560848826369.json
name: 4图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921473560848826369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1921473560848826369.json
hash: 99b1451d671c097e
coverage: 0.981818
learned_at: 2026-10-15 22:29:43
nodes: [VAEDecodeTiled, LTXVConditioning, CLIPTextEncode, ImageResizeKJ, LTXVFilmGrain, STGGuiderAdvanced, BasicScheduler, KSamplerSelect, STGAdvancedPresets, LTXVLatentUpsampler, LTXVAdainLatent, RandomNoise, SplitSigmas, STGGuiderAdvanced, STGAdvancedPresets, ImageResizeKJv2, ImageResizeKJv2, easy int, easy int, ImageResizeKJv2, LTXVLatentUpsamplerModelLoader, Set VAE Decoder Noise, RandomNoise, PrimitiveNode, VAEDecodeTiled, ImageResizeKJ, LTXVLatentUpsampler, LTXVAdainLatent, RandomNoise, SplitSigmas, STGGuiderAdvanced, STGAdvancedPresets, LTXVLatentUpsamplerModelLoader, VHS_VideoCombine, VAEDecode, LayerUtility: PurgeVRAM V2, LTXVTiledSampler, LTXVFilmGrain, LTXVTiledSampler, VHS_VideoCombine, LTXQ8Patch, CheckpointLoaderSimple, ImageBatch, ImageResizeKJv2, ImageBatch, ImageBatch, LoadImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, CLIPLoader, JWInteger, LTXVBaseSampler, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.7-dev.safetensors"}
---

# 视频生成/图生视频/4图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921473560848826369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1921473560848826369.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
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
- `ImageResizeKJv2`
- `easy int`
- `easy int`
- `ImageResizeKJv2`
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
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LTXVTiledSampler` ★核心
- `LTXVFilmGrain`
- `LTXVTiledSampler` ★核心
- `VHS_VideoCombine`
- `LTXQ8Patch`
- `CheckpointLoaderSimple` ★核心
- `ImageBatch`
- `ImageResizeKJv2`
- `ImageBatch`
- `ImageBatch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JWInteger`
- `LTXVBaseSampler` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.7-dev.safetensors`

## 知识

覆盖率 **98%**（54/55）

**有卡**：`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`ImageResizeKJ`、`LTXVFilmGrain`、`STGGuiderAdvanced`、`BasicScheduler`、`KSamplerSelect`、`STGAdvancedPresets`、`LTXVLatentUpsampler`、`LTXVAdainLatent`、`RandomNoise`、`SplitSigmas`、`ImageResizeKJv2`、`easy int`、`LTXVLatentUpsamplerModelLoader`、`Set VAE Decoder Noise`、`VHS_VideoCombine`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`LTXVTiledSampler`、`LTXQ8Patch`、`CheckpointLoaderSimple`、`ImageBatch`、`LoadImage`、`CLIPLoader`、`JWInteger`、`LTXVBaseSampler`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、LTXVLatentUpsampler、LTXVBaseSampler
