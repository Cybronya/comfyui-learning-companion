---
name: image_to_image_sampler_unet_vae_57
type: Image To Image
frequency: 3
level: strong
coverage: 0.820667
common_nodes: [CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetImageSize, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, PrimitiveFloat, QwenImage21Cache, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/豹豹喵呜制作，千问2.1服装提取&换装二合一工作流（PE版）_2112804585583759362.json, 图片生成/图生图/豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922.json, 图片生成/图生图/豹豹喵呜制作：真人动漫互转工作流（PE版）_2109906542836408322.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_57

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/豹豹喵呜制作，千问2.1服装提取&换装二合一工作流（PE版）_2112804585583759362.json、图片生成/图生图/豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922.json、图片生成/图生图/豹豹喵呜制作：真人动漫互转工作流（PE版）_2109906542836408322.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetImageSize`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `QwenImage21Cache`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageRemoveAlpha+` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveString` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `BatchImagesNode` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ColorMatchV2` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `Fast Muter (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: NumberCalculator` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `SDPoseDrawKeypoints` —— 1/3 个有
- `SDPoseKeypointExtractor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | linear_quadratic | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
