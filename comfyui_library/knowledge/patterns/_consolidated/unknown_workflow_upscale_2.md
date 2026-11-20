---
name: unknown_workflow_upscale_2
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9909
common_nodes: [ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, RH_Nano_Banana_Image2Image, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/全能图片V1-电商白底图换背景_1966775584833613825.json, 图片生成/图生图/全能图片V1-线稿上色_1966149405520949249.json, 图片生成/图生图/全能图片V1-老照片修复_1966124757429161986.json, 图片生成/图生图/全能图片V1-虚拟试衣_1966757934581624833.json, 图片生成/图生图/全能图片V1-角色周边设计_1968687391248666626.json, 图片生成/图生图/全能图片V1-设计稿样机效果_1966754869824696321.json, 图片生成/图生图/全能图片V1-针织玩偶_1966144631845154818.json, 图片生成/图生图/全能图片V1-风格化贴纸_1966140323560853505.json, 图片生成/图生图/全能图片V1-黑白图片上色_1966131468915437569.json, 图片生成/文生图/全能图片V1 深度图控制_1966877036839100418.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_2

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/全能图片V1-电商白底图换背景_1966775584833613825.json、图片生成/图生图/全能图片V1-线稿上色_1966149405520949249.json、图片生成/图生图/全能图片V1-老照片修复_1966124757429161986.json、图片生成/图生图/全能图片V1-虚拟试衣_1966757934581624833.json、图片生成/图生图/全能图片V1-角色周边设计_1968687391248666626.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `workflow>Depth` —— 1/10 个有
- `workflow>提示词` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
