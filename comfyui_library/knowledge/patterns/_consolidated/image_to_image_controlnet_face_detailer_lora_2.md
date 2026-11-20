---
name: image_to_image_controlnet_face_detailer_lora_2
type: Image To Image
frequency: 6
level: moderate
coverage: 0.822333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApply, ControlNetLoader, FaceDetailer, KSampler, LoadImage, LoraLoader, SaveImage, UltralyticsDetectorProvider, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/MajicMix+Flux-人像超级磨皮_2069335820053606401.json, 图片生成/图生图/SD1.5-tile-人像精修_1950204831518646273.json, 图片生成/图生图/【摄影修图】 商业级 + 修容、去痘_1922101324324749313.json, 图片生成/图生图/人像精修_1900359847442001921.json, 图片生成/图生图/人像精修带妆感（保留肌肤质感）磨皮带妆感_1926520554122285057.json, 图片生成/图生图/大厂商用人像精修工作流_1923661827207516162.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_face_detailer_lora_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/MajicMix+Flux-人像超级磨皮_2069335820053606401.json、图片生成/图生图/SD1.5-tile-人像精修_1950204831518646273.json、图片生成/图生图/【摄影修图】 商业级 + 修容、去痘_1922101324324749313.json、图片生成/图生图/人像精修_1900359847442001921.json、图片生成/图生图/人像精修带妆感（保留肌肤质感）磨皮带妆感_1926520554122285057.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApply`
- `ControlNetLoader`
- `FaceDetailer`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `CannyEdgePreprocessor` —— 1/6 个有
- `ChinesePrompt_Mix` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `Reroute (rgthree)` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.3 | 0.27 - 0.7 | 6 | 55% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 0.55 | 0.4 - 0.8 | 6 | 74% |
| 采样步数 | 10 | 10 - 15 | 6 | 83% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 6 | 80% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | normal | - | 6 | 83% |
| 重绘幅度 | 0.4 | 0.2 - 0.5 | 6 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.3，观测区间 0.27 - 0.7，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.55，观测区间 0.4 - 0.8，6 个样本
- 采样步数 中位数 10，观测区间 10 - 15，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 normal，6 个样本，一致性 83%
- 重绘幅度 中位数 0.4，观测区间 0.2 - 0.5，6 个样本
