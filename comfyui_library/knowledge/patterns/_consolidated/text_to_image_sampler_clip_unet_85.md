---
name: text_to_image_sampler_clip_unet_85
type: Text To Image
frequency: 8
level: strong
coverage: 0.924125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2的可解释性(这个偏原理性，看我B站教程)_2073829223965487105.json, 图片生成/文生图/Krea2｜8步电影级人像基准_2072179087476609025.json, 图片生成/文生图/Krea2｜C站质感复刻版_2072175221502734338.json, 图片生成/文生图/Krea2｜KNP LoRA强风格版_2072199377187336194.json, 图片生成/文生图/Krea2｜三段式渲染文生图_2072217224156377090.json, 图片生成/文生图/Krea2｜强驱动人像增强版_2072175228620464130.json, 图片生成/文生图/Krea2｜文生图   生图快 风格多_2072714726299226113.json, 图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Krea2的可解释性(这个偏原理性，看我B站教程)_2073829223965487105.json、图片生成/文生图/Krea2｜8步电影级人像基准_2072179087476609025.json、图片生成/文生图/Krea2｜C站质感复刻版_2072175221502734338.json、图片生成/文生图/Krea2｜KNP LoRA强风格版_2072199377187336194.json、图片生成/文生图/Krea2｜三段式渲染文生图_2072217224156377090.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `FluxResolutionNode` —— 6/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `DuckHideNode` —— 1/8 个有
- `LatentUpscaleBy` —— 1/8 个有
- `ModelAttentionBackend` —— 1/8 个有
- `SaveImageAdvanced` —— 1/8 个有
- `easy promptLine` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1920 | 8 | 70% |
| 高度 | 1536 | 1080 - 1536 | 8 | 89% |
| 采样步数 | 8 | 6 - 8 | 8 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 0.45 - 1 | 8 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1920，8 个样本
- 高度 中位数 1536，观测区间 1080 - 1536，8 个样本，取值集中（一致性 89%）
- 采样步数 中位数 8，观测区间 6 - 8，8 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，8 个样本，取值集中（一致性 80%）
- 高发问题（19/8 个样本）：Steps较低可能导致细节不足
