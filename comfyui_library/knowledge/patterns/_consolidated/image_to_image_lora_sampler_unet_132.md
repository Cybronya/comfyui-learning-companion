---
name: image_to_image_lora_sampler_unet_132
type: Image To Image
frequency: 6
level: moderate
coverage: 0.805667
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【楚心钟陌】返璞归真基础流_2019019903289794561.json, 图片生成/图生图/一键生成Hello Kitty中国风头像_2013190174729052161.json, 图片生成/图生图/千问2511 多角度自由切换_2009636132782350338.json, 图片生成/图生图/千问2511 多角度自由切换（提示词控制）_2009622014679588865.json, 图片生成/图生图/千问图片修改_2007817860055310337.json, 图片生成/图生图/通义千问2509双图编辑_1985768716262617090.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_132

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【楚心钟陌】返璞归真基础流_2019019903289794561.json、图片生成/图生图/一键生成Hello Kitty中国风头像_2013190174729052161.json、图片生成/图生图/千问2511 多角度自由切换_2009636132782350338.json、图片生成/图生图/千问2511 多角度自由切换（提示词控制）_2009622014679588865.json、图片生成/图生图/千问图片修改_2007817860055310337.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `Text` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy promptConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 0.99 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 0.8 - 1 | 6 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.99 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 92%）
- 风险：Prompt 约束强度(CFG) 观测到 0.99，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
