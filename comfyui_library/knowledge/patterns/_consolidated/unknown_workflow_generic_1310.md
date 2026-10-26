---
name: unknown_workflow_generic_1310
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [LoadImage, SaveImage, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/反推提示词/▶千问Qwen3.5-提示词反推_2059196803807006722.json, 图片生成/反推提示词/千问3.5 LLAMA本地推理，FT_2111584531978477570.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1310

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/▶千问Qwen3.5-提示词反推_2059196803807006722.json、图片生成/反推提示词/千问3.5 LLAMA本地推理，FT_2111584531978477570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `ShowText|fofo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
