---
name: text_to_image_sampler_clip_unet_118
type: Text To Image
frequency: 6
level: moderate
coverage: 0.827667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image 反推描述生图_1993864386123071490.json, 图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json, 图片生成/文生图/Z-Image-De文生图_1997873304331517954.json, 图片生成/文生图/Z-Image-Turbo-洗图升级版（每次6张）_1994584620748378114.json, 图片生成/文生图/Z-Image-lora_1994678393864134657.json, 图片生成/文生图/krea2 文生图 工作流+全节点注释_2077385249922834434.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image 反推描述生图_1993864386123071490.json、图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json、图片生成/文生图/Z-Image-De文生图_1997873304331517954.json、图片生成/文生图/Z-Image-Turbo-洗图升级版（每次6张）_1994584620748378114.json、图片生成/文生图/Z-Image-lora_1994678393864134657.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `CR Text` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LatentUpscaleBy` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1220 | 512 - 1664 | 6 | 56% |
| 高度 | 1196 | 512 - 1920 | 6 | 51% |
| 采样步数 | 10 | 4 - 20 | 6 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 6 | 65% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 6 | 84% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1220，观测区间 512 - 1664，6 个样本
- 高度 中位数 1196，观测区间 512 - 1920，6 个样本
- 采样步数 中位数 10，观测区间 4 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，6 个样本，取值集中（一致性 84%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
