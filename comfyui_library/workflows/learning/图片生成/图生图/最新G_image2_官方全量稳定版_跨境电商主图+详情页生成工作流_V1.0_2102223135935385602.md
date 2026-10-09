---
key: 图片生成/图生图/最新G_image2_官方全量稳定版_跨境电商主图+详情页生成工作流_V1.0_2102223135935385602.json
name: 最新G_image2_官方全量稳定版_跨境电商主图+详情页生成工作流_V1.0_2102223135935385602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最新G_image2_官方全量稳定版_跨境电商主图+详情页生成工作流_V1.0_2102223135935385602.json
hash: 1533d124b4f110d0
coverage: 0.631579
learned_at: 2026-10-09 22:27:10
nodes: [HAIGC_Layer, ShowText|pysssss, HAIGC_CombineUnits, RH_LLMAPI_Pro_Node, RH_RhartImageNG31FlashOfficialImageToImage, SaveImage, LoadImage, Text, Text, Text, RH_LLMAPI_Pro_Node, ShowText|pysssss, easy promptConcat, easy promptConcat, easy promptConcat, ProcessString, easy promptLine, easy showAnything, HAIGC_SavePSD]
patterns: []
missing: [easy promptConcat, easy promptConcat, easy promptConcat, easy promptLine]
discoveries: [次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/最新G_image2_官方全量稳定版_跨境电商主图+详情页生成工作流_V1.0_2102223135935385602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102223135935385602.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `HAIGC_Layer`
- `ShowText|pysssss`
- `HAIGC_CombineUnits`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageNG31FlashOfficialImageToImage`
- `SaveImage`
- `LoadImage`
- `Text`
- `Text`
- `Text`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `ProcessString`
- `easy promptLine`
- `easy showAnything`
- `HAIGC_SavePSD`

## 知识

覆盖率 **63%**（12/19）

**有卡**：`HAIGC_Layer`、`HAIGC_CombineUnits`、`RH_LLMAPI_Pro_Node`、`RH_RhartImageNG31FlashOfficialImageToImage`、`SaveImage`、`LoadImage`、`Text`、`ProcessString`、`HAIGC_SavePSD`

**缺卡**（4）：`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptLine`

**用到的条目**：LoadImage、SaveImage、HAIGC_SavePSD、ProcessString、RH_LLMAPI_Pro_Node、Text、HAIGC_Layer、HAIGC_CombineUnits

## 学习发现

- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
