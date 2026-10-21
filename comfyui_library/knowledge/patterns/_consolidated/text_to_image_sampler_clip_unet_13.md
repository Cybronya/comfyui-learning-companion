---
name: text_to_image_sampler_clip_unet_13
type: Text To Image
frequency: 18
level: moderate
coverage: 0.946056
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2的可解释性(这个偏原理性，看我B站教程)_2073829223965487105.json, 图片生成/文生图/Krea2｜8步电影级人像基准_2072179087476609025.json, 图片生成/文生图/Krea2｜C站质感复刻版_2072175221502734338.json, 图片生成/文生图/Krea2｜KNP LoRA强风格版_2072199377187336194.json, 图片生成/文生图/Krea2｜三段式渲染文生图_2072217224156377090.json, 图片生成/文生图/Krea2｜强驱动人像增强版_2072175228620464130.json, 图片生成/文生图/Krea2｜文生图   生图快 风格多_2072714726299226113.json, "图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json", "图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json", 图片生成/文生图/Z-Image Re-Turbo_2073289018476941314.json, 图片生成/文生图/krea2+Lora文生图_2082750366432718849.json, 图片生成/文生图/krea2_ID13_v2_融合prompt_单分支_2086591602310602754.json, 图片生成/文生图/krea2_对比流_官方vsAnima配方_random_2086586562653024257.json, 图片生成/文生图/【GUGU】Z-image文生图工作流_1993849344558383105.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json, 图片生成/文生图/（自用-zhenzhen）Z-image-turbo文生图2K版_2019482059055566849.json, 图片生成/文生图/（贞贞-小情绪版）Z-image文生图V1_1999750941198909441.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Krea2的可解释性(这个偏原理性，看我B站教程)_2073829223965487105.json、图片生成/文生图/Krea2｜8步电影级人像基准_2072179087476609025.json、图片生成/文生图/Krea2｜C站质感复刻版_2072175221502734338.json、图片生成/文生图/Krea2｜KNP LoRA强风格版_2072199377187336194.json、图片生成/文生图/Krea2｜三段式渲染文生图_2072217224156377090.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 13/18 个有
- `ConditioningKrea2Rebalance` —— 9/18 个有
- `PreviewImage` —— 9/18 个有
- `FluxResolutionNode` —— 7/18 个有
- `easy promptLine` —— 3/18 个有
- `CR Prompt Text` —— 2/18 个有
- `DuckHideNode` —— 2/18 个有
- `LatentUpscaleBy` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1600 | 18 | 81% |
| 高度 | 1760 | 1024 - 2048 | 18 | 84% |
| 采样步数 | 8 | 6 - 30 | 16 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 94% |
| 调度器 | simple | - | 16 | 75% |
| 重绘幅度 | 1 | 0.45 - 1 | 16 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1600，18 个样本，取值集中（一致性 81%）
- 高度 中位数 1760，观测区间 1024 - 2048，18 个样本，取值集中（一致性 84%）
- 采样步数 中位数 8，观测区间 6 - 30，16 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 94%
- 调度器 最常用 simple，16 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，16 个样本，取值集中（一致性 86%）
- 高发问题（24/18 个样本）：Steps较低可能导致细节不足
