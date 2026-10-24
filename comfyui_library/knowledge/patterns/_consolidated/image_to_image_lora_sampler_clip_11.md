---
name: image_to_image_lora_sampler_clip_11
type: Image To Image
frequency: 13
level: strong
coverage: 0.946231
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/PS专用溶图流_2080460737826344962.json, 图片生成/图生图/PS专用溶图流_2081930794498617346.json, 图片生成/图生图/PS专用溶图流_2081982051393302529.json, 图片生成/图生图/PS专用溶图流_2082013615124733954.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein——电商产品光影融合溶图打光_2018488925819506690.json, 图片生成/图生图/主图万物电商产品光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2072999532249567233.json, 图片生成/图生图/亚马逊光影融合1.0_2037456527702888450.json, 图片生成/图生图/溶图+打光_2098231532556210177.json, 图片生成/图生图/溶图打光-F.2_Klein人像细节迁移_2096170592125939714.json, 图片生成/图生图/溶图打光-F.2_Klein人像细节迁移_2096405298079686657.json, 图片生成/图生图/电商产品打光换背景光影溶图细节迁移保持细节尺寸不变_2073002986959364097.json, 图片生成/图生图/通道ID图2.0_2060658643808382978.json, 图片生成/文生图/产品融图打光（产品标贴一致性）_2037437084016844802.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/PS专用溶图流_2080460737826344962.json、图片生成/图生图/PS专用溶图流_2081930794498617346.json、图片生成/图生图/PS专用溶图流_2081982051393302529.json、图片生成/图生图/PS专用溶图流_2082013615124733954.json、图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein——电商产品光影融合溶图打光_2018488925819506690.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: HLFrequencyDetailRestore` —— 12/13 个有
- `ImpactInt` —— 7/13 个有
- `FastCanvas` —— 2/13 个有
- `FastCanvasTool` —— 2/13 个有
- `ImageCropper` —— 2/13 个有
- `easy imageRemBg` —— 2/13 个有
- `Int` —— 1/13 个有
- `LayerStyle: ColorOverlay V2` —— 1/13 个有
- `MaskPreview+` —— 1/13 个有
- `Preview from image [Crystools]` —— 1/13 个有
- `Switch any [Crystools]` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
