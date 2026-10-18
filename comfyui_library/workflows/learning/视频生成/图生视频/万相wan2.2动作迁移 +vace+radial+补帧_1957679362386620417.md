---
key: 视频生成/图生视频/万相wan2.2动作迁移 +vace+radial+补帧_1957679362386620417.json
name: 万相wan2.2动作迁移 +vace+radial+补帧_1957679362386620417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2动作迁移 +vace+radial+补帧_1957679362386620417.json
hash: 67f40257a8eb1d7e
coverage: 1
learned_at: 2026-10-15 22:31:17
nodes: [WanVideoSLG, WanVideoVACEModelSelect, DWPreprocessor, WanVideoLoraSelect, WanVideoExperimentalArgs, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, VHS_VideoCombine, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoTextEncode, VHS_LoadVideo, WanVideoEnhanceAVideo, WanVideoEasyCache, Bjornulf_ShowJson, LoadImage, WanVideoSetRadialAttention, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, WanVideoModelLoader, RH_Captioner, easy clearCacheAll, WanVideoDecode, LayerUtility: PurgeVRAM V2, Int, Int, Int, Int, VHS_VideoCombine, WanVideoSampler, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.2动作迁移 +vace+radial+补帧_1957679362386620417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957679362386620417.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSLG`
- `WanVideoVACEModelSelect`
- `DWPreprocessor`
- `WanVideoLoraSelect`
- `WanVideoExperimentalArgs`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoTextEncode`
- `VHS_LoadVideo`
- `WanVideoEnhanceAVideo`
- `WanVideoEasyCache`
- `Bjornulf_ShowJson`
- `LoadImage`
- `WanVideoSetRadialAttention`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `RH_Captioner`
- `easy clearCacheAll`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `Int`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`WanVideoSLG`、`WanVideoVACEModelSelect`、`DWPreprocessor`、`WanVideoLoraSelect`、`WanVideoExperimentalArgs`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`easy clearCacheAll`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTextEncode`、`VHS_LoadVideo`、`WanVideoEnhanceAVideo`、`WanVideoEasyCache`、`Bjornulf_ShowJson`、`LoadImage`、`WanVideoSetRadialAttention`、`ImageResizeKJv2`、`WanVideoModelLoader`、`RH_Captioner`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`Int`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
