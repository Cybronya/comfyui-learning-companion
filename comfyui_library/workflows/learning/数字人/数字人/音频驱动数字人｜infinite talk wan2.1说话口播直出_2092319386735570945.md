---
key: 数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json
name: 音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json
hash: eb3408d3e5ae2581
coverage: 0.76
learned_at: 2026-10-18 22:17:18
nodes: [GetImageRangeFromBatch, WanVideoEncode, GetImageSizeAndCount, GetNode, GetNode, PreviewAny, SetNode, SetNode, CLIPVisionLoader, SetNode, WanVideoDecode, WanVideoBlockSwap, ImageFromBatch, ColorMatch, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoLoraSelect, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, GetNode, GetNode, INTConstant, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, VHS_LoadVideo, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, INTConstant, PreviewAudio, GetNode, CR Text, WanVideoSampler, WanVideoLoraSelect, WanVideoModelLoader, MultiTalkModelLoader, AudioSeparation, SetNode, LoadImage, LoadAudio, TrimAudioDuration, PreviewAudio, GetNode, SetNode, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
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
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
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

覆盖率 **76%**（57/75）

**有卡**：`GetImageRangeFromBatch`、`WanVideoEncode`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoBlockSwap`、`ImageFromBatch`、`ColorMatch`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`PreviewAudio`、`CR Text`、`WanVideoSampler`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`AudioSeparation`、`LoadImage`、`LoadAudio`、`TrimAudioDuration`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
