---
name: unknown_workflow_generic_1100
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.855
common_nodes: [LoadImage, ShowText|pysssss, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/反推提示词/爆款封面反推提示词_2048712018777088001.json, 平台全量/Qwen3-VL-图片反推提示词_2020458220048879618.json, 平台全量/qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1100

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/爆款封面反推提示词_2048712018777088001.json、平台全量/Qwen3-VL-图片反推提示词_2020458220048879618.json、平台全量/qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `ShowText|pysssss`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `Text` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
