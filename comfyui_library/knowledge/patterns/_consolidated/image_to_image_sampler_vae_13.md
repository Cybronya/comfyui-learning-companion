---
name: image_to_image_sampler_vae_13
type: Image To Image
frequency: 9
level: strong
coverage: 0.408667
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy bookmark]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AIRix 短剧二创 一致性人物V2_1998447779892617217.json, 图片生成/图生图/AIRix-短剧二创-一致性人物V2_1987918335201447937.json, 图片生成/图生图/Qwen-Edit-2509 IP角色多视图工作流_2091500667302146049.json, 图片生成/图生图/Qwen-Edit-2509 人物角色多视图工作流_2091492663307624449.json, 图片生成/图生图/Qwen-一张图出人物全角度_1978412285632860161.json, 图片生成/图生图/V2人物全角度生成器（高度一致性）_2032291719257006082.json, 图片生成/图生图/多视角非循环（女版）_1988907373530066946.json, 图片生成/图生图/多视角非循环（男版）_1999392680000057346.json, 图片生成/文生图/一张图出人物全角度V1-人物一致性-阿硕_1978121708173451266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/AIRix 短剧二创 一致性人物V2_1998447779892617217.json、图片生成/图生图/AIRix-短剧二创-一致性人物V2_1987918335201447937.json、图片生成/图生图/Qwen-Edit-2509 IP角色多视图工作流_2091500667302146049.json、图片生成/图生图/Qwen-Edit-2509 人物角色多视图工作流_2091492663307624449.json、图片生成/图生图/Qwen-一张图出人物全角度_1978412285632860161.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 9 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy bookmark`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 8/9 个有
- `ImageFlip` —— 7/9 个有
- `Label (rgthree)` —— 5/9 个有
- `Mute / Bypass Repeater (rgthree)` —— 5/9 个有
- `Anything Everywhere3` —— 4/9 个有
- `CheckpointLoaderSimple` —— 4/9 个有
- `CompressImages` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `ImageBatchMulti` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `Mute / Bypass Relay (rgthree)` —— 4/9 个有
- `PreviewAny` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `PurgeVRAM_UTK` —— 4/9 个有
- `UNETLoader` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 3/9 个有
- `GeminiImageNode` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 960 | 720 - 960 | 9 | 86% |
| 高度 | 1304 | 1024 - 1384 | 9 | 88% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 0.8 | 0.6 - 0.8 | 4 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 132/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 960，观测区间 720 - 960，9 个样本，取值集中（一致性 86%）
- 高度 中位数 1304，观测区间 1024 - 1384，9 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，观测区间 0.6 - 0.8，4 个样本，取值集中（一致性 88%）
- 高发问题（132/9 个样本）：Steps较低可能导致细节不足
