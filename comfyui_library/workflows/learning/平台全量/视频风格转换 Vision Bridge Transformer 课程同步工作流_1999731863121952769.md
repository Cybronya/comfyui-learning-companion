---
key: 平台全量/视频风格转换 Vision Bridge Transformer 课程同步工作流_1999731863121952769.json
name: 视频风格转换 Vision Bridge Transformer 课程同步工作流_1999731863121952769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频风格转换 Vision Bridge Transformer 课程同步工作流_1999731863121952769.json
hash: 8bbe16553ece0a2f
coverage: 0.413043
learned_at: 2026-11-14 02:42:06
nodes: [ImageResizeKJv2, WanVideoTextEncode, WanVideoSLG, WanVideoSampler, WanVideoDecode, SetNode, GetNode, GetNode, WanVideoEncode, WanVideoEmptyEmbeds, ImageConcatMulti, VHS_VideoCombine, WanVideoContextOptions, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, WanVideoModelLoader, GetNode, WanVideoModelLoader, Note, PrimitiveStringMultiline, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_LoadVideoPath, VHS_LoadVideo, INTConstant, INTConstant]
patterns: []
missing: []
---

# 平台全量/视频风格转换 Vision Bridge Transformer 课程同步工作流_1999731863121952769.json

> 来源文件 `comfyui_library/workflows/平台全量/视频风格转换 Vision Bridge Transformer 课程同步工作流_1999731863121952769.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoModelLoader`
- `Note`
- `PrimitiveStringMultiline`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideoPath`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **41%**（19/46）

**有卡**：`ImageResizeKJv2`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoContextOptions`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`VHS_LoadVideoPath`、`VHS_LoadVideo`、`INTConstant`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJv2、ImageConcatMulti
