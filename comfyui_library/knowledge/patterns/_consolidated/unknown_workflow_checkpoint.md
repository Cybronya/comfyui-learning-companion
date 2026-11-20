---
name: unknown_workflow_checkpoint
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.645333
common_nodes: [CheckpointLoaderSimple, Image Comparer (rgthree), LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SUPIR图像修复工作流_1969062503655370754.json, 图片生成/图生图/【阡陌】SUPIR超高清细节修复放大工作流_1902930665241743361.json, 图片生成/图生图/模糊图一键变清晰_V1_1958057559603236865.json]
source: knowledge_consolidation
---

# unknown_workflow_checkpoint

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SUPIR图像修复工作流_1969062503655370754.json、图片生成/图生图/【阡陌】SUPIR超高清细节修复放大工作流_1902930665241743361.json、图片生成/图生图/模糊图一键变清晰_V1_1958057559603236865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

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
- `ImageResize+` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
