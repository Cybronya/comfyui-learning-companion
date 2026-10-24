---
name: unknown_workflow_controlnet_upscale_clip_2
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.857
common_nodes: [CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, DF_Int_to_Float, Image Comparer (rgthree), ImageResizeKJv2, LoadImage, PreviewImage, SaveImage, SetUnionControlNetType, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/动漫手办 2D to 3D_1940221249937166337.json, 图片生成/图生图/图生图-二次元-动漫手办_2046952108653547522.json, 图片生成/图生图/图生图-二次元-动漫手办_2046956707284258817.json, 图片生成/图生图/图生图二次元动漫手办_1939943211311734786.json, 图片生成/图生图/图生图二次元动漫手办_1945728382736748545.json, 图片生成/图生图/图生图二次元动漫手办_2031248193320652801.json, 图片生成/图生图/图生图生成二次元动漫手办_1944621526782234626.json, 图片生成/图生图/图生图＋二次元动漫手办_2064935646636101633.json, 图片生成/图生图/强烈推荐！图生图二次元动漫手办，二次元插画效果最好_2021123679098245122.json, 图片生成/图生图/生成二次元手办（超还原！！）_2028725930163703809.json, 视频生成/图生视频/图生图-二次元-动漫手办_2047507616280088577.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_clip_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/动漫手办 2D to 3D_1940221249937166337.json、图片生成/图生图/图生图-二次元-动漫手办_2046952108653547522.json、图片生成/图生图/图生图-二次元-动漫手办_2046956707284258817.json、图片生成/图生图/图生图二次元动漫手办_1939943211311734786.json、图片生成/图生图/图生图二次元动漫手办_1945728382736748545.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DF_Int_to_Float`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.4 | 0.4 - 0.4 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.4，观测区间 0.4 - 0.4，11 个样本，取值集中（一致性 100%）
