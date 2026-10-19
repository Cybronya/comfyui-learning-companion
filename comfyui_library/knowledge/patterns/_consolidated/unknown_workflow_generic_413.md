---
name: unknown_workflow_generic_413
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.833
common_nodes: [LoadImage, PreviewAny, SaveImage, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/反推提示词/qwen3.8-27B反推图片提示词_2103825737462673409.json, 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json, 视频生成/文生视频/反推重绘_2047964125099204609.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_413

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/qwen3.8-27B反推图片提示词_2103825737462673409.json、图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json、视频生成/文生视频/反推重绘_2047964125099204609.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2TextToImage` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
