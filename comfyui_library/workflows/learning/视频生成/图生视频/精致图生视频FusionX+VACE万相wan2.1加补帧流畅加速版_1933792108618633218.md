---
key: 视频生成/图生视频/精致图生视频FusionX+VACE万相wan2.1加补帧流畅加速版_1933792108618633218.json
name: 精致图生视频FusionX+VACE万相wan2.1加补帧流畅加速版_1933792108618633218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1933792108618633218.json
hash: 82b228ef58a3d835
coverage: 1
learned_at: 2026-10-15 22:30:15
nodes: [WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoExperimentalArgs, WanVideoVACEEncode, WanVideoDecode, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, LayerUtility: PurgeVRAM V2, GIMMVFI_interpolate, WanVideoVACEStartToEndFrame, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ImageResizeKJ, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoMagCache, Int, RH_OneShot_Prompter, CR Text, WanVideoSampler, VHS_VideoCombine, LoadImage, Int, Int, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/精致图生视频FusionX+VACE万相wan2.1加补帧流畅加速版_1933792108618633218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933792108618633218.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoExperimentalArgs`
- `WanVideoVACEEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `LayerUtility: PurgeVRAM V2`
- `GIMMVFI_interpolate`
- `WanVideoVACEStartToEndFrame`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJ`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoMagCache`
- `Int`
- `RH_OneShot_Prompter`
- `CR Text`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `Int`
- `Int`
- `WanVideoBlockSwap`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoExperimentalArgs`、`WanVideoVACEEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`LayerUtility: PurgeVRAM V2`、`GIMMVFI_interpolate`、`WanVideoVACEStartToEndFrame`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJ`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoMagCache`、`Int`、`RH_OneShot_Prompter`、`CR Text`、`WanVideoSampler`、`LoadImage`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、WanVideoLoraSelect
