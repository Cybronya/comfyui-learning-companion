---
name: text_to_image_upscale_sampler_clip_28
type: Text To Image
frequency: 3
level: strong
coverage: 0.887333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UNETLoader, Upscale Model Loader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image图生图洗稿超真实写实人物_1999362061907918849.json, 图片生成/图生图/Z-image超极速图生图（魔君降临--拳打nunchaku，脚踢Flux2）_1994269913843957762.json, 图片生成/文生图/Z-image超极速文生图（魔君降临--拳打nunchaku，脚踢Flux2）_1994262703730524162.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image图生图洗稿超真实写实人物_1999362061907918849.json、图片生成/图生图/Z-image超极速图生图（魔君降临--拳打nunchaku，脚踢Flux2）_1994269913843957762.json、图片生成/文生图/Z-image超极速文生图（魔君降临--拳打nunchaku，脚踢Flux2）_1994262703730524162.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `easy showAnything` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 768 - 1080 | 3 | 83% |
| 高度 | 1024 | 1024 - 1920 | 3 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1080，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 1024 - 1920，3 个样本
