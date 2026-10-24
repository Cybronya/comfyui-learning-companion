---
name: unknown_workflow_inpaint_lora
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.84
common_nodes: [EasyControlGenerate, EasyControlLoadFlux, GetImageSizeAndCount, ImageConcanate, ImageResizeTo8x, LoadImage, SaveImage, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/EasyControl-吉卜力转绘｜深度控制_1910868139192844290.json, 图片生成/图生图/EasyControl商品迁移-体验篇_1913508782293614593.json, 图片生成/文生图/EasyControl-吉卜力转绘_姿势_深度_线稿_1907687687565021186.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/EasyControl-吉卜力转绘｜深度控制_1910868139192844290.json、图片生成/图生图/EasyControl商品迁移-体验篇_1913508782293614593.json、图片生成/文生图/EasyControl-吉卜力转绘_姿势_深度_线稿_1907687687565021186.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `EasyControlGenerate`
- `EasyControlLoadFlux`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageResizeTo8x`
- `LoadImage`
- `SaveImage`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `EasyControlLoadLora` —— 2/3 个有
- `EasyControlLoadMultiLora` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `InpaintPreprocessor` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
