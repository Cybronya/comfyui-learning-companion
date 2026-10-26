---
key: 图片生成/反推提示词/LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305.json
name: LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305.json
hash: 22db4a31cc476975
coverage: 0.918182
learned_at: 2026-10-26 01:45:32
nodes: [CFGGuider, LTXVSeparateAVLatent, ImageScaleBy, CFGGuider, easy cleanGpuUsed, KSamplerSelect, KSamplerSelect, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, easy cleanGpuUsed, easy cleanGpuUsed, RandomNoise, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConcatAVLatent, easy cleanGpuUsed, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, RandomNoise, SaveAudio, GetImageSize, CR Text Concatenate, ttN concat, easy convertAnything, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, RH_LLMAPI_NODE, Display Any (rgthree), CR Text Concatenate, CR Text, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, ManualSigmas, ImpactSwitch, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, UNETLoader, VRAMReserver, LTXVConditioning, SamplerCustomAdvanced, LTX2_NAG, CR String To Combo, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, LTXVScheduler, ManualSigmas, ManualSigmas, SamplerCustomAdvanced, Int, Int, Int, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text, ImpactSwitch, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-distilled.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `CFGGuider`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `PIP_IntegerCalculator`
- `Int`
- `PIP_IntegerCalculator`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `RandomNoise`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `SaveAudio`
- `GetImageSize`
- `CR Text Concatenate`
- `ttN concat`
- `easy convertAnything`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_NODE`
- `Display Any (rgthree)`
- `CR Text Concatenate`
- `CR Text`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `ImpactSwitch`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `VRAMReserver`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `CR String To Combo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `Int`
- `Int`
- `Int`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `ImpactSwitch`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（101/110）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`ImageScaleBy`、`easy cleanGpuUsed`、`KSamplerSelect`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SaveAudio`、`GetImageSize`、`CR Text Concatenate`、`ttN concat`、`easy convertAnything`、`CR Text`、`RH_LLMAPI_NODE`、`Display Any (rgthree)`、`LTXVLatentUpsampler`、`ManualSigmas`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`VRAMReserver`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTX2_NAG`、`CR String To Combo`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVScheduler`、`KSampler`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`VAELoader`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
