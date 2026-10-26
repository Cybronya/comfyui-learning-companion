---
name: unknown_workflow_generic_1481
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9305
common_nodes: [CR Prompt Text, ImageBatchMulti, LoadImage, PreviewAny, SaveImage, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/全能图片V2（Google Gemma-4）多图编辑_2042609394663297026.json, 图片生成/文生图/全能图片G2（image-2.0）文生图_多图编辑_2053092636742955010.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1481

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能图片V2（Google Gemma-4）多图编辑_2042609394663297026.json、图片生成/文生图/全能图片G2（image-2.0）文生图_多图编辑_2053092636742955010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `ImageBatchMulti`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `RH_RhartImageG2TextToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
