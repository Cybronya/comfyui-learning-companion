---
key: 视频生成/图生视频/infinitetalk_Wan2.1-单人数字人_1958727770622816258.json
name: infinitetalk_Wan2.1-单人数字人_1958727770622816258.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958727770622816258.json
hash: 0f868d3804454955
coverage: 1
learned_at: 2026-10-15 22:31:22
nodes: [WanVideoBlockSwap, MultiTalkModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CLIPVisionLoader, ImageResizeKJv2, WanVideoClipVisionEncode, WanVideoTextEncode, PreviewAudio, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, ImageSmartSharpen+, WanVideoDecode, easy clearCacheAll, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, Int, CR Text, AudioCrop, easy anythingIndexSwitch, LoadAudio, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoImageToVideoMultiTalk, MathExpression|pysssss, AudioSeparation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, Audio Duration (mtb), LoadImage, CR Text, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/infinitetalk_Wan2.1-单人数字人_1958727770622816258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958727770622816258.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `PreviewAudio`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `ImageSmartSharpen+`
- `WanVideoDecode`
- `easy clearCacheAll`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `Int`
- `CR Text`
- `AudioCrop`
- `easy anythingIndexSwitch`
- `LoadAudio`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoImageToVideoMultiTalk`
- `MathExpression|pysssss`
- `AudioSeparation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `Audio Duration (mtb)`
- `LoadImage`
- `CR Text`
- `Int`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`WanVideoBlockSwap`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`PreviewAudio`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`ImageSmartSharpen+`、`WanVideoDecode`、`easy clearCacheAll`、`WanVideoSampler`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`Int`、`CR Text`、`AudioCrop`、`easy anythingIndexSwitch`、`LoadAudio`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoMultiTalk`、`MathExpression|pysssss`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`Audio Duration (mtb)`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
