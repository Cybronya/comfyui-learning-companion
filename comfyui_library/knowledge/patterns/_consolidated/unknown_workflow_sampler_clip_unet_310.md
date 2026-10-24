---
name: unknown_workflow_sampler_clip_unet_310
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.89975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z 手持质感 文生图_2021145496873607169.json, 图片生成/文生图/Z-Image-Turbo LoRA 出图+放大_2018944118063370242.json, 图片生成/文生图/Z_image_seedvr2_1993859723476877313.json, 图片生成/文生图/文生图+LoRA+高清放大_2069642245782990849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_310

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z 手持质感 文生图_2021145496873607169.json、图片生成/文生图/Z-Image-Turbo LoRA 出图+放大_2018944118063370242.json、图片生成/文生图/Z_image_seedvr2_1993859723476877313.json、图片生成/文生图/文生图+LoRA+高清放大_2069642245782990849.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `SeedVR2ExtraArgs` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `LoadLoraOnly` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
