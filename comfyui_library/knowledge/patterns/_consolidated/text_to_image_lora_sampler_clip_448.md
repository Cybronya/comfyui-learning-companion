---
name: text_to_image_lora_sampler_clip_448
type: Text To Image
frequency: 4
level: strong
coverage: 0.83675
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, GetImageSize, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveFloat, QwenImage21Cache, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538.json, 图片生成/图生图/千问2.1服装提取换装二合一 虚拟换装PE版处理工具_2113352556004069377.json, 图片生成/图生图/真人动漫互转图生图工作流PE版，写实二次元一键切换_2110461219638435842.json, 图片生成/图生图/真人动漫互转图生图工作流PE版，写实二次元一键切换_2113469138810261506.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_448

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538.json、图片生成/图生图/千问2.1服装提取换装二合一 虚拟换装PE版处理工具_2113352556004069377.json、图片生成/图生图/真人动漫互转图生图工作流PE版，写实二次元一键切换_2110461219638435842.json、图片生成/图生图/真人动漫互转图生图工作流PE版，写实二次元一键切换_2113469138810261506.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageRemoveAlpha+` —— 3/4 个有
- `JoinStrings` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `PrimitiveString` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `ColorMatchV2` —— 2/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `BatchImagesNode` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `Fast Muter (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerUtility: NumberCalculator` —— 1/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/4 个有
- `SDPoseDrawKeypoints` —— 1/4 个有
- `SDPoseKeypointExtractor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
