---
name: unknown_workflow_sampler_clip_unet_286
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z 文生图（厨房模型）_2000808844013993985.json, 图片生成/图生图/z-image图像反推+高清增强_1996478328385191937.json, 图片生成/文生图/Qwen2512文生图工作流_2026224981025234945.json, 图片生成/文生图/Qwen3反推洗图_Z_image_seedvr2_1994317011379568642.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_286

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z 文生图（厨房模型）_2000808844013993985.json、图片生成/图生图/z-image图像反推+高清增强_1996478328385191937.json、图片生成/文生图/Qwen2512文生图工作流_2026224981025234945.json、图片生成/文生图/Qwen3反推洗图_Z_image_seedvr2_1994317011379568642.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `SeedVR2BlockSwap` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `SeedVR2ExtraArgs` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `JWStringConcat` —— 1/4 个有
- `LoadLoraOnly` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

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
