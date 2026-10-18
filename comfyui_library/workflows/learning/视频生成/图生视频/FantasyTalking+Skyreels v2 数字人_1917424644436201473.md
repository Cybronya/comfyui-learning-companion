---
key: 视频生成/图生视频/FantasyTalking+Skyreels v2 数字人_1917424644436201473.json
name: FantasyTalking+Skyreels v2 数字人_1917424644436201473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/FantasyTalking+Skyreels v2 数字人_1917424644436201473.json
hash: 9884cccf869a7b4b
coverage: 0.864865
learned_at: 2026-10-15 22:29:40
nodes: [FantasyTalkingModelLoader, DownloadAndLoadWav2VecModel, CLIPVisionLoader, WanVideoDecode, CreateCFGScheduleFloatList, VHS_VideoInfo, JWFloatToInteger, VHS_LoadVideo, JWFloatToInteger, FantasyTalkingWav2VecEmbeds, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTeaCache, LoadWanVideoT5TextEncoder, Reroute, Fast Groups Bypasser (rgthree), WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoImageToVideoEncode, Reroute, easy cleanGpuUsed, WanVideoSampler, WanVideoModelLoader, DF_Integer, SimpleMath+, DF_Integer, LoadImage, LoadAudio, DF_Integer, DF_Integer, Reroute, Reroute, VHS_VideoCombine, VHS_VideoCombine, ImageConcanate]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyTalking+Skyreels v2 数字人_1917424644436201473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917424644436201473.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `FantasyTalkingModelLoader`
- `DownloadAndLoadWav2VecModel`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `VHS_VideoInfo`
- `JWFloatToInteger`
- `VHS_LoadVideo`
- `JWFloatToInteger`
- `FantasyTalkingWav2VecEmbeds`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `Reroute`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `DF_Integer`
- `SimpleMath+`
- `DF_Integer`
- `LoadImage`
- `LoadAudio`
- `DF_Integer`
- `DF_Integer`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcanate`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`FantasyTalkingModelLoader`、`DownloadAndLoadWav2VecModel`、`CLIPVisionLoader`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`VHS_VideoInfo`、`JWFloatToInteger`、`VHS_LoadVideo`、`FantasyTalkingWav2VecEmbeds`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoModelLoader`、`DF_Integer`、`SimpleMath+`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`ImageConcanate`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
