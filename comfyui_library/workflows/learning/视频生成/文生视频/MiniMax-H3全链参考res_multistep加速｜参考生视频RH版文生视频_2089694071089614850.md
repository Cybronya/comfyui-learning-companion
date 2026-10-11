---
key: 视频生成/文生视频/MiniMax-H3全链参考res_multistep加速｜参考生视频RH版文生视频_2089694071089614850.json
name: MiniMax-H3全链参考res_multistep加速｜参考生视频RH版文生视频_2089694071089614850
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全链参考res_multistep加速｜参考生视频RH版文生视频_2089694071089614850.json
hash: b25c64148ff64753
coverage: 0.929577
learned_at: 2026-10-11 21:19:46
nodes: [RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VAVAELoader, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAVideoReference, RHMiniMaxH3Ref2VAAudioReference, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3DecodeAV, CreateVideo, SaveVideo, LoadImage, LoadImage, LoadVideo, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VAEncode, LoadAudio, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax-H3全链参考res_multistep加速｜参考生视频RH版文生视频_2089694071089614850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全链参考res_multistep加速｜参考生视频RH版文生视频_2089694071089614850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAVideoReference`
- `RHMiniMaxH3Ref2VAAudioReference`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3DualSigmaSampler` ★核心
- `RHMiniMaxH3DecodeAV`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VAEncode`
- `LoadAudio`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **93%**（66/71）

**有卡**：`RHMiniMaxH3Ref2VATextEncoderLoader`、`RHMiniMaxH3Ref2VAModelLoader`、`RHMiniMaxH3Ref2VAVAELoader`、`RHMiniMaxH3Ref2VAImageReference`、`RHMiniMaxH3Ref2VAVideoReference`、`RHMiniMaxH3Ref2VAAudioReference`、`RHMiniMaxH3EmptyAVLatent`、`RHMiniMaxH3DualSigmaSampler`、`RHMiniMaxH3DecodeAV`、`CreateVideo`、`SaveVideo`、`LoadImage`、`LoadVideo`、`RHMiniMaxH3Ref2VATarget`、`RHMiniMaxH3Ref2VAEncode`、`LoadAudio`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
