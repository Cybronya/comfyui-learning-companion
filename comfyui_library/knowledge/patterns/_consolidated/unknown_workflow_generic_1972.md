---
name: unknown_workflow_generic_1972
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5
common_nodes: [CR Text, CR Text Replace, GetNode, JDCN_StringToList, LoadImage, MemoryCleaner, ProcessString, SaveImage, SetNode, ShowText|pysssss, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [平台全量/真人写真套图 V1.1_2049378808213544961.json, 平台全量/真人写真套图 V1.3_2049418470210674690.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1972

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/真人写真套图 V1.1_2049378808213544961.json、平台全量/真人写真套图 V1.3_2049418470210674690.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Text Replace`
- `GetNode`
- `JDCN_StringToList`
- `LoadImage`
- `MemoryCleaner`
- `ProcessString`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
