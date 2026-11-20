---
key: 平台全量/视频修复_ 支持SeedVR2.5,FlashVSR_2021143685181739010.json
name: 视频修复_ 支持SeedVR2.5,FlashVSR_2021143685181739010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频修复_ 支持SeedVR2.5,FlashVSR_2021143685181739010.json
hash: c1a6953d8d46d014
coverage: 0.481481
learned_at: 2026-11-14 02:35:24
nodes: [Reroute, Reroute, Reroute, Note, SetNode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Reroute, VHS_VideoInfo, ImageScaleToTotalPixels, Note, SeedVR2VideoUpscaler, Reroute, Reroute, Reroute, Reroute, Note, VHS_VideoCombine, Note, JWInteger, INTConstant, FlashVSRNode, VHS_VideoInfo, VHS_LoadVideo, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频修复_ 支持SeedVR2.5,FlashVSR_2021143685181739010.json

> 来源文件 `comfyui_library/workflows/平台全量/视频修复_ 支持SeedVR2.5,FlashVSR_2021143685181739010.json`

## 结构

**生成流程**：Process → Other

**节点**（27 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `SetNode`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Reroute`
- `VHS_VideoInfo`
- `ImageScaleToTotalPixels`
- `Note`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `JWInteger`
- `INTConstant`
- `FlashVSRNode`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `VHS_LoadVideo`

## 知识

覆盖率 **48%**（13/27）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VHS_VideoInfo`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`VHS_VideoCombine`、`JWInteger`、`INTConstant`、`FlashVSRNode`、`VHS_LoadVideo`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、FlashVSRNode、ImageScaleToTotalPixels、INTConstant、JWInteger、VHS_LoadVideo
