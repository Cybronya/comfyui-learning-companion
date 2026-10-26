---
key: 数字人/数字人/LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105.json
name: LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105.json
hash: f8d1ef9b2e279f11
coverage: 0.911392
learned_at: 2026-10-26 22:10:17
nodes: [MathExpression|pysssss, StringFunction|pysssss, ShowText|pysssss, DualCLIPLoader, LTX2_NAG, VAELoader, LTX2SamplingPreviewOverride, CLIPTextEncode, KSamplerSelect, ModelSamplingSD3, VAELoaderKJ, ImageResizeKJv2, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, VisualizeSigmasKJ, AILab_QwenVL_Advanced, Int, UNETLoader, Int, VAELoaderKJ, ConditioningZeroOut, LTXVConditioning, SamplerCustom, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, JjkText, JjkText, Int, BasicScheduler, CLIPTextEncode, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `MathExpression|pysssss`
- `StringFunction|pysssss`
- `ShowText|pysssss`
- `DualCLIPLoader`
- `LTX2_NAG`
- `VAELoader`
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `VisualizeSigmasKJ`
- `AILab_QwenVL_Advanced`
- `Int`
- `UNETLoader` ★核心
- `Int`
- `VAELoaderKJ`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `JjkText`
- `JjkText`
- `Int`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
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

覆盖率 **91%**（72/79）

**有卡**：`MathExpression|pysssss`、`StringFunction|pysssss`、`DualCLIPLoader`、`LTX2_NAG`、`VAELoader`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`KSamplerSelect`、`ModelSamplingSD3`、`VAELoaderKJ`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`VisualizeSigmasKJ`、`AILab_QwenVL_Advanced`、`Int`、`UNETLoader`、`ConditioningZeroOut`、`LTXVConditioning`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`BasicScheduler`、`LoadImage`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
