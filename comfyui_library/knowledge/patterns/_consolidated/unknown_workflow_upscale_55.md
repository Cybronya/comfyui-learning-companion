---
name: unknown_workflow_upscale_55
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CreateVideo, GetVideoComponents, LoadVideo, SaveVideo, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [平台全量/VOSR 2.0 视频高清放大_2097685495408058369.json, 平台全量/VOSR 2.0 视频高清放大_2114921205957488642.json, 平台全量/视频高清放大（VOSR2）_2107738552468590593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_55

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VOSR 2.0 视频高清放大_2097685495408058369.json、平台全量/VOSR 2.0 视频高清放大_2114921205957488642.json、平台全量/视频高清放大（VOSR2）_2107738552468590593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `LoadVideo`
- `SaveVideo`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 2/3 个有
- `ImageScale` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
