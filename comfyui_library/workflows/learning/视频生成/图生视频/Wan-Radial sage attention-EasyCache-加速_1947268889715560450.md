---
key: 视频生成/图生视频/Wan-Radial sage attention-EasyCache-加速_1947268889715560450.json
name: Wan-Radial sage attention-EasyCache-加速_1947268889715560450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1947268889715560450.json
hash: 3d0b82301e1bb1fc
coverage: 0.914286
learned_at: 2026-10-15 22:30:45
nodes: [WanVideoVACEModelSelect, RH_Captioner, LoadWanVideoT5TextEncoder, WanVideoSetRadialAttention, WanVideoEasyCache, VHS_VideoCombine, WanVideoSampler, WanVideoModelLoader, WanVideoVACEEncode, WanVideoTextEncode, WanVideoEasyCache, WanVideoSampler, WanVideoSetRadialAttention, WanVideoEasyCache, VHS_VideoCombine, WanVideoSampler, WanVideoModelLoader, LayerUtility: PurgeVRAM V2, WanVideoDecode, WanVideoDecode, WanVideoDecode, WanVideoBlockSwap, WanVideoSetRadialAttention, Note, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, WanVideoModelLoader, VHS_VideoCombine, WanVideoLoraSelect, LoadImage, easy seed, WanVideoVAELoader, ImageResizeKJ, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan-Radial sage attention-EasyCache-加速_1947268889715560450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947268889715560450.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoVACEModelSelect`
- `RH_Captioner`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetRadialAttention`
- `WanVideoEasyCache`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`
- `WanVideoEasyCache`
- `WanVideoSampler` ★核心
- `WanVideoSetRadialAttention`
- `WanVideoEasyCache`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `WanVideoDecode`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetRadialAttention`
- `Note`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `LoadImage`
- `easy seed`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `Note`
- `Note`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoVACEModelSelect`、`RH_Captioner`、`LoadWanVideoT5TextEncoder`、`WanVideoSetRadialAttention`、`WanVideoEasyCache`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`WanVideoLoraSelect`、`LoadImage`、`easy seed`、`WanVideoVAELoader`、`ImageResizeKJ`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
