---
name: unknown_workflow_generic_1722
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6905
common_nodes: [ImpactSwitch, JjkText, LoadImage, RH_Captioner, RH_Jimeng_Image2Video, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/即梦AI-图生视频_1945038277844062209.json, 视频生成/图生视频/即梦AI-图生视频_1984987150372524033.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1722

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/即梦AI-图生视频_1945038277844062209.json、视频生成/图生视频/即梦AI-图生视频_1984987150372524033.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `ImpactSwitch`
- `JjkText`
- `LoadImage`
- `RH_Captioner`
- `RH_Jimeng_Image2Video`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
