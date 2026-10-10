---
key: 视频生成/文生视频/Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698.json
name: Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698.json
hash: 9b27113d1eea4c6e
coverage: 0.833333
learned_at: 2026-10-10 23:08:08
nodes: [SaveVideo, MathExpression|pysssss, Bjornulf_AnythingToText, VHS_SelectImages, VHS_LoadVideoPath, LoadAudio, ShellAgentPluginInputText, SaveImage, PreviewImage, AudioCrop, ShellAgentPluginInputText, RH_Wan25_T2V]
patterns: []
missing: [MathExpression|pysssss]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `SaveVideo`
- `MathExpression|pysssss`
- `Bjornulf_AnythingToText`
- `VHS_SelectImages`
- `VHS_LoadVideoPath`
- `LoadAudio`
- `ShellAgentPluginInputText`
- `SaveImage`
- `PreviewImage`
- `AudioCrop`
- `ShellAgentPluginInputText`
- `RH_Wan25_T2V`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`SaveVideo`、`Bjornulf_AnythingToText`、`VHS_SelectImages`、`VHS_LoadVideoPath`、`LoadAudio`、`ShellAgentPluginInputText`、`SaveImage`、`AudioCrop`、`RH_Wan25_T2V`

**缺卡**（1）：`MathExpression|pysssss`

**用到的条目**：SaveImage、SaveVideo、LoadAudio、AudioCrop、VHS_LoadVideoPath、ShellAgentPluginInputText、Bjornulf_AnythingToText、VHS_SelectImages

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
