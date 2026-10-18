---
key: 视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json
name: InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json
hash: 944dcb4e4879d0e6
coverage: 0.941176
learned_at: 2026-10-17 01:09:21
nodes: [TDQwen3TTSModelLoader, PreviewAudio, SaveAudioAdvanced, Qwen3TTSCustomVoice, VHS_VideoCombine, SeedVR2BlockSwap, SeedVR2ExtraArgs, ImageScaleToTotalPixels, MultiTalkWav2VecEmbeds, SeedVR2, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, Audio Duration (mtb), MathExpression|pysssss, DownloadAndLoadWav2VecModel, MathExpression|pysssss, AudioCombine, AudioCombine, PreviewAudio, SeedVCRun, AudioSeparation, AudioCrop, AudioCombine, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, MultiTalkModelLoader, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoMultiTalk, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, GetImageRangeFromBatch, WanVideoClipVisionEncode, WanVideoTextEncode, LoadAudio, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `TDQwen3TTSModelLoader`
- `PreviewAudio`
- `SaveAudioAdvanced`
- `Qwen3TTSCustomVoice`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `ImageScaleToTotalPixels`
- `MultiTalkWav2VecEmbeds`
- `SeedVR2`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `DownloadAndLoadWav2VecModel`
- `MathExpression|pysssss`
- `AudioCombine`
- `AudioCombine`
- `PreviewAudio`
- `SeedVCRun`
- `AudioSeparation`
- `AudioCrop`
- `AudioCombine`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `LoadAudio`
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
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **94%**（64/68）

**有卡**：`TDQwen3TTSModelLoader`、`PreviewAudio`、`SaveAudioAdvanced`、`Qwen3TTSCustomVoice`、`VHS_VideoCombine`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`ImageScaleToTotalPixels`、`MultiTalkWav2VecEmbeds`、`SeedVR2`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`DownloadAndLoadWav2VecModel`、`AudioCombine`、`SeedVCRun`、`AudioSeparation`、`AudioCrop`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoMultiTalk`、`WanVideoDecode`、`WanVideoSampler`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
