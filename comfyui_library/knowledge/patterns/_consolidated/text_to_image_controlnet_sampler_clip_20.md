---
name: text_to_image_controlnet_sampler_clip_20
type: Text To Image
frequency: 3
level: moderate
coverage: 0.876
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商 固定场景改变人物姿势_1961619724868194306.json, 图片生成/文生图/Flux_现代都市_文生图_1999040279489470466.json, 图片生成/文生图/工作流基础系列19-FLUX-Canny_Depth工作流_2047844431319015426.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商 固定场景改变人物姿势_1961619724868194306.json、图片生成/文生图/Flux_现代都市_文生图_1999040279489470466.json、图片生成/文生图/工作流基础系列19-FLUX-Canny_Depth工作流_2047844431319015426.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `GemmaxRun` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `InstructPixToPixConditioning` —— 1/3 个有
- `LayerUtility: GetImageSize` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1.2 | 3 | 91% |
| 宽度 | 512 | 512 - 720 | 3 | 83% |
| 高度 | 512 | 512 - 1280 | 3 | 53% |
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1.2，3 个样本，取值集中（一致性 91%）
- 宽度 中位数 512，观测区间 512 - 720，3 个样本，取值集中（一致性 83%）
- 高度 中位数 512，观测区间 512 - 1280，3 个样本
- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
