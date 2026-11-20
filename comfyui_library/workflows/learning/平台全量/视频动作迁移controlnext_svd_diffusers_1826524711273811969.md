---
key: 平台全量/视频动作迁移controlnext_svd_diffusers_1826524711273811969.json
name: 视频动作迁移controlnext_svd_diffusers_1826524711273811969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频动作迁移controlnext_svd_diffusers_1826524711273811969.json
hash: 09c717eeabb65baa
coverage: 0.935484
learned_at: 2026-11-14 02:35:46
nodes: [ImageScale, GetImageSizeAndCount, ControlNextSampler, DownloadAndLoadControlNeXt, ControlNextDecode, ImageScale, ControlNextDiffusersScheduler, Display Int (rgthree), Display Int (rgthree), PreviewImage, GetImageSizeAndCount, Display Int (rgthree), Display Int (rgthree), ImageResize+, Display Int (rgthree), Display Int (rgthree), GetImageSizeAndCount, ControlNextGetPoses, GetImageSizeAndCount, ImageConcatMulti, GetImageSizeAndCount, LoadImage, VHS_LoadVideo, ImageConcatMulti, Note, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/视频动作迁移controlnext_svd_diffusers_1826524711273811969.json

> 来源文件 `comfyui_library/workflows/平台全量/视频动作迁移controlnext_svd_diffusers_1826524711273811969.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（31 个）：
- `ImageScale`
- `GetImageSizeAndCount`
- `ControlNextSampler` ★核心
- `DownloadAndLoadControlNeXt`
- `ControlNextDecode`
- `ImageScale`
- `ControlNextDiffusersScheduler`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `PreviewImage`
- `GetImageSizeAndCount`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `ImageResize+`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `GetImageSizeAndCount`
- `ControlNextGetPoses`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `LoadImage`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`ImageScale`、`GetImageSizeAndCount`、`ControlNextSampler`、`DownloadAndLoadControlNeXt`、`ControlNextDecode`、`ControlNextDiffusersScheduler`、`Display Int (rgthree)`、`ImageResize+`、`ControlNextGetPoses`、`ImageConcatMulti`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：LoadImage、ControlNextSampler、ControlNextDecode、GetImageSizeAndCount、ImageResize+、ControlNextDiffusersScheduler、ControlNextGetPoses、Display Int (rgthree)
