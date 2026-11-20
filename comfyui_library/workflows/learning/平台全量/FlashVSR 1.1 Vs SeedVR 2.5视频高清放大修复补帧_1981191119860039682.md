---
key: 平台全量/FlashVSR 1.1 Vs SeedVR 2.5视频高清放大修复补帧_1981191119860039682.json
name: FlashVSR 1.1 Vs SeedVR 2.5视频高清放大修复补帧_1981191119860039682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FlashVSR 1.1 Vs SeedVR 2.5视频高清放大修复补帧_1981191119860039682.json
hash: f5f3cc798b41a0ea
coverage: 0.866667
learned_at: 2026-11-14 00:26:53
nodes: [DownloadAndLoadGIMMVFIModel, VHS_VideoInfoSource, LayerUtility: PurgeVRAM V2, Any Switch (rgthree), GIMMVFI_interpolate, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel, VHS_LoadVideo, VHS_VideoCombine, Fast Groups Muter (rgthree), FlashVSRNode]
patterns: []
missing: []
---

# 平台全量/FlashVSR 1.1 Vs SeedVR 2.5视频高清放大修复补帧_1981191119860039682.json

> 来源文件 `comfyui_library/workflows/平台全量/FlashVSR 1.1 Vs SeedVR 2.5视频高清放大修复补帧_1981191119860039682.json`

## 结构

**生成流程**：Process → Other

**节点**（15 个）：
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoInfoSource`
- `LayerUtility: PurgeVRAM V2`
- `Any Switch (rgthree)`
- `GIMMVFI_interpolate`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`VHS_VideoInfoSource`、`LayerUtility: PurgeVRAM V2`、`GIMMVFI_interpolate`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`VHS_VideoCombine`、`SeedVR2LoadDiTModel`、`VHS_LoadVideo`、`FlashVSRNode`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、DownloadAndLoadGIMMVFIModel、FlashVSRNode、GIMMVFI_interpolate、LayerUtility: PurgeVRAM V2、VHS_LoadVideo
