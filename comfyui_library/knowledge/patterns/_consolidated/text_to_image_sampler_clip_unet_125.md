---
name: text_to_image_sampler_clip_unet_125
type: Text To Image
frequency: 5
level: strong
coverage: 0.967
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, Krea2StyleReference, Krea2TwoStyleReferences, Krea2TwoStyleTransfer, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-双图风格融合_2074080784067153921.json, 图片生成/图生图/Krea2-双图风格融合_2074854796380696578.json, 图片生成/图生图/Krea2-双图风格融合_2074858296485433345.json, 图片生成/图生图/Krea2-双图风格迁移（按风格生成）_2074492775432802306.json, 图片生成/图生图/VividMuse-Krea2风格迁移工作流合集_2083380797230379009.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Krea2-双图风格融合_2074080784067153921.json、图片生成/图生图/Krea2-双图风格融合_2074854796380696578.json、图片生成/图生图/Krea2-双图风格融合_2074858296485433345.json、图片生成/图生图/Krea2-双图风格迁移（按风格生成）_2074492775432802306.json、图片生成/图生图/VividMuse-Krea2风格迁移工作流合集_2083380797230379009.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `Krea2StyleReference`
- `Krea2TwoStyleReferences`
- `Krea2TwoStyleTransfer`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LayerUtility: ImageReel` —— 3/5 个有
- `LayerUtility: ImageReelComposit` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `Krea2StyleTransfer` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `TextEncodeKrea2OstrisEdit` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | 928 - 1024 | 5 | 95% |
| 高度 | 1160 | 1024 - 1280 | 5 | 93% |
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 928，观测区间 928 - 1024，5 个样本，取值集中（一致性 95%）
- 高度 中位数 1160，观测区间 1024 - 1280，5 个样本，取值集中（一致性 93%）
- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
