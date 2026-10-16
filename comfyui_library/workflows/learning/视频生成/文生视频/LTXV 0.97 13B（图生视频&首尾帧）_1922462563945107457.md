---
key: 视频生成/文生视频/LTXV 0.97 13B（图生视频&首尾帧）_1922462563945107457.json
name: LTXV 0.97 13B（图生视频&首尾帧）_1922462563945107457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1922462563945107457.json
hash: a8c88ff75e5ce777
coverage: 0.783133
learned_at: 2026-10-15 22:43:23
nodes: [VAEDecodeTiled, LTXVConditioning, CLIPTextEncode, CLIPLoader, RandomNoise, STGGuiderAdvanced, Note, BasicScheduler, KSamplerSelect, STGAdvancedPresets, RandomNoise, STGGuiderAdvanced, STGAdvancedPresets, Set VAE Decoder Noise, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ImageConcatMulti, VideoCombine_Adv, ImageConcatMulti, AddLabel, AddLabel, EmptyImage, Note, LTXVLatentUpsampler, LTXVAdainLatent, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, SplitSigmas, VAEDecodeTiled, LTXVConditioning, CLIPLoader, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, ImageResizeKJ, CheckpointLoaderSimple, VAEDecode, LTXVFilmGrain, STGGuiderAdvanced, Note, BasicScheduler, KSamplerSelect, LTXVLatentUpsampler, LTXVAdainLatent, Note, RandomNoise, SplitSigmas, Note, STGGuiderAdvanced, STGAdvancedPresets, STGAdvancedPresets, Set VAE Decoder Noise, LTXVBaseSampler, CLIPTextEncode, VHS_VideoCombine, ImageResizeKJ, LTXVFilmGrain, VHS_VideoCombine, Note, Note, Note, Note, Note, Note, LTXVBaseSampler, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, Note, Note, CLIPTextEncode, ImageBatch, LoadImage, LoadImage, CheckpointLoaderSimple, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, RandomNoise, LoadImage, Fast Groups Muter (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.7-dev.safetensors"}
---

# 视频生成/文生视频/LTXV 0.97 13B（图生视频&首尾帧）_1922462563945107457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1922462563945107457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（83 个）：
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `RandomNoise`
- `STGGuiderAdvanced`
- `Note`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `STGAdvancedPresets`
- `RandomNoise`
- `STGGuiderAdvanced`
- `STGAdvancedPresets`
- `Set VAE Decoder Noise`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `VideoCombine_Adv`
- `ImageConcatMulti`
- `AddLabel`
- `AddLabel`
- `EmptyImage`
- `Note`
- `LTXVLatentUpsampler` ★核心
- `LTXVAdainLatent`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LTXVTiledSampler` ★核心
- `SplitSigmas`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `CLIPLoader`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `LTXVTiledSampler` ★核心
- `ImageResizeKJ`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `LTXVFilmGrain`
- `STGGuiderAdvanced`
- `Note`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVAdainLatent`
- `Note`
- `RandomNoise`
- `SplitSigmas`
- `Note`
- `STGGuiderAdvanced`
- `STGAdvancedPresets`
- `STGAdvancedPresets`
- `Set VAE Decoder Noise`
- `LTXVBaseSampler` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `LTXVFilmGrain`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LTXVBaseSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ImageBatch`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LoadImage`
- `Fast Groups Muter (rgthree)`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.7-dev.safetensors`

## 知识

覆盖率 **78%**（65/83）

**有卡**：`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`CLIPLoader`、`RandomNoise`、`STGGuiderAdvanced`、`BasicScheduler`、`KSamplerSelect`、`STGAdvancedPresets`、`Set VAE Decoder Noise`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ImageConcatMulti`、`VideoCombine_Adv`、`AddLabel`、`EmptyImage`、`LTXVLatentUpsampler`、`LTXVAdainLatent`、`LTXVLatentUpsamplerModelLoader`、`LTXVTiledSampler`、`SplitSigmas`、`ImageResizeKJ`、`CheckpointLoaderSimple`、`LTXVFilmGrain`、`LTXVBaseSampler`、`VHS_VideoCombine`、`ImageBatch`、`LoadImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerSelect、LTXVLatentUpsampler
