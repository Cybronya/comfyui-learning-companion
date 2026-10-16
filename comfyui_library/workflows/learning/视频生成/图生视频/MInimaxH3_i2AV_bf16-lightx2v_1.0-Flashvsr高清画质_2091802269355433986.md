---
key: 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986.json
name: MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986.json
hash: 1dece24d8ca74998
coverage: 0.967742
learned_at: 2026-10-16 22:30:34
nodes: [KSamplerSelect, BasicGuider, SamplerCustomAdvanced, BasicScheduler, VAEDecode, VAEDecodeAudio, EnhancedLoadDiffusionModel, MiniMaxH3ImageToVideo, ComfyMathExpression, CLIPLoader, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, FlashVSR_SM_KSampler, JWInteger, GetImageRangeFromBatch, LayerUtility: PurgeVRAM V2, DF_Get_image_size, FlashVSR_SM_Model, VHS_VideoCombine, RandomNoise, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, AnyBooleanSwitch, PrimitiveFloat, Int, LayerUtility: ImageScaleByAspectRatio V2, Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 273607961}
---

# 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（31 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `EnhancedLoadDiffusionModel`
- `MiniMaxH3ImageToVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `FlashVSR_SM_KSampler` ★核心
- `JWInteger`
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `DF_Get_image_size`
- `FlashVSR_SM_Model`
- `VHS_VideoCombine`
- `RandomNoise`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AnyBooleanSwitch`
- `PrimitiveFloat`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `273607961`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`EnhancedLoadDiffusionModel`、`MiniMaxH3ImageToVideo`、`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`FlashVSR_SM_KSampler`、`JWInteger`、`GetImageRangeFromBatch`、`LayerUtility: PurgeVRAM V2`、`DF_Get_image_size`、`FlashVSR_SM_Model`、`VHS_VideoCombine`、`RandomNoise`、`LayerUtility: ImageScaleByAspectRatio V2`、`AnyBooleanSwitch`、`Int`、`Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、FlashVSR_SM_KSampler、VAEDecodeAudio
