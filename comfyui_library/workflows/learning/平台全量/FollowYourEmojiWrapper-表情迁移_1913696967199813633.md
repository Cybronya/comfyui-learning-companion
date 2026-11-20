---
key: 平台全量/FollowYourEmojiWrapper-表情迁移_1913696967199813633.json
name: FollowYourEmojiWrapper-表情迁移_1913696967199813633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FollowYourEmojiWrapper-表情迁移_1913696967199813633.json
hash: 2b1df55106aac7d9
coverage: 0.941176
learned_at: 2026-11-14 00:30:42
nodes: [ImageResizeKJ, ImageResizeKJ, PreviewImage, FYEMediaPipe, VAELoader, VAEEncode, VHS_VideoCombine, DownloadAndLoadFYEModel, VAEDecode, VHS_VideoCombine, GetImageSizeAndCount, FYESampler, FYECLIPEncode, FYELandmarkEncode, VHS_LoadVideo, FYEMediaPipe, LoadImage]
patterns: []
missing: []
---

# 平台全量/FollowYourEmojiWrapper-表情迁移_1913696967199813633.json

> 来源文件 `comfyui_library/workflows/平台全量/FollowYourEmojiWrapper-表情迁移_1913696967199813633.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ImageResizeKJ`
- `ImageResizeKJ`
- `PreviewImage`
- `FYEMediaPipe`
- `VAELoader`
- `VAEEncode` ★核心
- `VHS_VideoCombine`
- `DownloadAndLoadFYEModel`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `FYESampler` ★核心
- `FYECLIPEncode`
- `FYELandmarkEncode`
- `VHS_LoadVideo`
- `FYEMediaPipe`
- `LoadImage`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`ImageResizeKJ`、`FYEMediaPipe`、`VAELoader`、`VAEEncode`、`VHS_VideoCombine`、`DownloadAndLoadFYEModel`、`VAEDecode`、`GetImageSizeAndCount`、`FYESampler`、`FYECLIPEncode`、`FYELandmarkEncode`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoadImage、FYESampler、VAEEncode、FYECLIPEncode、FYELandmarkEncode、GetImageSizeAndCount
