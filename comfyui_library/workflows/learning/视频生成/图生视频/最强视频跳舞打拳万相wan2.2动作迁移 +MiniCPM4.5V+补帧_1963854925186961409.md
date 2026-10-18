---
key: 视频生成/图生视频/最强视频跳舞打拳万相wan2.2动作迁移 +MiniCPM4.5V+补帧_1963854925186961409.json
name: 最强视频跳舞打拳万相wan2.2动作迁移 +MiniCPM4.5V+补帧_1963854925186961409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最强视频跳舞打拳万相wan2.2动作迁移 +MiniCPM4.5V+补帧_1963854925186961409.json
hash: 19086d499f665295
coverage: 1
learned_at: 2026-10-15 22:31:33
nodes: [WanVideoSLG, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoTextEncode, VHS_LoadVideo, WanVideoEasyCache, easy clearCacheAll, Int, Int, Int, VHS_VideoCombine, DWPreprocessor, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, WanVideoDecode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, LoadImage, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, WanVideoModelLoader, Bjornulf_ShowJson, easy cleanGpuUsed, AILab_MiniCPM_4_V, WanVideoSampler, WanVideoBlockSwap, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/最强视频跳舞打拳万相wan2.2动作迁移 +MiniCPM4.5V+补帧_1963854925186961409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963854925186961409.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSLG`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoTextEncode`
- `VHS_LoadVideo`
- `WanVideoEasyCache`
- `easy clearCacheAll`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `Bjornulf_ShowJson`
- `easy cleanGpuUsed`
- `AILab_MiniCPM_4_V`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `Int`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoSLG`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`easy clearCacheAll`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTextEncode`、`VHS_LoadVideo`、`WanVideoEasyCache`、`Int`、`VHS_VideoCombine`、`DWPreprocessor`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`ImageResizeKJv2`、`WanVideoModelLoader`、`Bjornulf_ShowJson`、`easy cleanGpuUsed`、`AILab_MiniCPM_4_V`、`WanVideoSampler`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
