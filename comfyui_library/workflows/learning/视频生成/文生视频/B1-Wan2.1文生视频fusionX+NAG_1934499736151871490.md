---
key: 视频生成/文生视频/B1-Wan2.1文生视频fusionX+NAG_1934499736151871490.json
name: B1-Wan2.1文生视频fusionX+NAG_1934499736151871490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/B1-Wan2.1文生视频fusionX+NAG_1934499736151871490.json
hash: 81e2b9bd6e6b06bb
coverage: 1
learned_at: 2026-10-15 22:43:27
nodes: [WanVideoDecode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, WanVideoEnhanceAVideo, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoSLG, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncodeSingle, WanVideoModelLoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoTextEncodeSingle]
patterns: []
missing: []
---

# 视频生成/文生视频/B1-Wan2.1文生视频fusionX+NAG_1934499736151871490.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1934499736151871490.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（15 个）：
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `WanVideoEnhanceAVideo`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `WanVideoSLG`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTextEncodeSingle`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeSingle`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoDecode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`WanVideoEnhanceAVideo`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`WanVideoSLG`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncodeSingle`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader
