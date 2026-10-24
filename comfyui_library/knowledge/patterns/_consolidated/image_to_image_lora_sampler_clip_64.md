---
name: image_to_image_lora_sampler_clip_64
type: Image To Image
frequency: 5
level: strong
coverage: 0.8882
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoader, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像优化高清  Wan2.2 VS SRPO_1987454677631610882.json, 图片生成/图生图/洗图-图像高清，增加画质 Wan2.2 & SRPO_1988094555440443393.json, 图片生成/图生图/洗图-图像高清，增加画质 Wan2.2 & SRPO_1993299242611572738.json, 图片生成/图生图/洗图_1989678050919018497.json, 图片生成/文生图/Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图像优化高清  Wan2.2 VS SRPO_1987454677631610882.json、图片生成/图生图/洗图-图像高清，增加画质 Wan2.2 & SRPO_1988094555440443393.json、图片生成/图生图/洗图-图像高清，增加画质 Wan2.2 & SRPO_1993299242611572738.json、图片生成/图生图/洗图_1989678050919018497.json、图片生成/文生图/Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `Float` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `ImageScaleToMegapixels` —— 4/5 个有
- `ImageUpscaleWithModel` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.7 | 0.7 - 0.7 | 5 | 100% |
| LoRA 文本强度 | 0.7 | 0.7 - 0.7 | 5 | 100% |
| 采样步数 | 10 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s | - | 5 | 60% |
| 调度器 | bong_tangent | - | 5 | 60% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 5 | 39% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.7，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，观测区间 0.7 - 0.7，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，5 个样本，一致性 60%
- 调度器 最常用 bong_tangent，5 个样本，一致性 60%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，5 个样本，取值分散，一致性仅 39%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
