---
name: image_to_image_lora_sampler_unet_151
type: Image To Image
frequency: 4
level: strong
coverage: 0.96075
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511姿态迁移_2012123669828472833.json, 图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json, 图片生成/图生图/Qwen-Edit-2511真实转动漫风V2_2015683033436790786.json, 图片生成/图生图/【🛫书墨】姿态构图迁移v3-anypose_2010972516814168065.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511姿态迁移_2012123669828472833.json、图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json、图片生成/图生图/Qwen-Edit-2511真实转动漫风V2_2015683033436790786.json、图片生成/图生图/【🛫书墨】姿态构图迁移v3-anypose_2010972516814168065.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `ColorCorrect` —— 2/4 个有
- `ImageBlend` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `SDPoseOODLoader` —— 2/4 个有
- `SDPoseOODProcessor` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `KOOK_SaveJPGImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
