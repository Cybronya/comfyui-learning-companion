---
key: 视频生成/文生视频/HY-motion 1.0骨骼动画V1_2007835675105693697.json
name: HY-motion 1.0骨骼动画V1_2007835675105693697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HY-motion 1.0骨骼动画V1_2007835675105693697.json
hash: 6db4572f1fe9ca40
coverage: 0.909091
learned_at: 2026-10-11 03:07:08
nodes: [VHS_VideoCombine, HYMotionLoadNetwork, HYMotionPreview, HYMotionLoadLLM, HYMotionExportFBX, HYMotionGenerate, HYMotionPreviewAnimation, Preview3D, HYMotionEncodeText, CR Prompt Text, Float]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/HY-motion 1.0骨骼动画V1_2007835675105693697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HY-motion 1.0骨骼动画V1_2007835675105693697.json`

## 结构

**生成流程**：Other

**节点**（11 个）：
- `VHS_VideoCombine`
- `HYMotionLoadNetwork`
- `HYMotionPreview`
- `HYMotionLoadLLM`
- `HYMotionExportFBX`
- `HYMotionGenerate`
- `HYMotionPreviewAnimation`
- `Preview3D`
- `HYMotionEncodeText`
- `CR Prompt Text`
- `Float`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VHS_VideoCombine`、`HYMotionLoadNetwork`、`HYMotionPreview`、`HYMotionLoadLLM`、`HYMotionExportFBX`、`HYMotionGenerate`、`HYMotionPreviewAnimation`、`Preview3D`、`HYMotionEncodeText`、`Float`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：HYMotionEncodeText、Preview3D、HYMotionPreview、HYMotionPreviewAnimation、VHS_VideoCombine、Float、HYMotionExportFBX、HYMotionGenerate

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
