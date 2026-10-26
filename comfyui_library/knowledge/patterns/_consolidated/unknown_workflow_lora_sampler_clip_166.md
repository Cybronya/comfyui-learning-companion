---
name: unknown_workflow_lora_sampler_clip_166
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wojak极简动漫风格_2021151492207550466.json, 图片生成/文生图/国风唯美3D动漫风格_1994731961375657985.json, 数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json, 数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/wojak极简动漫风格_2021151492207550466.json、图片生成/文生图/国风唯美3D动漫风格_1994731961375657985.json、数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json、数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_TextConcatenate` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `QwenImageLatentAspectRatio` —— 2/4 个有
- `Seed Generator` —— 2/4 个有
- `Text` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 8 - 26 | 4 | 47% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | dpmpp_sde | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | 0.65 - 1 | 4 | 83% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 8 - 26，4 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.65 - 1，4 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
