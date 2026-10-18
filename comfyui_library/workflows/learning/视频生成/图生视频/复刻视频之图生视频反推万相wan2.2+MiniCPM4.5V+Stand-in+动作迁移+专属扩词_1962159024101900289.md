---
key: 视频生成/图生视频/复刻视频之图生视频反推万相wan2.2+MiniCPM4.5V+Stand-in+动作迁移+专属扩词_1962159024101900289.json
name: 复刻视频之图生视频反推万相wan2.2+MiniCPM4.5V+Stand-in+动作迁移+专属扩词_1962159024101900289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/复刻视频之图生视频反推万相wan2.2+MiniCPM4.5V+Stand-in+动作迁移+专属扩词_1962159024101900289.json
hash: 02f030a929999cad
coverage: 0.954545
learned_at: 2026-10-15 22:31:30
nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, JWInteger, WanVideoDecode, SeedVR2BlockSwap, SeedVR2GGUF, VHS_VideoCombine, WanVideoExperimentalArgs, VHS_VideoCombine, PrimitiveString, CR Text, Primitive integer [Crystools], ShowText|pysssss, JWInteger, VHS_LoadVideo, VHS_VideoCombine, FaceProcessorLoader, ApplyFaceProcessor, WanVideoEncode, DWPreprocessor, ImageResizeKJv2, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoEasyCache, LoadImage, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoVACEEncode, WanVideoLoraSelect, RHHiddenNodes, SimpleMath+, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoAddStandInLatent, LayerUtility: PurgeVRAM V2, WanVideoTextEncode, LayerUtility: PurgeVRAM V2, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/复刻视频之图生视频反推万相wan2.2+MiniCPM4.5V+Stand-in+动作迁移+专属扩词_1962159024101900289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962159024101900289.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `JWInteger`
- `WanVideoDecode`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `PrimitiveString`
- `CR Text`
- `Primitive integer [Crystools]`
- `ShowText|pysssss`
- `JWInteger`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `WanVideoEncode`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoEasyCache`
- `LoadImage`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `RHHiddenNodes`
- `SimpleMath+`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoAddStandInLatent`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`JWInteger`、`WanVideoDecode`、`SeedVR2BlockSwap`、`SeedVR2GGUF`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`CR Text`、`Primitive integer [Crystools]`、`VHS_LoadVideo`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEncode`、`DWPreprocessor`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoEasyCache`、`LoadImage`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoVACEEncode`、`RHHiddenNodes`、`SimpleMath+`、`LayerUtility: PurgeVRAM V2`、`WanVideoAddStandInLatent`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、SeedVR2BlockSwap、SeedVR2GGUF、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
