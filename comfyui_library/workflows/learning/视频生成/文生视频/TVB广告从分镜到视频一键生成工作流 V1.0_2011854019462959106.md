---
key: 视频生成/文生视频/TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106.json
name: TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106.json
hash: 5c96dc3f416d35e9
coverage: 0.761905
learned_at: 2026-10-11 03:07:12
nodes: [DownloadAndLoadTransNetModelXC, CR Text, RH_Nano_Banana2_Image2Image, LoadImage, SaveImage, LoadImage, RHHiddenNodes, TransNetV2_Run, Int, PreviewAny, PreviewAny, DeleteVideoSegmentXC, VideoConcatenatorXC, GetVideoComponents, VHS_LoadVideoPath, VHS_VideoCombine, easy imageConcat, RH_LLMAPI_NODE, PreviewImage, RH_Sora2_I2V, SaveVideo]
patterns: []
missing: [CR Text, easy imageConcat]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（21 个）：
- `DownloadAndLoadTransNetModelXC`
- `CR Text`
- `RH_Nano_Banana2_Image2Image`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `RHHiddenNodes`
- `TransNetV2_Run`
- `Int`
- `PreviewAny`
- `PreviewAny`
- `DeleteVideoSegmentXC`
- `VideoConcatenatorXC`
- `GetVideoComponents`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `easy imageConcat`
- `RH_LLMAPI_NODE`
- `PreviewImage`
- `RH_Sora2_I2V`
- `SaveVideo`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`DownloadAndLoadTransNetModelXC`、`RH_Nano_Banana2_Image2Image`、`LoadImage`、`SaveImage`、`RHHiddenNodes`、`TransNetV2_Run`、`Int`、`DeleteVideoSegmentXC`、`VideoConcatenatorXC`、`GetVideoComponents`、`VHS_LoadVideoPath`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`RH_Sora2_I2V`、`SaveVideo`

**缺卡**（2）：`CR Text`、`easy imageConcat`

**用到的条目**：LoadImage、SaveImage、SaveVideo、GetVideoComponents、Int、RH_LLMAPI_NODE、RHHiddenNodes、VHS_VideoCombine

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
