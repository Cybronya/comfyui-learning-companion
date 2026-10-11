---
key: 视频生成/文生视频/happyhorse-1.0 + 提示词扩写 文生视频 0.9元_秒_2049431714971262977.json
name: happyhorse-1.0 + 提示词扩写 文生视频 0.9元_秒_2049431714971262977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/happyhorse-1.0 + 提示词扩写 文生视频 0.9元_秒_2049431714971262977.json
hash: bc73d44ecd69356d
coverage: 0.444444
learned_at: 2026-10-11 19:49:44
nodes: [CR Text Replace, Int2Any_AS, Any To String (mtb), PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_NODE, RH_AlibabaHappyhorse10TextToVideo, SaveVideo, PrimitiveStringMultiline]
patterns: []
missing: [Any To String (mtb), CR Text Replace]
discoveries: [次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/happyhorse-1.0 + 提示词扩写 文生视频 0.9元_秒_2049431714971262977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/happyhorse-1.0 + 提示词扩写 文生视频 0.9元_秒_2049431714971262977.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `CR Text Replace`
- `Int2Any_AS`
- `Any To String (mtb)`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RH_AlibabaHappyhorse10TextToVideo`
- `SaveVideo`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **44%**（4/9）

**有卡**：`Int2Any_AS`、`RH_LLMAPI_NODE`、`RH_AlibabaHappyhorse10TextToVideo`、`SaveVideo`

**缺卡**（2）：`Any To String (mtb)`、`CR Text Replace`

**用到的条目**：SaveVideo、RH_LLMAPI_NODE、Int2Any_AS、RH_AlibabaHappyhorse10TextToVideo、sd15-t2i-basic、sd15-t2i-lora、Int、node

## 学习发现

- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
