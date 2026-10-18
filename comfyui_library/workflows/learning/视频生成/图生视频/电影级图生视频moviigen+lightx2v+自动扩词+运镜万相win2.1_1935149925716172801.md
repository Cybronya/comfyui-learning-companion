---
key: 视频生成/图生视频/电影级图生视频moviigen+lightx2v+自动扩词+运镜万相win2.1_1935149925716172801.json
name: 电影级图生视频moviigen+lightx2v+自动扩词+运镜万相win2.1_1935149925716172801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电影级图生视频moviigen+lightx2v+自动扩词+运镜万相win2.1_1935149925716172801.json
hash: e8373854cc0114f1
coverage: 1
learned_at: 2026-10-15 22:30:20
nodes: [WanVideoEnhanceAVideo, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, JWInteger, WanVideoBlockSwap, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoLoraSelect, LayerUtility: PurgeVRAM V2, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, RH_OneShot_Prompter, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, JWInteger, WanVideoModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, SimpleMath+, LoadImage, Text Multiline, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, WanVideoSampler, WanVideoMagCache, VHS_VideoCombine, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/电影级图生视频moviigen+lightx2v+自动扩词+运镜万相win2.1_1935149925716172801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935149925716172801.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `JWInteger`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `RH_OneShot_Prompter`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `JWInteger`
- `WanVideoModelLoader`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `SimpleMath+`
- `LoadImage`
- `Text Multiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoMagCache`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`JWInteger`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`LayerUtility: PurgeVRAM V2`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`RH_OneShot_Prompter`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`WanVideoModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`SimpleMath+`、`LoadImage`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoMagCache`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
