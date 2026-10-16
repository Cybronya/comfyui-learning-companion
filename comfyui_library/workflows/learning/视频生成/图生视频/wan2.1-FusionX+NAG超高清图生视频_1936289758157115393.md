---
key: 视频生成/图生视频/wan2.1-FusionX+NAG超高清图生视频_1936289758157115393.json
name: wan2.1-FusionX+NAG超高清图生视频_1936289758157115393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1936289758157115393.json
hash: 09eb6d0977c04203
coverage: 0.909091
learned_at: 2026-10-15 22:30:25
nodes: [WanVideoSampler, WanVideoDecode, WanVideoVAELoader, WanVideoEnhanceAVideo, ImageResizeKJ, WanVideoSLG, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageScaleToMegapixels, UpscaleModelLoader, PreviewImage, VHS_VideoCombine, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, Note Plus (mtb), MarkdownNote, LoadImage, WanVideoBlockSwap, WanVideoApplyNAG, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-FusionX+NAG超高清图生视频_1936289758157115393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936289758157115393.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（22 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `ImageResizeKJ`
- `WanVideoSLG`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `Note Plus (mtb)`
- `MarkdownNote`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoApplyNAG`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`ImageResizeKJ`、`WanVideoSLG`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`VHS_VideoCombine`、`WanVideoTextEncodeSingle`、`Note Plus (mtb)`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、UpscaleModelLoader
