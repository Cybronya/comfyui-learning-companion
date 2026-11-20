---
name: unknown_workflow_generic_664
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8952
common_nodes: [ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_ComfyFluxKontext, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Flux-Kontext多图融合 三图编辑-电商产品展示 一句修改图像_1933159787083538433.json, 图片生成/图生图/Flux-Kontext模型功能全面测试最全案例演示超详细使用教程_1933145305657290753.json, 图片生成/文生图/FLUX kontext 图像编辑-一句话改图-多图融合_1929554434584645634.json, 平台全量/FLUX kontext 图像编辑(三视图、线稿图、改变画风)_1930205092375597058.json, 平台全量/龙明Kontext模型功能全面测试_1934988189696204801.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_664

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux-Kontext多图融合 三图编辑-电商产品展示 一句修改图像_1933159787083538433.json、图片生成/图生图/Flux-Kontext模型功能全面测试最全案例演示超详细使用教程_1933145305657290753.json、图片生成/文生图/FLUX kontext 图像编辑-一句话改图-多图融合_1929554434584645634.json、平台全量/FLUX kontext 图像编辑(三视图、线稿图、改变画风)_1930205092375597058.json、平台全量/龙明Kontext模型功能全面测试_1934988189696204801.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_ComfyFluxKontext`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AutoDownloadBiRefNetModel` —— 4/5 个有
- `LayerUtility: CropByMask V2` —— 4/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 4/5 个有
- `RembgByBiRefNet` —— 4/5 个有
- `DeepTranslatorTextNode` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
