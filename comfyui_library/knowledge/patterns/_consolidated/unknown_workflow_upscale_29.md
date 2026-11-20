---
name: unknown_workflow_upscale_29
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9618
common_nodes: [ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, RH_Nano_Banana_Image2Image, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [平台全量/全能图片V1 软装方案一键提取图工作流 V1.0_1980475490505043970.json, 平台全量/全能图片V1-8位像素图标_1966146943112179713.json, 平台全量/全能图片V1-IP形象制作_1966137786493472770.json, 平台全量/全能图片V1-老照片修复高清放大_1978041926794489858.json, 平台全量/设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/全能图片V1 软装方案一键提取图工作流 V1.0_1980475490505043970.json、平台全量/全能图片V1-8位像素图标_1966146943112179713.json、平台全量/全能图片V1-IP形象制作_1966137786493472770.json、平台全量/全能图片V1-老照片修复高清放大_1978041926794489858.json、平台全量/设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
