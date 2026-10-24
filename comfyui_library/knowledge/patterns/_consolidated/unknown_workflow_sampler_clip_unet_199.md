---
name: unknown_workflow_sampler_clip_unet_199
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.928714
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json, 图片生成/文生图/image_z_image_turbo造像 去除ai油腻味文生图_1996224077834633218.json, 图片生成/文生图/image_z_turbo_文生图_原版无Lora_2004484063744454657.json, 图片生成/文生图/logo生成器+QwenImage=艾橘溪_1954145034784391169.json, 图片生成/文生图/中文书法字体设计 - 媲美即梦 - Qwen-Image文生图_1953065521521618946.json, 图片生成/文生图/中文书法字体设计 -文生图-中文字体logo-书法字体设计-艺术字_2021848205499043842.json, 图片生成/文生图/千问Qwen-image中文书法字体设计 - 媲美即梦_2002775003546415106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_199

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json、图片生成/文生图/image_z_image_turbo造像 去除ai油腻味文生图_1996224077834633218.json、图片生成/文生图/image_z_turbo_文生图_原版无Lora_2004484063744454657.json、图片生成/文生图/logo生成器+QwenImage=艾橘溪_1954145034784391169.json、图片生成/文生图/中文书法字体设计 - 媲美即梦 - Qwen-Image文生图_1953065521521618946.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `EmptySD3LatentImage` —— 6/7 个有
- `Text Multiline` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CR SDXL Aspect Ratio` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `LoadImage` —— 1/7 个有
- `SDXLEmptyLatentSizePicker+` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 25 | 7 | 68% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 7 | 40% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，7 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
