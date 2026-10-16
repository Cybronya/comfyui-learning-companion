---
key: 视频生成/图生视频/万相win2.1+ VACE首尾帧+accvid加速+2倍补帧流畅  生成最终帧率30，保证流畅_1928305949314793473.json
name: 万相win2.1+ VACE首尾帧+accvid加速+2倍补帧流畅  生成最终帧率30，保证流畅_1928305949314793473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1928305949314793473.json
hash: fb4c008464ad9386
coverage: 0.966667
learned_at: 2026-10-15 22:29:57
nodes: [WanVideoExperimentalArgs, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, LoadImage, LoadImage, ImageResizeKJ, ImageResizeKJ, WanVideoTextEncode, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, WanVideoSLG, WanVideoDecode, LayerUtility: PurgeVRAM V2, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, CR Upscale Image, WanVideoSampler, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, Anything Everywhere3, Int, Int, Int, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/万相win2.1+ VACE首尾帧+accvid加速+2倍补帧流畅  生成最终帧率30，保证流畅_1928305949314793473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1928305949314793473.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `WanVideoSLG`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `CR Upscale Image`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `Anything Everywhere3`
- `Int`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`WanVideoSLG`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`GIMMVFI_interpolate`、`CR Upscale Image`、`WanVideoSampler`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`Int`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
