---
key: 视频生成/文生视频/【文生3D人物动作】混元Motion1.0_2007873904911585282.json
name: 【文生3D人物动作】混元Motion1.0_2007873904911585282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【文生3D人物动作】混元Motion1.0_2007873904911585282.json
hash: 11aa675fa94b1180
coverage: 0.769231
learned_at: 2026-10-11 03:07:14
nodes: [HYMotionEncodeText, HYMotionLoadLLM, HYMotionGenerate, HYMotionLoadNetwork, easy saveText, Float, VHS_VideoCombine, HYMotionExportFBX, Note, Note, HYMotionPreview, HYMotionPreviewAnimation, RH_Translator]
patterns: []
missing: [easy saveText]
discoveries: [次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/【文生3D人物动作】混元Motion1.0_2007873904911585282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【文生3D人物动作】混元Motion1.0_2007873904911585282.json`

## 结构

**生成流程**：Output → Other

**节点**（13 个）：
- `HYMotionEncodeText`
- `HYMotionLoadLLM`
- `HYMotionGenerate`
- `HYMotionLoadNetwork`
- `easy saveText`
- `Float`
- `VHS_VideoCombine`
- `HYMotionExportFBX`
- `Note`
- `Note`
- `HYMotionPreview`
- `HYMotionPreviewAnimation`
- `RH_Translator`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`HYMotionEncodeText`、`HYMotionLoadLLM`、`HYMotionGenerate`、`HYMotionLoadNetwork`、`Float`、`VHS_VideoCombine`、`HYMotionExportFBX`、`HYMotionPreview`、`HYMotionPreviewAnimation`、`RH_Translator`

**缺卡**（1）：`easy saveText`

**用到的条目**：HYMotionEncodeText、HYMotionPreview、HYMotionPreviewAnimation、RH_Translator、VHS_VideoCombine、Float、HYMotionExportFBX、HYMotionGenerate

## 学习发现

- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
