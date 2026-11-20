---
name: unknown_workflow_generic_1703
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [CR Prompt Text, CR Text, CR Text Concatenate, LoadImage, PreviewImage, RHHiddenNodes, RH_RhartImageG2ImageToImage, SaveImage, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/【3.1超值】带货视频  超低价  适合 口播短视频 带货讲解_2080302190673092610.json, 视频生成/图生视频/【超值】带货视频  低至0.04元_秒  全自动  带货视频生成_2076026308588560386.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1703

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【3.1超值】带货视频  超低价  适合 口播短视频 带货讲解_2080302190673092610.json、视频生成/图生视频/【超值】带货视频  低至0.04元_秒  全自动  带货视频生成_2076026308588560386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RH_RhartVideoGImageToVideo` —— 1/2 个有
- `RH_Veo3_Image2Video` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
