---
key: 视频生成/图生视频/Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289.json
name: Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289.json
hash: 987c6500ae44e242
coverage: 0.925926
learned_at: 2026-10-16 22:30:27
nodes: [RandomNoise, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, EnhancedLoadDiffusionModel, VAELoader, LoraLoaderBypassModelOnly, Int, VAEDecode, VAEDecodeAudio, FlashVSR_SM_KSampler, JWInteger, FlashVSR_SM_Model, LayerUtility: PurgeVRAM V2, DF_Get_image_size, VHS_VideoCombine, VHS_VideoCombine, GetImageRangeFromBatch, RHHiddenNodes, LoadImage, Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（50/54）

**有卡**：`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ImageToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`EnhancedLoadDiffusionModel`、`LoraLoaderBypassModelOnly`、`Int`、`VAEDecode`、`VAEDecodeAudio`、`FlashVSR_SM_KSampler`、`JWInteger`、`FlashVSR_SM_Model`、`LayerUtility: PurgeVRAM V2`、`DF_Get_image_size`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`RHHiddenNodes`、`LoadImage`、`Text`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
