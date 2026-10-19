---
key: 数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json
name: infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json
hash: 05212951a52d2b16
coverage: 0.763889
learned_at: 2026-10-18 22:17:13
nodes: [GetImageRangeFromBatch, WanVideoEncode, GetImageSizeAndCount, GetNode, GetNode, PreviewAny, SetNode, SetNode, CLIPVisionLoader, SetNode, WanVideoDecode, WanVideoBlockSwap, ImageFromBatch, ColorMatch, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoLoraSelect, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, GetNode, GetNode, INTConstant, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, VHS_LoadVideo, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, INTConstant, PreviewAudio, GetNode, CR Text, WanVideoSampler, WanVideoLoraSelect, WanVideoModelLoader, MultiTalkModelLoader, AudioSeparation, SetNode, LoadImage, LoadAudio, TrimAudioDuration, PreviewAudio, SetNode, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `ImageFromBatch`
- `ColorMatch`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `VHS_LoadVideo`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `INTConstant`
- `PreviewAudio`
- `GetNode`
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `AudioSeparation`
- `SetNode`
- `LoadImage`
- `LoadAudio`
- `TrimAudioDuration`
- `PreviewAudio`
- `SetNode`
- `VHS_VideoCombine`
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

覆盖率 **76%**（55/72）

**有卡**：`GetImageRangeFromBatch`、`WanVideoEncode`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoBlockSwap`、`ImageFromBatch`、`ColorMatch`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`PreviewAudio`、`CR Text`、`WanVideoSampler`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`AudioSeparation`、`LoadImage`、`LoadAudio`、`TrimAudioDuration`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
