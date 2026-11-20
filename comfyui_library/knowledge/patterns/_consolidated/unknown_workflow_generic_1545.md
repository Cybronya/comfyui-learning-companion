---
name: unknown_workflow_generic_1545
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [MultiplePathsInputPlus, Qwen3_VQA, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/视频一键反推提示词｜精准提取_2031957260590649346.json, 平台全量/Qwen3VL首尾帧反推提示词_2001198315683409922.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1545

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/视频一键反推提示词｜精准提取_2031957260590649346.json、平台全量/Qwen3VL首尾帧反推提示词_2001198315683409922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `MultiplePathsInputPlus`
- `Qwen3_VQA`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 1/2 个有
- `VideoLoaderPlus` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
