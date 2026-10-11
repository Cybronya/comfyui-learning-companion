---
key: 视频生成/文生视频/Seedance2.5一键小说原文转15秒漫剧工作流_2091050755548606466.json
name: Seedance2.5一键小说原文转15秒漫剧工作流_2091050755548606466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.5一键小说原文转15秒漫剧工作流_2091050755548606466.json
hash: afa1f10f9695c84a
coverage: 0.733333
learned_at: 2026-10-11 21:19:50
nodes: [LoadImage, LoadImage, CR Prompt Text, CR Prompt Text, CR Prompt Text, RHHiddenNodes, RHLLMChatNode, ShowText|pysssss, LoadImage, RHHiddenNodes, RHHiddenNodes, RH_RhartImageG2OfficialImageToImage, SaveImage, RH_BytedanceSeedance25TokenMultimodalVideo, SaveVideo]
patterns: []
missing: [CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Seedance2.5一键小说原文转15秒漫剧工作流_2091050755548606466.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.5一键小说原文转15秒漫剧工作流_2091050755548606466.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（15 个）：
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `RHHiddenNodes`
- `RHLLMChatNode`
- `ShowText|pysssss`
- `LoadImage`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `RH_BytedanceSeedance25TokenMultimodalVideo`
- `SaveVideo`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`LoadImage`、`RHHiddenNodes`、`RHLLMChatNode`、`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RH_BytedanceSeedance25TokenMultimodalVideo`、`SaveVideo`

**缺卡**（3）：`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance25TokenMultimodalVideo、SaveImage、SaveVideo、RH_RhartImageG2OfficialImageToImage、RHHiddenNodes、RHLLMChatNode、sd15-t2i-basic

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
