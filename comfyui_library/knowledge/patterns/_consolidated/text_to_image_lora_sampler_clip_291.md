---
name: text_to_image_lora_sampler_clip_291
type: Text To Image
frequency: 7
level: strong
coverage: 0.904286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3开源版图片编辑｜多图合成换背景创意生图_2097158027400007682.json, 图片生成/图生图/MiniMax H3开源版图片编辑｜多图编辑换背景创意生图人物特效_2089713767801245698.json, 图片生成/图生图/MiniMax_H3开源版图片编辑｜多图编辑换背景创意生图_2097098299735101441.json, 图片生成/图生图/krea2自用图生图｜图像编辑一键生成直出_2092320745304182786.json, 图片生成/图生图/图片视频图片编辑｜MiniMax_H3图生图换背景_2092940233808637954.json, 图片生成/图生图/自用图生图工具｜krea2低幅度重绘一键出图_2092549239720210433.json, 图片生成/文生图/2K加速版文生图｜MiniMaxH3开源美少女写实出图_2089063557869694977.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_291

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/MiniMax H3开源版图片编辑｜多图合成换背景创意生图_2097158027400007682.json、图片生成/图生图/MiniMax H3开源版图片编辑｜多图编辑换背景创意生图人物特效_2089713767801245698.json、图片生成/图生图/MiniMax_H3开源版图片编辑｜多图编辑换背景创意生图_2097098299735101441.json、图片生成/图生图/krea2自用图生图｜图像编辑一键生成直出_2092320745304182786.json、图片生成/图生图/图片视频图片编辑｜MiniMax_H3图生图换背景_2092940233808637954.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `EasyCache` —— 5/7 个有
- `ImageFromBatch` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `LayerUtility: ImageReel` —— 4/7 个有
- `LayerUtility: ImageReelComposit` —— 4/7 个有
- `MiniMaxH3ReferenceToVideo` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `MiniMaxH3ImageToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
