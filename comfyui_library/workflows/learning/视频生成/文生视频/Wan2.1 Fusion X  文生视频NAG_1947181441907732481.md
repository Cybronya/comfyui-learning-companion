---
key: 视频生成/文生视频/Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json
name: Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json
hash: c5f5a292c54db712
coverage: 1
learned_at: 2026-10-15 22:43:31
nodes: [WanVideoEnhanceAVideo, WanVideoDecode, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, GIMMVFI_interpolate, ImageScaleToMegapixels, UpscaleModelLoader, WanVideoSLG, WanVideoModelLoader, WanVideoVAELoader, WanVideoSampler, VHS_VideoCombine, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1947181441907732481.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoBlockSwap`
- `GIMMVFI_interpolate`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `WanVideoSLG`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoDecode`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`GIMMVFI_interpolate`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`WanVideoSLG`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、UpscaleModelLoader、UpscaleModelLoader、VHS_VideoCombine
