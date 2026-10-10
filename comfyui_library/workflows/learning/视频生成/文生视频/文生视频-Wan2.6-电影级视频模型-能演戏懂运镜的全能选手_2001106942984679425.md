---
key: 视频生成/文生视频/文生视频-Wan2.6-电影级视频模型-能演戏懂运镜的全能选手_2001106942984679425.json
name: 文生视频-Wan2.6-电影级视频模型-能演戏懂运镜的全能选手_2001106942984679425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频-Wan2.6-电影级视频模型-能演戏懂运镜的全能选手_2001106942984679425.json
hash: 334200f5c672f625
coverage: 0.75
learned_at: 2026-10-11 02:57:41
nodes: [LoadAudio, RH_Wan26_T2V, CR Text, SaveVideo]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/文生视频-Wan2.6-电影级视频模型-能演戏懂运镜的全能选手_2001106942984679425.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频-Wan2.6-电影级视频模型-能演戏懂运镜的全能选手_2001106942984679425.json`

## 结构

**生成流程**：Output → Other

**节点**（4 个）：
- `LoadAudio`
- `RH_Wan26_T2V`
- `CR Text`
- `SaveVideo`

## 知识

覆盖率 **75%**（3/4）

**有卡**：`LoadAudio`、`RH_Wan26_T2V`、`SaveVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：SaveVideo、LoadAudio、RH_Wan26_T2V、sd15-t2i-basic、sd15-t2i-lora、Text、SaveImage、CS_Preview_Any

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
