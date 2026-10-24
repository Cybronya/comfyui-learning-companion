---
name: image_to_image_controlnet_upscale_face_detailer
type: Image To Image
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingV2Preprocessor, FaceDetailer, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerColor: Brightness & Contrast, LoadImage, SaveImage, Text Concatenate, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/iL超清真人转动漫_1930781565452746754.json, 图片生成/图生图/重绘超清真人转动漫工作流图生图漫改图片工作流_2089571808591835137.json, 图片生成/图生图/重绘超清真人转动漫工作流风格迁移图生图漫改图片工作流_2089676789865074690.json, 图片生成/图生图/重绘超清真人转动漫工作流风格迁移图生图漫改图片工作流_2090065257011171330.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/iL超清真人转动漫_1930781565452746754.json、图片生成/图生图/重绘超清真人转动漫工作流图生图漫改图片工作流_2089571808591835137.json、图片生成/图生图/重绘超清真人转动漫工作流风格迁移图生图漫改图片工作流_2089676789865074690.json、图片生成/图生图/重绘超清真人转动漫工作流风格迁移图生图漫改图片工作流_2090065257011171330.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `FaceDetailer`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `SaveImage`
- `Text Concatenate`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
