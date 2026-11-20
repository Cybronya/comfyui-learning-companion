---
name: unknown_workflow_generic_1923
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [LoadImage, RealRestorerApplyDevices, RealRestorerLoadPipeline, RealRestorerRun, SaveImage]
problems: []
missing: []
members: [平台全量/【4月】RealRestorer 最强开源图片修复（有参考）_2042882892698755074.json, 视频生成/图生视频/RealRestorer编辑_2039725363995090945.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1923

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【4月】RealRestorer 最强开源图片修复（有参考）_2042882892698755074.json、视频生成/图生视频/RealRestorer编辑_2039725363995090945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RealRestorerApplyDevices`
- `RealRestorerLoadPipeline`
- `RealRestorerRun`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_Translator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
