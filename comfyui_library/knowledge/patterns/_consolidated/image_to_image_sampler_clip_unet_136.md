---
name: image_to_image_sampler_clip_unet_136
type: Image To Image
frequency: 3
level: weak
coverage: 0.900667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein动作迁移_2012315513514369025.json, 图片生成/图生图/Flux2-klein动漫角色转真人_2012456402224160769.json, 图片生成/图生图/Qwen 2512 重绘_洗图_2007990679003209729.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2-klein动作迁移_2012315513514369025.json、图片生成/图生图/Flux2-klein动漫角色转真人_2012456402224160769.json、图片生成/图生图/Qwen 2512 重绘_洗图_2007990679003209729.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有
- `PIP_图像联结` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Textbox` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 9 | 3 | 0% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 0.8 | - | 2 | 75% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 9，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
