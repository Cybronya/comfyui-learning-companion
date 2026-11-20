---
name: unknown_workflow_upscale_56
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.885667
common_nodes: [LoadImage, SaveImage, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [平台全量/VOSR2 放大图像预处理_2102622254843645953.json, 平台全量/VOSR2 高清放大_2102447098020057090.json, 平台全量/图片高清放大（VOSR2）_2107738549553553410.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VOSR2 放大图像预处理_2102622254843645953.json、平台全量/VOSR2 高清放大_2102447098020057090.json、平台全量/图片高清放大（VOSR2）_2107738549553553410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `ImageBlur` —— 1/3 个有
- `ImageScale` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
