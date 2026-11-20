---
key: 平台全量/视频细节修复和放大： SeedVR2.5+FlashVSR_2063615333767933954.json
name: 视频细节修复和放大： SeedVR2.5+FlashVSR_2063615333767933954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频细节修复和放大： SeedVR2.5+FlashVSR_2063615333767933954.json
hash: 36a1673a7ffd625b
coverage: 0.5
learned_at: 2026-11-14 02:40:26
nodes: [Reroute, Reroute, Note, SetNode, Reroute, ImageScaleToTotalPixels, Reroute, Reroute, Reroute, Reroute, Note, VHS_VideoCombine, Note, JWInteger, VHS_LoadVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_VideoInfo, INTConstant, Note, VHS_VideoCombine, VHS_LoadVideo, FlashVSRNode, VHS_VideoInfo, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 平台全量/视频细节修复和放大： SeedVR2.5+FlashVSR_2063615333767933954.json

> 来源文件 `comfyui_library/workflows/平台全量/视频细节修复和放大： SeedVR2.5+FlashVSR_2063615333767933954.json`

## 结构

**生成流程**：Process → Other

**节点**（26 个）：
- `Reroute`
- `Reroute`
- `Note`
- `SetNode`
- `Reroute`
- `ImageScaleToTotalPixels`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `JWInteger`
- `VHS_LoadVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_VideoInfo`
- `INTConstant`
- `Note`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `FlashVSRNode`
- `VHS_VideoInfo`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **50%**（13/26）

**有卡**：`ImageScaleToTotalPixels`、`VHS_VideoCombine`、`JWInteger`、`VHS_LoadVideo`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VHS_VideoInfo`、`INTConstant`、`FlashVSRNode`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、FlashVSRNode、ImageScaleToTotalPixels、INTConstant、JWInteger、VHS_LoadVideo
