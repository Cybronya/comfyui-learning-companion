---
key: 平台全量/人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386.json
name: 人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386.json
hash: 9a403b1d27b7240a
coverage: 1
learned_at: 2026-11-14 01:37:02
nodes: [ImageScale, ImageScale, GetImageSizeAndCount, ImageConcatMulti, GetImageSizeAndCount, ControlNextDiffusersScheduler, ControlNextSampler, DownloadAndLoadControlNeXt, ControlNextDecode, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, ControlNextGetPoses, GetImageSizeAndCount, ImageResize+, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386.json

> 来源文件 `comfyui_library/workflows/平台全量/人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（21 个）：
- `ImageScale`
- `ImageScale`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ControlNextDiffusersScheduler`
- `ControlNextSampler` ★核心
- `DownloadAndLoadControlNeXt`
- `ControlNextDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ControlNextGetPoses`
- `GetImageSizeAndCount`
- `ImageResize+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`ImageScale`、`GetImageSizeAndCount`、`ImageConcatMulti`、`ControlNextDiffusersScheduler`、`ControlNextSampler`、`DownloadAndLoadControlNeXt`、`ControlNextDecode`、`VHS_VideoCombine`、`ControlNextGetPoses`、`ImageResize+`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、ControlNextSampler、ControlNextDecode、GetImageSizeAndCount、ImageResize+、ControlNextDiffusersScheduler、ControlNextGetPoses、DownloadAndLoadControlNeXt
