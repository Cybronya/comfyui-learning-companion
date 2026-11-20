---
name: image_to_image_sampler_clip_unet_95
type: Image To Image
frequency: 5
level: weak
coverage: 0.9278
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image，反推洗图_1987161071591034881.json, 图片生成/图生图/Qwen-Image 图生图_1958119913732919297.json, 图片生成/图生图/Qwen-Image 手动遮罩局部修改_1958468974650540033.json, 图片生成/图生图/qwen编辑线稿转效果图_1958881314973888513.json, 视频生成/图生视频/水墨插画qwen_2037441276806701058.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image，反推洗图_1987161071591034881.json、图片生成/图生图/Qwen-Image 图生图_1958119913732919297.json、图片生成/图生图/Qwen-Image 手动遮罩局部修改_1958468974650540033.json、图片生成/图生图/qwen编辑线稿转效果图_1958881314973888513.json、视频生成/图生视频/水墨插画qwen_2037441276806701058.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `easy imageConcat` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 20 | 5 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 39% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 40% |
| 重绘幅度 | 0.8 | 0.71 - 1 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 20，5 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 40%
- 重绘幅度 中位数 0.8，观测区间 0.71 - 1，5 个样本，取值集中（一致性 86%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
