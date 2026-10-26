---
name: unknown_workflow_generic_1686
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8035
common_nodes: [LoadImage, PrimitiveStringMultiline, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/Pixverse V6图生视频工作流｜爱诗 V6 图片转视频_2099677244473040897.json, 视频生成/图生视频/Seedance 2.0多模态参考工作流｜多图参考生视频_2099453267779612673.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1686

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Pixverse V6图生视频工作流｜爱诗 V6 图片转视频_2099677244473040897.json、视频生成/图生视频/Seedance 2.0多模态参考工作流｜多图参考生视频_2099453267779612673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RH_BytedanceSeedance20GlobalMultimodalVideo` —— 1/2 个有
- `RH_PixverseV6ImageToVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
