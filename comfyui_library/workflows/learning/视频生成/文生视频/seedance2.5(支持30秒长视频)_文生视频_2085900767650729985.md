---
key: 视频生成/文生视频/seedance2.5(支持30秒长视频)_文生视频_2085900767650729985.json
name: seedance2.5(支持30秒长视频)_文生视频_2085900767650729985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/seedance2.5(支持30秒长视频)_文生视频_2085900767650729985.json
hash: f3aa7be2f687b9da
coverage: 0.666667
learned_at: 2026-10-10 23:09:17
nodes: [CR Text, RH_BytedanceSeedance25TokenTextToVideo, SaveVideo]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/seedance2.5(支持30秒长视频)_文生视频_2085900767650729985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/seedance2.5(支持30秒长视频)_文生视频_2085900767650729985.json`

## 结构

**生成流程**：Output → Other

**节点**（3 个）：
- `CR Text`
- `RH_BytedanceSeedance25TokenTextToVideo`
- `SaveVideo`

## 知识

覆盖率 **67%**（2/3）

**有卡**：`RH_BytedanceSeedance25TokenTextToVideo`、`SaveVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：RH_BytedanceSeedance25TokenTextToVideo、SaveVideo、sd15-t2i-basic、sd15-t2i-lora、Seed、Text、sampler_name 调整经验、steps 调整经验

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
