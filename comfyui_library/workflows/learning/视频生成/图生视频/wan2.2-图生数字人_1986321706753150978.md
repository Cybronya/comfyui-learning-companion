---
key: 视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json
name: wan2.2-图生数字人_1986321706753150978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json
hash: c4ddb34285d60420
coverage: 0.979592
learned_at: 2026-10-15 22:32:54
nodes: [MultiTalkModelLoader, Anything Everywhere, WanVideoTextEncodeCached, ImageResizeKJv2, DownloadAndLoadWav2VecModel, WanVideoSampler, WanVideoImageToVideoMultiTalk, CLIPVisionLoader, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, CR Prompt Text, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoEncode, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncodeCached, CLIPVisionLoader, WanVideoEncode, GetImageRangeFromBatch, WanVideoClipVisionEncode, GetImageSizeAndCount, WanVideoImageToVideoMultiTalk, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, LayerUtility: PurgeVRAM, WanVideoSampler, ImageResizeKJv2, AudioSeparation, SoundFlow_TrimAudio, Apply Whisper, RH_GetAudioDuration, VoxCPM_TTS, Float to Int, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, WanVideoDecode, MultiTalkWav2VecEmbeds, WanVideoModelLoader, String Literal, LoadAudio, JWInteger, SimpleMath+, MultiTalkModelLoader, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986321706753150978.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `MultiTalkModelLoader`
- `Anything Everywhere`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `DownloadAndLoadWav2VecModel`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM`
- `CR Prompt Text`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoMultiTalk`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `AudioSeparation`
- `SoundFlow_TrimAudio`
- `Apply Whisper`
- `RH_GetAudioDuration`
- `VoxCPM_TTS`
- `Float to Int`
- `LayerUtility: PurgeVRAM`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoModelLoader`
- `String Literal`
- `LoadAudio`
- `JWInteger`
- `SimpleMath+`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **98%**（48/49）

**有卡**：`MultiTalkModelLoader`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`AudioSeparation`、`SoundFlow_TrimAudio`、`Apply Whisper`、`RH_GetAudioDuration`、`VoxCPM_TTS`、`Float to Int`、`WanVideoModelLoader`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`String Literal`、`LoadAudio`、`JWInteger`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
