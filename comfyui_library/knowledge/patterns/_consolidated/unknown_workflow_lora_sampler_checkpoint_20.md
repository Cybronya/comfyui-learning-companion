---
name: unknown_workflow_lora_sampler_checkpoint_20
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问单图编辑AIOv5 （Ai应用可进工作流）_2001328771955388418.json, 图片生成/图生图/千问图像编辑基础工作流_1988144496988872705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千问单图编辑AIOv5 （Ai应用可进工作流）_2001328771955388418.json、图片生成/图生图/千问图像编辑基础工作流_1988144496988872705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Filter Adjustments` —— 1/2 个有
- `Image Rotate Hue` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Int` —— 1/2 个有
- `SaveLatent` —— 1/2 个有
- `TT_img_enc_v2` —— 1/2 个有
- `TwoWaySwitch` —— 1/2 个有
- `VHS_Unbatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 50% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
