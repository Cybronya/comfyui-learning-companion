---
name: unknown_workflow_checkpoint_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.879333
common_nodes: [CheckpointLoaderSimple, Image Comparer (rgthree), LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage]
problems: []
missing: []
members: [平台全量/SupirLightning高清修复_1956984415826972673.json, 平台全量/supir高清放大工作流_1964310578095341570.json, 平台全量/爆炸细节-SUPIR-最强图像细节添加工具_1902274533598846978.json]
source: knowledge_consolidation
---

# unknown_workflow_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/SupirLightning高清修复_1956984415826972673.json、平台全量/supir高清放大工作流_1964310578095341570.json、平台全量/爆炸细节-SUPIR-最强图像细节添加工具_1902274533598846978.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ImageResize+` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
