---
name: unknown_workflow_generic_845
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78
common_nodes: [ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_ComfyFluxKontext, RH_Translator, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext三图模式_1938500281393176578.json, 图片生成/图生图/Flux Kontext双图模式_1937089697271173121.json, 图片生成/图生图/flux Kontext三图模式_1937094945591185409.json, 平台全量/Flux Kontext三图模式人物画脸谱换背景_1937742240431411201.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_845

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Kontext三图模式_1938500281393176578.json、图片生成/图生图/Flux Kontext双图模式_1937089697271173121.json、图片生成/图生图/flux Kontext三图模式_1937094945591185409.json、平台全量/Flux Kontext三图模式人物画脸谱换背景_1937742240431411201.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: CropByMask V2` —— 3/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/4 个有
- `RMBG` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
