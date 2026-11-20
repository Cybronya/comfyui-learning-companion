---
name: text_to_image_sampler_clip_unet_127
type: Text To Image
frequency: 6
level: moderate
coverage: 0.927167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json, 图片生成/文生图/官流Qwen-lmage-FP8中文版_1953112797149392898.json, 图片生成/文生图/文生图_2110627225245671426.json, 图片生成/文生图/文生图：Qwen-Image 8步加速出图V2_1986279659136569345.json, 图片生成/文生图/橘猫和胖虎搞笑图片抖音超火_1987561612901068801.json, 图片生成/文生图/潦草线条铅笔画_2017271179677016065.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_127

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json、图片生成/文生图/官流Qwen-lmage-FP8中文版_1953112797149392898.json、图片生成/文生图/文生图_2110627225245671426.json、图片生成/文生图/文生图：Qwen-Image 8步加速出图V2_1986279659136569345.json、图片生成/文生图/橘猫和胖虎搞笑图片抖音超火_1987561612901068801.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `Textbox` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `DyPE_FLUX` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | 8 - 30 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 35% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 864 | 720 - 1104 | 6 | 82% |
| 高度 | 1368 | 1280 - 1472 | 6 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，观测区间 8 - 30，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 864，观测区间 720 - 1104，6 个样本，取值集中（一致性 82%）
- 高度 中位数 1368，观测区间 1280 - 1472，6 个样本，取值集中（一致性 94%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
