---
name: unknown_workflow_upscale_clip_checkpoint
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.752
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, Image Comparer (rgthree), LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/8K图片高清放大_2083449760907878402.json, 图片生成/图生图/supir放大，适用于面部占比大的_1954064245321453570.json, 图片生成/图生图/【实用流】SUPIR  8K 效率放大_1819075068759814146.json, 图片生成/图生图/万物8k高清_2018494322525605889.json, 图片生成/图生图/图片SUP-模糊变高清_2046220648355205122.json, 图片生成/图生图/无损图片 一键高清放大_1908444757444730882.json, 图片生成/图生图/高清8K放大_1994687453787267073.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/8K图片高清放大_2083449760907878402.json、图片生成/图生图/supir放大，适用于面部占比大的_1954064245321453570.json、图片生成/图生图/【实用流】SUPIR  8K 效率放大_1819075068759814146.json、图片生成/图生图/万物8k高清_2018494322525605889.json、图片生成/图生图/图片SUP-模糊变高清_2046220648355205122.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/7 个有
- `ImpactInt` —— 5/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `UltimateSDUpscale` —— 5/7 个有
- `ImageResize+` —— 4/7 个有
- `Display Int (rgthree)` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `HD UltimateSDUpscale` —— 2/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
