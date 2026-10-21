---
name: unknown_workflow_generic_770
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8055
common_nodes: [LoadImage, PreviewAny, RH_RhartImageG2TextToImage, SaveImage, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/G2+ Gemma 4 替你写生图提示词！_2048327820568432642.json, 视频生成/文生视频/反推重绘_2047964125099204609.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_770

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/G2+ Gemma 4 替你写生图提示词！_2048327820568432642.json、视频生成/文生视频/反推重绘_2047964125099204609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewAny`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
