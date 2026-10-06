---
key: 图片生成/图生图/全能图片G Image2.5图生图_2107159515836805121.json
name: 全能图片G Image2.5图生图_2107159515836805121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片G Image2.5图生图_2107159515836805121.json
hash: 9853473502005478
coverage: 0.5
learned_at: 2026-10-06 21:43:18
nodes: [SaveImage, Text, LoadImage, RH_RhartImageG25OfficialTokenSunburstEdit]
patterns: []
missing: [RH_RhartImageG25OfficialTokenSunburstEdit, Text]
discoveries: [次要节点 `RH_RhartImageG25OfficialTokenSunburstEdit` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/全能图片G Image2.5图生图_2107159515836805121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全能图片G Image2.5图生图_2107159515836805121.json`

## 结构

**生成流程**：Output → Other

**节点**（4 个）：
- `SaveImage`
- `Text`
- `LoadImage`
- `RH_RhartImageG25OfficialTokenSunburstEdit`

## 知识

覆盖率 **50%**（2/4）

**有卡**：`SaveImage`、`LoadImage`

**缺卡**（2）：`RH_RhartImageG25OfficialTokenSunburstEdit`、`Text`

**用到的条目**：LoadImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `RH_RhartImageG25OfficialTokenSunburstEdit` 知识库中没有该节点类型的任何知识
- 次要节点 `Text` 知识库中没有该节点类型的任何知识
