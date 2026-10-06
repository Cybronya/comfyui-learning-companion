---
key: 图片生成/反推提示词/小说剧本转标准JSON预处理剧本+搭配全栈式短剧生成V4.2.1使用_2088987931473170433.json
name: 小说剧本转标准JSON预处理剧本+搭配全栈式短剧生成V4.2.1使用_2088987931473170433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/小说剧本转标准JSON预处理剧本+搭配全栈式短剧生成V4.2.1使用_2088987931473170433.json
hash: 43d48dd44a00f71f
coverage: 0
learned_at: 2026-10-06 21:38:44
nodes: [JjkText, PreviewAny, RHLLMChatNode, SaveText]
patterns: []
missing: [RHLLMChatNode, PreviewAny, SaveText]
discoveries: [次要节点 `RHLLMChatNode` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 该工作流的所有节点都没有对应知识卡，当前无法解释其行为]
---

# 图片生成/反推提示词/小说剧本转标准JSON预处理剧本+搭配全栈式短剧生成V4.2.1使用_2088987931473170433.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/小说剧本转标准JSON预处理剧本+搭配全栈式短剧生成V4.2.1使用_2088987931473170433.json`

## 结构

**生成流程**：Other

**节点**（4 个）：
- `JjkText`
- `PreviewAny`
- `RHLLMChatNode`
- `SaveText`

## 知识

覆盖率 **0%**（0/4）

**缺卡**（3）：`RHLLMChatNode`、`PreviewAny`、`SaveText`

**用到的条目**：sd15-t2i-basic、sd15-t2i-lora、SaveImage

## 学习发现

- 次要节点 `RHLLMChatNode` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 该工作流的所有节点都没有对应知识卡，当前无法解释其行为
