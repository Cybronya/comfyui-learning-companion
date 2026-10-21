---
key: 图片生成/文生图/提示词强化for Qwen image 2.1_2102000116893839362.json
name: 提示词强化for Qwen image 2.1_2102000116893839362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/提示词强化for Qwen image 2.1_2102000116893839362.json
hash: 17107cdc47e66581
coverage: 0.559322
learned_at: 2026-10-20 01:52:32
nodes: [SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, JsonExtractString, llama_cpp_model_loader, llama_cpp_parameters, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveBoolean, PrimitiveBoolean, GetNode, 孤海注释, 孤海注释, GetNode, GetNode, ExecutionBlocker, PrimitiveInt, ImpactNeg, ImpactNeg, ExecutionBlocker, ExecutionBlocker, CR Text Replace, PrimitiveBoolean, PrimitiveBoolean, MathExpression_UTK, llama_cpp_instruct_adv, RHLLMChatNode, easy anythingIndexSwitch, DapaoMakeImageBatchNode, llama_cpp_instruct_adv, RHLLMChatNode, 1hew_SaveTxt, easy anythingIndexSwitch, easy anythingIndexSwitch, JjkText, 忽略多组孤海, SetNode, PrimitiveInt, ExecutionBlocker, SaveImage, ExecutionBlocker, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/提示词强化for Qwen image 2.1_2102000116893839362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/提示词强化for Qwen image 2.1_2102000116893839362.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（59 个）：
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JsonExtractString`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `GetNode`
- `孤海注释`
- `孤海注释`
- `GetNode`
- `GetNode`
- `ExecutionBlocker`
- `PrimitiveInt`
- `ImpactNeg`
- `ImpactNeg`
- `ExecutionBlocker`
- `ExecutionBlocker`
- `CR Text Replace`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `MathExpression_UTK`
- `llama_cpp_instruct_adv`
- `RHLLMChatNode`
- `easy anythingIndexSwitch`
- `DapaoMakeImageBatchNode`
- `llama_cpp_instruct_adv`
- `RHLLMChatNode`
- `1hew_SaveTxt`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `JjkText`
- `忽略多组孤海`
- `SetNode`
- `PrimitiveInt`
- `ExecutionBlocker`
- `SaveImage`
- `ExecutionBlocker`
- `LoadImage`

## 知识

覆盖率 **56%**（33/59）

**有卡**：`LoadImage`、`JsonExtractString`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`PrimitiveBoolean`、`ExecutionBlocker`、`ImpactNeg`、`CR Text Replace`、`MathExpression_UTK`、`llama_cpp_instruct_adv`、`RHLLMChatNode`、`easy anythingIndexSwitch`、`DapaoMakeImageBatchNode`、`1hew_SaveTxt`、`忽略多组孤海`、`SaveImage`

**用到的条目**：LoadImage、SaveImage、1hew_SaveTxt、DapaoMakeImageBatchNode、ExecutionBlocker、ImpactNeg、JsonExtractString、llama_cpp_instruct_adv
