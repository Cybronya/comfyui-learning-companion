---
key: 视频生成/文生视频/minimax参考输入depth与openpose_2101320036567834625.json
name: minimax参考输入depth与openpose_2101320036567834625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/minimax参考输入depth与openpose_2101320036567834625.json
hash: 5262fb29383f4102
coverage: 0.9
learned_at: 2026-10-11 22:12:49
nodes: [VHS_VideoCombine, VHS_VideoCombine, MuyeImageBlendingMode, VHS_VideoInfo, PreviewAny, VHS_VideoCombine, DepthAnythingV2Preprocessor, DWPreprocessor, VHS_LoadVideo, SaveImage]
patterns: []
missing: []
---

# 视频生成/文生视频/minimax参考输入depth与openpose_2101320036567834625.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/minimax参考输入depth与openpose_2101320036567834625.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MuyeImageBlendingMode`
- `VHS_VideoInfo`
- `PreviewAny`
- `VHS_VideoCombine`
- `DepthAnythingV2Preprocessor`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `SaveImage`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`VHS_VideoCombine`、`MuyeImageBlendingMode`、`VHS_VideoInfo`、`DepthAnythingV2Preprocessor`、`DWPreprocessor`、`VHS_LoadVideo`、`SaveImage`

**用到的条目**：DepthAnythingV2Preprocessor、SaveImage、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo、DWPreprocessor、MuyeImageBlendingMode、sd15-t2i-basic
