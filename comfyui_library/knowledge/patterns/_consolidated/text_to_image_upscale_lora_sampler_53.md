---
name: text_to_image_upscale_lora_sampler_53
type: Text To Image
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageUpscaleWithModel, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio, easy clearCacheAll, Latent Noise Injection]
members: [图片生成/文生图/1985605435585703937.json, 图片生成/文生图/Qwen-鬼刀画风_2005241079274373122.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1985605435585703937.json、图片生成/文生图/Qwen-鬼刀画风_2005241079274373122.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `GLM_Text_Chat` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Latent Noise Injection` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RandomLineFromText` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 2 | 33% |
| 宽度 | 1104 | - | 2 | 84% |
| 高度 | 1192 | - | 2 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 宽度 中位数 1104，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- 高度 中位数 1192，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio、easy clearCacheAll、Latent Noise Injection
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
