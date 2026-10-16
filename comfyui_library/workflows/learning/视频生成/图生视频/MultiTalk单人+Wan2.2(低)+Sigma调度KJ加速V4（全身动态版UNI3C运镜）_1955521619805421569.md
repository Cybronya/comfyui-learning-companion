---
key: 视频生成/图生视频/MultiTalk单人+Wan2.2(低)+Sigma调度KJ加速V4（全身动态版UNI3C运镜）_1955521619805421569.json
name: MultiTalk单人+Wan2.2(低)+Sigma调度KJ加速V4（全身动态版UNI3C运镜）_1955521619805421569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955521619805421569.json
hash: d25c33e0ef000bdb
coverage: 0.80303
learned_at: 2026-10-15 22:31:09
nodes: [DownloadAndLoadWav2VecModel, easy showAnything, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoImageToVideoEncode, Audio Duration (mtb), easy showAnything, AudioSeparation, easy showAnything, SimpleMath+, AudioCrop, JWIntegerToString, CLIPVisionLoader, LayerUtility: PurgeVRAM, JWInteger, PrimitiveFloat, Note, Note, Note, Note, Note, Note, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SimpleMath+, Note, TextInput_, LoadAudio, PrimitiveInt, easy showAnything, MultiTalkModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoLoraSelect, StringToFloatList, FloatToSigmas, VHS_LoadVideo, JWInteger, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, EmptyImage, GetImageSizeAndCount, LoadImage, ColorMatch, LayerUtility: ImageScaleByAspectRatio V2, AddLabel, ImageResizeKJ, AddLabel, VHS_VideoCombine, CreateCFGScheduleFloatList, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, MultiTalkWav2VecEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/MultiTalk单人+Wan2.2(低)+Sigma调度KJ加速V4（全身动态版UNI3C运镜）_1955521619805421569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955521619805421569.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `Audio Duration (mtb)`
- `easy showAnything`
- `AudioSeparation`
- `easy showAnything`
- `SimpleMath+`
- `AudioCrop`
- `JWIntegerToString`
- `CLIPVisionLoader`
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `PrimitiveFloat`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `SimpleMath+`
- `Note`
- `TextInput_`
- `LoadAudio`
- `PrimitiveInt`
- `easy showAnything`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `StringToFloatList`
- `FloatToSigmas`
- `VHS_LoadVideo`
- `JWInteger`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `EmptyImage`
- `GetImageSizeAndCount`
- `LoadImage`
- `ColorMatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AddLabel`
- `ImageResizeKJ`
- `AddLabel`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `MultiTalkWav2VecEmbeds`

## 知识

覆盖率 **80%**（53/66）

**有卡**：`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`Audio Duration (mtb)`、`AudioSeparation`、`SimpleMath+`、`AudioCrop`、`JWIntegerToString`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM`、`JWInteger`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`TextInput_`、`LoadAudio`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`StringToFloatList`、`FloatToSigmas`、`VHS_LoadVideo`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageConcatMulti`、`EmptyImage`、`GetImageSizeAndCount`、`LoadImage`、`ColorMatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`AddLabel`、`ImageResizeKJ`、`easy cleanGpuUsed`、`WanVideoSampler`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
