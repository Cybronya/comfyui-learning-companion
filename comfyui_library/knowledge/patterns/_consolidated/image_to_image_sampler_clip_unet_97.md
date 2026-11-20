---
name: image_to_image_sampler_clip_unet_97
type: Image To Image
frequency: 5
level: weak
coverage: 0.871
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image图生图+自动反推提示词_2049742527770710018.json, 图片生成/图生图/Z-Image图生图-一键转写实风格_2053871796142788609.json, 图片生成/图生图/Z-image-base蛋挞图生图_2029062811237752834.json, 图片生成/图生图/qwen2512_图生图（洗图）工作流bf16版本_2011980103621812226.json, 图片生成/图生图/千府AI-ZIMAGE高清修复工作流_2004054470956883970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-Image图生图+自动反推提示词_2049742527770710018.json、图片生成/图生图/Z-Image图生图-一键转写实风格_2053871796142788609.json、图片生成/图生图/Z-image-base蛋挞图生图_2029062811237752834.json、图片生成/图生图/qwen2512_图生图（洗图）工作流bf16版本_2011980103621812226.json、图片生成/图生图/千府AI-ZIMAGE高清修复工作流_2004054470956883970.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `easy imageScaleDownToSize` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CR Latent Batch Size` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 40 | 5 | 15% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 4 | 5 | 46% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 0.5 | 0.1 - 0.8 | 5 | 39% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 40，5 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 4，5 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 0.5，观测区间 0.1 - 0.8，5 个样本，取值分散，一致性仅 39%
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
