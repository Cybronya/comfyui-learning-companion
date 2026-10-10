---
key: 视频生成/文生视频/seedance2.5(支持30秒长视频)_多模态生视频_2086018514942517249.json
name: seedance2.5(支持30秒长视频)_多模态生视频_2086018514942517249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/seedance2.5(支持30秒长视频)_多模态生视频_2086018514942517249.json
hash: 5e78107dcf57ef63
coverage: 0.857143
learned_at: 2026-10-10 23:09:16
nodes: [LoadImage, RH_BytedanceSeedance25TokenMultimodalVideo, LoadVideo, LoadAudio, CR Text, SaveVideo, LoadImage]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/seedance2.5(支持30秒长视频)_多模态生视频_2086018514942517249.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/seedance2.5(支持30秒长视频)_多模态生视频_2086018514942517249.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `LoadImage`
- `RH_BytedanceSeedance25TokenMultimodalVideo`
- `LoadVideo`
- `LoadAudio`
- `CR Text`
- `SaveVideo`
- `LoadImage`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadImage`、`RH_BytedanceSeedance25TokenMultimodalVideo`、`LoadVideo`、`LoadAudio`、`SaveVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance25TokenMultimodalVideo、SaveVideo、LoadAudio、LoadVideo、sd15-t2i-basic、sd15-t2i-lora、Seed

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
