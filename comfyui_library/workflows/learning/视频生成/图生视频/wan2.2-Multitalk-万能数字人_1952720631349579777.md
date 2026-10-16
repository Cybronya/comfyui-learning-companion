---
key: 视频生成/图生视频/wan2.2-Multitalk-万能数字人_1952720631349579777.json
name: wan2.2-Multitalk-万能数字人_1952720631349579777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952720631349579777.json
hash: 91020a4e4d767beb
coverage: 0.921053
learned_at: 2026-10-15 22:31:03
nodes: [InversionDemoLazyIndexSwitch, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, WanVideoModelLoader, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, WanVideoTextEncode, easy cleanGpuUsed, WanVideoDecode, VHS_VideoCombine, WanVideoImageToVideoEncode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, WanVideoVAELoader, MathExpression|pysssss, AudioSeparation, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, LoadImage, Note, LoadAudio, AudioCrop, Int, CR Text, CR Text, Audio Duration (mtb), PreviewAudio, Note, WanVideoClipVisionEncode, WanVideoSampler, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Multitalk-万能数字人_1952720631349579777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952720631349579777.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
- `InversionDemoLazyIndexSwitch`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `AudioSeparation`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `LoadImage`
- `Note`
- `LoadAudio`
- `AudioCrop`
- `Int`
- `CR Text`
- `CR Text`
- `Audio Duration (mtb)`
- `PreviewAudio`
- `Note`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心

## 知识

覆盖率 **92%**（35/38）

**有卡**：`InversionDemoLazyIndexSwitch`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`MathExpression|pysssss`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`LoadImage`、`LoadAudio`、`AudioCrop`、`Int`、`CR Text`、`Audio Duration (mtb)`、`PreviewAudio`、`WanVideoClipVisionEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
