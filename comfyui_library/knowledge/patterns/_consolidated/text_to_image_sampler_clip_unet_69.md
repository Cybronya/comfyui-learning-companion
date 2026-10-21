---
name: text_to_image_sampler_clip_unet_69
type: Text To Image
frequency: 7
level: moderate
coverage: 0.881286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json, 图片生成/文生图/Krea 2 分层控制_2072527998418513922.json, 图片生成/文生图/Krea2_2K_4K直出_超写实人像光影_2095323854578216962.json, 图片生成/文生图/Moody Krea 2 Mix -文生图_2084479377294843906.json, 图片生成/文生图/Z-IMAGE文生图_洗图小钢炮（开源王者）_1994224941826588674.json, 图片生成/文生图/Z-Image 反推描述生图_1993864386123071490.json, 图片生成/文生图/Z-Image-lora_1994678393864134657.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json、图片生成/文生图/Krea 2 分层控制_2072527998418513922.json、图片生成/文生图/Krea2_2K_4K直出_超写实人像光影_2095323854578216962.json、图片生成/文生图/Moody Krea 2 Mix -文生图_2084479377294843906.json、图片生成/文生图/Z-IMAGE文生图_洗图小钢炮（开源王者）_1994224941826588674.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadImage` —— 5/7 个有
- `RH_Captioner` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `easy int` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ConditioningKrea2Rebalance` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `Power Lora Loader (rgthree)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Text Multiline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | 512 - 2048 | 7 | 46% |
| 高度 | 1024 | 512 - 1920 | 7 | 50% |
| 采样步数 | 10 | 8 - 12 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 864，观测区间 512 - 2048，7 个样本，取值分散，一致性仅 46%
- 高度 中位数 1024，观测区间 512 - 1920，7 个样本，取值分散，一致性仅 50%
- 采样步数 中位数 10，观测区间 8 - 12，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
