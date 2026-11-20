---
name: text_to_image_lora_sampler_clip_634
type: Text To Image
frequency: 2
level: weak
coverage: 0.8685
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Image_2.1溶图工作流，图片融合其它图片处理方案_2109813671357669377.json, 图片生成/图生图/精修图生图工作流，提升图片细节与质感的专业修图方案_2104746115060031490.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_634

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen_Image_2.1溶图工作流，图片融合其它图片处理方案_2109813671357669377.json、图片生成/图生图/精修图生图工作流，提升图片细节与质感的专业修图方案_2104746115060031490.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 1/2 个有
- `DetailTransfer` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `PainterFluxImageEdit` —— 1/2 个有
- `QwenImage21BlockCacheT8` —— 1/2 个有
- `QwenImage21SageAttentionT8` —— 1/2 个有
- `QwenImage21SpectrumT8` —— 1/2 个有
- `TextEncodeQwenImage21GH` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
