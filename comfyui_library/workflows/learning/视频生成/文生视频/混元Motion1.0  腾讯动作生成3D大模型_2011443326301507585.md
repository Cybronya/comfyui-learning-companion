---
key: 视频生成/文生视频/混元Motion1.0  腾讯动作生成3D大模型_2011443326301507585.json
name: 混元Motion1.0  腾讯动作生成3D大模型_2011443326301507585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/混元Motion1.0  腾讯动作生成3D大模型_2011443326301507585.json
hash: 6d33699e91c59c85
coverage: 0.769231
learned_at: 2026-10-11 03:07:15
nodes: [HYMotionEncodeText, HYMotionLoadLLM, HYMotionGenerate, HYMotionLoadNetwork, easy saveText, Float, VHS_VideoCombine, HYMotionExportFBX, Note, Note, HYMotionPreview, HYMotionPreviewAnimation, RH_Translator]
patterns: []
missing: [easy saveText]
discoveries: [次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/混元Motion1.0  腾讯动作生成3D大模型_2011443326301507585.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/混元Motion1.0  腾讯动作生成3D大模型_2011443326301507585.json`

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
