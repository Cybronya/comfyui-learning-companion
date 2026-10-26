---
key: 图片生成/反推提示词/复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442.json
name: 复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442.json
hash: 99d8bcc601245b68
coverage: 0.928571
learned_at: 2026-10-26 01:48:00
nodes: [WanVideoSLG, WanVideoEnhanceAVideo, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, JWInteger, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SimpleMath+, WanVideoDecode, SeedVR2BlockSwap, SeedVR2GGUF, VHS_VideoCombine, WanVideoExperimentalArgs, WanVideoEmptyEmbeds, VHS_VideoCombine, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, CR Text, RHHiddenNodes, WanVideoModelLoader, WanVideoSampler, PrimitiveString, JWInteger, WanVideoBlockSwap, RHHiddenNodes, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/反推提示词/复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（28 个）：
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `JWInteger`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `WanVideoDecode`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `CR Text`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `PrimitiveString`
- `JWInteger`
- `WanVideoBlockSwap`
- `RHHiddenNodes`
- `WanVideoTextEncode`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`WanVideoSLG`、`WanVideoEnhanceAVideo`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`WanVideoDecode`、`SeedVR2BlockSwap`、`SeedVR2GGUF`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`WanVideoEmptyEmbeds`、`VHS_LoadVideo`、`CR Text`、`RHHiddenNodes`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoTextEncode`

**用到的条目**：SeedVR2BlockSwap、SeedVR2GGUF、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、RHHiddenNodes
