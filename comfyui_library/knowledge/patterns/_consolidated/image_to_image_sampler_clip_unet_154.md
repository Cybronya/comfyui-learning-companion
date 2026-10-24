---
name: image_to_image_sampler_clip_unet_154
type: Image To Image
frequency: 3
level: weak
coverage: 0.950667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2洗图加速版_1994693315876560898.json, 图片生成/文生图/KSK Krea2｜原图重绘风格变身_2072199218311286785.json, 视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux2洗图加速版_1994693315876560898.json、图片生成/文生图/KSK Krea2｜原图重绘风格变身_2072199218311286785.json、视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `image_scale_pixel_v2` —— 2/3 个有
- `ConditioningKrea2Rebalance` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `Qwen3VLProcessor` —— 1/3 个有
- `VAELoaderKJ` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 3 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.46 - 0.7 | 3 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.46 - 0.7，3 个样本，取值集中（一致性 81%）
