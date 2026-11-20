---
name: text_to_image_controlnet_sampler_clip_5
type: Text To Image
frequency: 8
level: moderate
coverage: 0.96975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, ModelPatchLoader, SaveImage, UNETLoader, VAEDecode, VAELoader, ZImageFunControlnet]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-Base-万能局部重绘（极速版）_2027782001276751874.json, 图片生成/图生图/Z-image-base-姿势控制_2027928258439811073.json, 图片生成/图生图/Z-image-base-深度控制_2027926513785507842.json, 图片生成/图生图/Z-image-base-线条控制_2027918612886982657.json, 图片生成/图生图/Z-image-turbo-万能局部重绘（极速版）_2027775204977549313.json, 图片生成/图生图/Z-image-turbo-扩图_2033154181028126721.json, 图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json, 图片生成/文生图/造相Z-image Controlnet union_2016406271590666241.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image-Base-万能局部重绘（极速版）_2027782001276751874.json、图片生成/图生图/Z-image-base-姿势控制_2027928258439811073.json、图片生成/图生图/Z-image-base-深度控制_2027926513785507842.json、图片生成/图生图/Z-image-base-线条控制_2027918612886982657.json、图片生成/图生图/Z-image-turbo-万能局部重绘（极速版）_2027775204977549313.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `AIO_Preprocessor` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `MaskFillHoles` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `ImagePadForOutpaint` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 768 | 8 | 82% |
| 高度 | 512 | 512 - 1280 | 8 | 58% |
| 采样步数 | 7 | 6 - 30 | 8 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 8 | 47% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 768，8 个样本，取值集中（一致性 82%）
- 高度 中位数 512，观测区间 512 - 1280，8 个样本
- 采样步数 中位数 7，观测区间 6 - 30，8 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，8 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
