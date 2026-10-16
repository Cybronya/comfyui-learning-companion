---
key: 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610.json
name: MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610.json
hash: c2f2a04329a7e27f
coverage: 1
learned_at: 2026-10-16 21:27:39
nodes: [RandomNoise, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, EnhancedLoadDiffusionModel, VAELoader, LoraLoaderBypassModelOnly, Int, VAEDecode, VAEDecodeAudio, FlashVSR_SM_KSampler, JWInteger, FlashVSR_SM_Model, LayerUtility: PurgeVRAM V2, DF_Get_image_size, VHS_VideoCombine, VHS_VideoCombine, GetImageRangeFromBatch, RHHiddenNodes, LoadImage, Text]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 122473925}
---

# 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（27 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `EnhancedLoadDiffusionModel`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `Int`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `FlashVSR_SM_KSampler` ★核心
- `JWInteger`
- `FlashVSR_SM_Model`
- `LayerUtility: PurgeVRAM V2`
- `DF_Get_image_size`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `RHHiddenNodes`
- `LoadImage`
- `Text`

## 关键参数

- `seed` = `1280`
- `steps` = `122473925`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ImageToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`EnhancedLoadDiffusionModel`、`LoraLoaderBypassModelOnly`、`Int`、`VAEDecode`、`VAEDecodeAudio`、`FlashVSR_SM_KSampler`、`JWInteger`、`FlashVSR_SM_Model`、`LayerUtility: PurgeVRAM V2`、`DF_Get_image_size`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`RHHiddenNodes`、`LoadImage`、`Text`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、FlashVSR_SM_KSampler、VAEDecodeAudio
