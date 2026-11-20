---
name: unknown_workflow_sampler_87
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [InstantIR_Loader, InstantIR_Sampler, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/InstantIR万能图像模糊变高清修复V1_1937854843388084226.json, 平台全量/InstantIR低分辨率修复_1856762382893928450.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/InstantIR万能图像模糊变高清修复V1_1937854843388084226.json、平台全量/InstantIR低分辨率修复_1856762382893928450.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `InstantIR_Loader`
- `InstantIR_Sampler`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
