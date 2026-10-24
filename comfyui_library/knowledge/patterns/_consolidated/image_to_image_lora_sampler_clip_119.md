---
name: image_to_image_lora_sampler_clip_119
type: Image To Image
frequency: 2
level: weak
coverage: 0.824
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, Int, KSampler, LatentCutToBatch, LatentFromBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/10倍加速Qwen Image Layered千问分层模型（图像分解为多个 RGBA 层）-试玩版_2002225813649014786.json, 图片生成/图生图/Qwen+Layerd分层图生图&文生图一键切换加速工作流_2074068495398170625.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/10倍加速Qwen Image Layered千问分层模型（图像分解为多个 RGBA 层）-试玩版_2002225813649014786.json、图片生成/图生图/Qwen+Layerd分层图生图&文生图一键切换加速工作流_2074068495398170625.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `Int`
- `KSampler`
- `LatentCutToBatch`
- `LatentFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `SimpleComparison+` —— 1/2 个有
- `SimpleMathCondition+` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | - | 2 | 36% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
