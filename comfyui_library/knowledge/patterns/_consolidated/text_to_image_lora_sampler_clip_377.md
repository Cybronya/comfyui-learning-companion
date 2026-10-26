---
name: text_to_image_lora_sampler_clip_377
type: Text To Image
frequency: 5
level: strong
coverage: 0.8966
common_nodes: [CLIPLoader, CLIPTextEncode, Easy_QwenEdit2509, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, JjkText, KSampler, Krea2OstrisEditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2动漫转真人Anything2Real V3目前最佳方案 动漫风格转写实_2108720385909944322.json, 图片生成/图生图/Krea2动漫转真人图生图处理生成工作流工具_2102514616378159106.json, 图片生成/图生图/Krea2动漫转真人｜二次元图生图写真化｜真人质感还原度高_2102279427303501826.json, 图片生成/图生图/Krea2漫剧角色资产一键生成工作流图生四视图_2100300485814218754.json, 图片生成/图生图/动漫转真人V3 Krea2 图生图人物写实化转换_2094195206609526785.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_377

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Krea2动漫转真人Anything2Real V3目前最佳方案 动漫风格转写实_2108720385909944322.json、图片生成/图生图/Krea2动漫转真人图生图处理生成工作流工具_2102514616378159106.json、图片生成/图生图/Krea2动漫转真人｜二次元图生图写真化｜真人质感还原度高_2102279427303501826.json、图片生成/图生图/Krea2漫剧角色资产一键生成工作流图生四视图_2100300485814218754.json、图片生成/图生图/动漫转真人V3 Krea2 图生图人物写实化转换_2094195206609526785.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Easy_QwenEdit2509`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `JjkText`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ColorCorrect` —— 3/5 个有
- `Lora Loader Stack (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageMergeNode` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Int` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `kkPadImageToCanvas` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（11/5 个样本）：Steps较低可能导致细节不足
