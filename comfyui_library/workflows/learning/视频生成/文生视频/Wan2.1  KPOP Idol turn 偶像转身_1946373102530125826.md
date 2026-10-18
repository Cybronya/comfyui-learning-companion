---
key: 视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json
name: Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json
hash: bd1c25918f0a2b62
coverage: 0.947368
learned_at: 2026-10-15 22:43:31
nodes: [ImageScaleToMegapixels, Fast Groups Bypasser (rgthree), VHS_VideoCombine, UpscaleModelLoader, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoDecode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoEnhanceAVideo, WanVideoVAELoader, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSLG, WanVideoBlockSwap, WanVideoTextEncodeSingle]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1946373102530125826.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `ImageScaleToMegapixels`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`ImageScaleToMegapixels`、`VHS_VideoCombine`、`UpscaleModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoDecode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSLG`、`WanVideoBlockSwap`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect、UpscaleModelLoader、UpscaleModelLoader
