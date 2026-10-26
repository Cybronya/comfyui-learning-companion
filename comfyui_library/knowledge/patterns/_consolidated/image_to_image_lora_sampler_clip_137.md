---
name: image_to_image_lora_sampler_clip_137
type: Image To Image
frequency: 2
level: weak
coverage: 0.762
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json, 图片生成/图生图/f2K+Zimage-美感提升-动漫转真人_2046185008498479106.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json、图片生成/图生图/f2K+Zimage-美感提升-动漫转真人_2046185008498479106.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `CR Conditioning Input Switch` —— 1/2 个有
- `CR Image Input Switch (4 way)` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.8 | - | 2 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
