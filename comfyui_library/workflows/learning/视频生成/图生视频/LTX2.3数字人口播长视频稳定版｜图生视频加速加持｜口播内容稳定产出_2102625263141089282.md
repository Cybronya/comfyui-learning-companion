---
key: 视频生成/图生视频/LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282.json
name: LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282.json
hash: 5b0ee48e91df56f0
coverage: 0.717742
learned_at: 2026-10-17 02:28:52
nodes: [DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, GetNode, GetNode, SamplerCustomAdvanced, RandomNoise, RandomNoise, GetNode, CFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, ManualSigmas, LTXVSeparateAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LatentUpscaleModelLoader, MathExpression|pysssss, SetNode, SetNode, TTResolutionSelector, GetNode, GetNode, MelBandRoFormerModelLoader, SetNode, CLIPTextEncode, VAEDecodeTiled, DiffusionModelLoaderKJ, VHS_VideoCombine, LTX2_NAG, GetNode, CLIPTextEncode, Bool, Int, Int, Float, MathExpression|pysssss, Audio Duration (mtb), AudioCrop, JWString, JWString, LoadAudio, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `DualCLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LatentUpscaleModelLoader`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `TTResolutionSelector`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Bool`
- `Int`
- `Int`
- `Float`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `AudioCrop`
- `JWString`
- `JWString`
- `LoadAudio`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **72%**（89/124）

**有卡**：`DualCLIPLoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`MathExpression|pysssss`、`TTResolutionSelector`、`MelBandRoFormerModelLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`DiffusionModelLoaderKJ`、`VHS_VideoCombine`、`LTX2_NAG`、`Bool`、`Int`、`Float`、`Audio Duration (mtb)`、`AudioCrop`、`JWString`、`LoadAudio`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
