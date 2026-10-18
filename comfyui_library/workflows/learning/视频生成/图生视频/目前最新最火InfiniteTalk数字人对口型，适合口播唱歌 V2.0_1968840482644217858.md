---
key: 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json
name: 目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json
hash: ff1fe5327630f205
coverage: 1
learned_at: 2026-10-15 22:31:46
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, AudioSeparation, WanVideoClipVisionEncode, WanVideoTextEncode, MultiTalkModelLoader, WanVideoSampler, WanVideoModelLoader, SimpleMath+, WanVideoLoraSelect, ImageFromBatch+, WanVideoDecode, CLIPVisionLoader, WanVideoImageToVideoMultiTalk, MultiTalkWav2VecEmbeds, SimpleMath+, LoadImage, CR Text, ImageResizeKJv2, VHS_VideoCombine, LoadAudio, AudioCrop, VHS_LoadVideo, VHS_VideoCombine, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoModelLoader, Audio Duration (mtb), AudioSeparation, LoadAudio, AudioCrop, WanVideoVAELoader, CLIPVisionLoader, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, GetImageSizeAndCount, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoDecode, JWInteger, VHS_VideoCombine, VHS_VideoCombine, MultiTalkWav2VecEmbeds, WanVideoTextEncode, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968840482644217858.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（53 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `AudioSeparation`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `MultiTalkModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `ImageFromBatch+`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `LoadImage`
- `CR Text`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadAudio`
- `AudioCrop`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Audio Duration (mtb)`
- `AudioSeparation`
- `LoadAudio`
- `AudioCrop`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTextEncode`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **100%**（53/53）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`AudioSeparation`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`WanVideoSampler`、`WanVideoModelLoader`、`SimpleMath+`、`WanVideoLoraSelect`、`ImageFromBatch+`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`LoadImage`、`CR Text`、`ImageResizeKJv2`、`VHS_VideoCombine`、`LoadAudio`、`AudioCrop`、`VHS_LoadVideo`、`Audio Duration (mtb)`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`GetImageSizeAndCount`、`JWInteger`、`INTConstant`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
