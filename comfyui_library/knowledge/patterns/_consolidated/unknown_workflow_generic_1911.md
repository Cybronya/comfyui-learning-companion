---
name: unknown_workflow_generic_1911
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [LoadVideo, RH_SkyreelsV3SingleShotVideoExtension, SaveVideo]
problems: []
missing: []
members: [平台全量/SkyreelsV3SingleShotVideoExtension_2038487986031042561.json, 平台全量/视频延长工作流｜短视频续写镜头延长_2099314481460506625.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1911

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/SkyreelsV3SingleShotVideoExtension_2038487986031042561.json、平台全量/视频延长工作流｜短视频续写镜头延长_2099314481460506625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadVideo`
- `RH_SkyreelsV3SingleShotVideoExtension`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
