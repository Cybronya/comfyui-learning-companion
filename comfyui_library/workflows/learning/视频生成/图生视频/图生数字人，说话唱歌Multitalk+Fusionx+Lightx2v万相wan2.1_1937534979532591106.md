---
key: 视频生成/图生视频/图生数字人，说话唱歌Multitalk+Fusionx+Lightx2v万相wan2.1_1937534979532591106.json
name: 图生数字人，说话唱歌Multitalk+Fusionx+Lightx2v万相wan2.1_1937534979532591106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生数字人，说话唱歌Multitalk+Fusionx+Lightx2v万相wan2.1_1937534979532591106.json
hash: 08d97d15564a1924
coverage: 0.875
learned_at: 2026-10-15 22:30:29
nodes: [DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, DownloadAndLoadGIMMVFIModel, SimpleMath+, Audio Duration (mtb), easy showAnything, JWIntegerToString, AudioCrop, easy showAnything, easy showAnything, AudioSeparation, easy cleanGpuUsed, WanVideoDecode, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoTextEncode, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, SimpleMath+, easy showAnything, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoModelLoader, WanVideoVAELoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, TextInput_, PrimitiveFloat, GIMMVFI_interpolate, VHS_VideoCombine, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/图生数字人，说话唱歌Multitalk+Fusionx+Lightx2v万相wan2.1_1937534979532591106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937534979532591106.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `DownloadAndLoadGIMMVFIModel`
- `SimpleMath+`
- `Audio Duration (mtb)`
- `easy showAnything`
- `JWIntegerToString`
- `AudioCrop`
- `easy showAnything`
- `easy showAnything`
- `AudioSeparation`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `SimpleMath+`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `TextInput_`
- `PrimitiveFloat`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`DownloadAndLoadGIMMVFIModel`、`SimpleMath+`、`Audio Duration (mtb)`、`JWIntegerToString`、`AudioCrop`、`AudioSeparation`、`easy cleanGpuUsed`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadAudio`、`TextInput_`、`GIMMVFI_interpolate`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
