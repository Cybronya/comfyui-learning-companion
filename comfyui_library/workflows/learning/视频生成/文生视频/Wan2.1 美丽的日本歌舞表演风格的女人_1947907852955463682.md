---
key: 视频生成/文生视频/Wan2.1 美丽的日本歌舞表演风格的女人_1947907852955463682.json
name: Wan2.1 美丽的日本歌舞表演风格的女人_1947907852955463682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 美丽的日本歌舞表演风格的女人_1947907852955463682.json
hash: 73220c5a3bc8c8fe
coverage: 0.947368
learned_at: 2026-10-15 22:43:32
nodes: [WanVideoSLG, LoadWanVideoT5TextEncoder, DownloadAndLoadGIMMVFIModel, WanVideoDecode, GIMMVFI_interpolate, WanVideoBlockSwap, ImageScaleToMegapixels, Fast Groups Bypasser (rgthree), VHS_VideoCombine, UpscaleModelLoader, WanVideoEnhanceAVideo, WanVideoVAELoader, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncodeSingle]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 美丽的日本歌舞表演风格的女人_1947907852955463682.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1947907852955463682.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoSLG`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `WanVideoBlockSwap`
- `ImageScaleToMegapixels`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeSingle`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`GIMMVFI_interpolate`、`WanVideoBlockSwap`、`ImageScaleToMegapixels`、`VHS_VideoCombine`、`UpscaleModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect、UpscaleModelLoader、UpscaleModelLoader
