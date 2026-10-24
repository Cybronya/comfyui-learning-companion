---
name: text_to_image_sampler_clip_unet_204
type: Text To Image
frequency: 2
level: weak
coverage: 0.9245
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PrimitiveStringMultiline, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473.json, 图片生成/文生图/z-image-turbo-小而快的生图模型_1993815876799496193.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_204

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/(贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473.json、图片生成/文生图/z-image-turbo-小而快的生图模型_1993815876799496193.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PerturbedAttentionGuidance` —— 1/2 个有
- `String` —— 1/2 个有
- `TextConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 1192 | - | 2 | 60% |
| 高度 | 1104 | - | 2 | 84% |
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_3s_ode | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1192，样本不足，未给区间，2 个样本
- 高度 中位数 1104，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_3s_ode，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
