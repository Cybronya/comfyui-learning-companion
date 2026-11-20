---
name: unknown_workflow_checkpoint_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.793333
common_nodes: [CheckpointLoaderSimple, LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/放大_2031973545307279362.json, 平台全量/CG迷-SUPIR图片修复，高清放大工作流_1927016363271868418.json, 平台全量/高清放大_sdz_1937021542687739905.json]
source: knowledge_consolidation
---

# unknown_workflow_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/放大_2031973545307279362.json、平台全量/CG迷-SUPIR图片修复，高清放大工作流_1927016363271868418.json、平台全量/高清放大_sdz_1937021542687739905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `Float` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
