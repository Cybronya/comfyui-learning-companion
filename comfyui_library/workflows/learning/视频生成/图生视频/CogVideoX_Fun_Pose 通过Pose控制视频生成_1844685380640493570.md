---
key: 视频生成/图生视频/CogVideoX_Fun_Pose 通过Pose控制视频生成_1844685380640493570.json
name: CogVideoX_Fun_Pose 通过Pose控制视频生成_1844685380640493570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1844685380640493570.json
hash: 8644cdcb9561928d
coverage: 1
learned_at: 2026-10-15 22:29:14
nodes: [WidgetToString, AddLabel, VHS_VideoCombine, DownloadAndLoadCogVideoModel, CogVideoDecode, CogVideoTextEncode, INTConstant, DWPreprocessor, ImageResizeKJ, GetImageSizeAndCount, CogVideoImageEncode, CogVideoSampler, ImageConcatMulti, CLIPLoader, VHS_LoadVideo, CogVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/CogVideoX_Fun_Pose 通过Pose控制视频生成_1844685380640493570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1844685380640493570.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WidgetToString`
- `AddLabel`
- `VHS_VideoCombine`
- `DownloadAndLoadCogVideoModel`
- `CogVideoDecode`
- `CogVideoTextEncode`
- `INTConstant`
- `DWPreprocessor`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `CogVideoImageEncode`
- `CogVideoSampler` ★核心
- `ImageConcatMulti`
- `CLIPLoader`
- `VHS_LoadVideo`
- `CogVideoTextEncode`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WidgetToString`、`AddLabel`、`VHS_VideoCombine`、`DownloadAndLoadCogVideoModel`、`CogVideoDecode`、`CogVideoTextEncode`、`INTConstant`、`DWPreprocessor`、`ImageResizeKJ`、`GetImageSizeAndCount`、`CogVideoImageEncode`、`CogVideoSampler`、`ImageConcatMulti`、`CLIPLoader`、`VHS_LoadVideo`

**用到的条目**：CLIPLoader、CogVideoSampler、CogVideoDecode、CogVideoImageEncode、CogVideoTextEncode、GetImageSizeAndCount、ImageResizeKJ、AddLabel
