---
name: image_to_image_sampler_unet_vae_11
type: Image To Image
frequency: 10
level: moderate
coverage: 0.882
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json, 图片生成/图生图/赛博玄幻·湘灵 女主｜图生图_2093230068645584897.json, 图片生成/图生图/赛博玄幻修仙者｜墨渊·图生图_2093285943129231361.json, 图片生成/图生图/赛博玄幻修仙者｜燕青·图生图_2093374930367901697.json, 图片生成/图生图/转现实场景qwen_2001592460314853378.json, 图片生成/图生图/镜头360_视角调整_1995146042221977602.json, 图片生成/图生图/🎯天下无腰Qwen Edit8步加速版（自用）_2021638917606346754.json, 图片生成/文生图/人物超新全方位视角转换（新版）_1999135446234001410.json, 图片生成/文生图/全新多角度视角转换（新版）_1999145049768198145.json, 视频生成/图生视频/qwen多视角转换工作流_1987730871912435714.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json、图片生成/图生图/赛博玄幻·湘灵 女主｜图生图_2093230068645584897.json、图片生成/图生图/赛博玄幻修仙者｜墨渊·图生图_2093285943129231361.json、图片生成/图生图/赛博玄幻修仙者｜燕青·图生图_2093374930367901697.json、图片生成/图生图/转现实场景qwen_2001592460314853378.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `CFGNorm` —— 6/10 个有
- `TextEncodeQwenImageEditPlus` —— 6/10 个有
- `CLIPTextEncode` —— 5/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `easy imageSize` —— 4/10 个有
- `CR Text` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `ModelPatchLoader` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `ZImageFunControlnet` —— 1/10 个有
- `图像缩放V2_孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 22 | 10 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 55% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 1 | 0.75 - 1 | 10 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 22，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.75 - 1，10 个样本，取值集中（一致性 88%）
