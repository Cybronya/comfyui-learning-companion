---
key: 平台全量/Infinitetalk_ Video-to-Digital Human – More Dynami_2109809915975004162.json
name: Infinitetalk_ Video-to-Digital Human – More Dynami_2109809915975004162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Infinitetalk_ Video-to-Digital Human – More Dynami_2109809915975004162.json
hash: b68c8249788a7e4c
coverage: 0.933333
learned_at: 2026-11-14 00:32:43
nodes: [MultiTalkModelLoader, WanVideoVAELoader, CLIPVisionLoader, Setter, Setter, Setter, Setter, GetImageRangeFromBatch, WanVideoClipVisionEncode, Getter, Getter, Getter, Getter, Getter, Float to Int, SoundFlow_GetLength, AudioSeparation, AudioCrop, DownloadAndLoadWav2VecModel, WanVideoModelLoader, Setter, Setter, MultiTalkWav2VecEmbeds, SimpleMath+, WanVideoDecode, Reroute, ImageConcanate, VHS_VideoCombine, Getter, WanVideoTextEncodeCached, WanVideoLoraSelect, WanVideoSampler, WanVideoEncode, VHS_VideoCombine, easy cleanGpuUsed, Getter, WanVideoImageToVideoMultiTalk, Getter, WanVideoBlockSwap, ImageResizeKJv2, VHS_LoadVideo, Setter, PrimitiveInt, PrimitiveInt, LoadAudio]
patterns: []
missing: []
---

# 平台全量/Infinitetalk_ Video-to-Digital Human – More Dynami_2109809915975004162.json

> 来源文件 `comfyui_library/workflows/平台全量/Infinitetalk_ Video-to-Digital Human – More Dynami_2109809915975004162.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `Setter`
- `Setter`
- `Setter`
- `Setter`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Float to Int`
- `SoundFlow_GetLength`
- `AudioSeparation`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `WanVideoModelLoader`
- `Setter`
- `Setter`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `WanVideoDecode`
- `Reroute`
- `ImageConcanate`
- `VHS_VideoCombine`
- `Getter`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `Getter`
- `WanVideoImageToVideoMultiTalk`
- `Getter`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `Setter`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadAudio`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`MultiTalkModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`Setter`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`Getter`、`Float to Int`、`SoundFlow_GetLength`、`AudioSeparation`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`SimpleMath+`、`WanVideoDecode`、`ImageConcanate`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoEncode`、`easy cleanGpuUsed`、`WanVideoImageToVideoMultiTalk`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadAudio`

**用到的条目**：WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、CLIPVisionLoader
