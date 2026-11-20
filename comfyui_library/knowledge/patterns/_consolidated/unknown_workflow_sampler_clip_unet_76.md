---
name: unknown_workflow_sampler_clip_unet_76
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.779385
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json, 图片生成/图生图/Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753.json, 图片生成/图生图/Flux3快速图像编辑_2110973569806192641.json, 图片生成/图生图/flux3_klein_image_edit图像编辑_2110972221408763906.json, 图片生成/图生图/flux3_klein_image_edit图像编辑_2112068355019599874.json, 图片生成/图生图/flux3_klein_image_edit图像编辑_2116710407900581890.json, 图片生成/图生图/（9图）flux3_klein_image_edit图像编辑_2111089818842255361.json, 图片生成/文生图/ERNIE-Image-turbo 文生图_2044607804283035649.json, 图片生成/文生图/Flux3 kelin图像编辑_2110901954389041153.json, 图片生成/文生图/Flux3 kelin图像编辑（提示词优化）_2110918718791438338.json, 图片生成/文生图/flux3图像编辑_2111385356770828290.json, 平台全量/Flux3 kelin图像编辑（提示词优化）_2118163838213382146.json, 平台全量/Flux3 kelin图像编辑（提示词优化）_2118221181013807105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_76

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json、图片生成/图生图/Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753.json、图片生成/图生图/Flux3快速图像编辑_2110973569806192641.json、图片生成/图生图/flux3_klein_image_edit图像编辑_2110972221408763906.json、图片生成/图生图/flux3_klein_image_edit图像编辑_2112068355019599874.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `ReferenceMultiLatent` —— 12/13 个有
- `Image Comparer (rgthree)` —— 11/13 个有
- `TextGenerate` —— 10/13 个有
- `EmptyFlux2LatentImage` —— 8/13 个有
- `PreviewAny` —— 8/13 个有
- `CreateBoundingBoxes` —— 7/13 个有
- `Text` —— 6/13 个有
- `CR Text` —— 5/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `ACE_TextGoogleTranslate` —— 1/13 个有
- `ImageCompare` —— 1/13 个有
- `Int` —— 1/13 个有
- `JjkText` —— 1/13 个有
- `StringReplace` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 13 | 77% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 13 | 64% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | simple | - | 13 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，13 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 simple，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
