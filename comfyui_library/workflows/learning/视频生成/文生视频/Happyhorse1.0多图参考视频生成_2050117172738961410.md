---
key: 视频生成/文生视频/Happyhorse1.0多图参考视频生成_2050117172738961410.json
name: Happyhorse1.0多图参考视频生成_2050117172738961410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Happyhorse1.0多图参考视频生成_2050117172738961410.json
hash: 3f1a54f0dc0761d7
coverage: 0.478261
learned_at: 2026-10-11 19:49:34
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), RH_AlibabaHappyhorse10ReferenceToVideo, RH_AlibabaHappyhorse10TextToVideo, SaveVideo, CR Prompt Text, RH_AlibabaHappyhorse10ImageToVideo, LoadImage, SaveVideo, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SaveVideo, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CR Prompt Text]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Happyhorse1.0多图参考视频生成_2050117172738961410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Happyhorse1.0多图参考视频生成_2050117172738961410.json`

## 结构

**生成流程**：Output → Other

**节点**（23 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `RH_AlibabaHappyhorse10ReferenceToVideo`
- `RH_AlibabaHappyhorse10TextToVideo`
- `SaveVideo`
- `CR Prompt Text`
- `RH_AlibabaHappyhorse10ImageToVideo`
- `LoadImage`
- `SaveVideo`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SaveVideo`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **48%**（11/23）

**有卡**：`LoadImage`、`RH_AlibabaHappyhorse10ReferenceToVideo`、`RH_AlibabaHappyhorse10TextToVideo`、`SaveVideo`、`RH_AlibabaHappyhorse10ImageToVideo`

**缺卡**（5）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、RH_AlibabaHappyhorse10TextToVideo、RH_AlibabaHappyhorse10ImageToVideo、RH_AlibabaHappyhorse10ReferenceToVideo、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
