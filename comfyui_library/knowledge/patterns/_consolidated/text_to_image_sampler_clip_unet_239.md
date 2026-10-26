---
name: text_to_image_sampler_clip_unet_239
type: Text To Image
frequency: 2
level: weak
coverage: 0.7885
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImpactConditionalBranch, KSampler, PDRatioSelector, PrimitiveBoolean, PrimitiveStringMultiline, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/boogu_base_文生图-支持复杂提示词(可自动扩写)_2069358557987954689.json, 图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词（可自动扩写）​_2069356414316924929.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_239

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/boogu_base_文生图-支持复杂提示词(可自动扩写)_2069358557987954689.json、图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词（可自动扩写）​_2069356414316924929.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactConditionalBranch`
- `KSampler`
- `PDRatioSelector`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 980 | - | 2 | 96% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 22 | - | 2 | 18% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 980，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
