---
name: text_to_image_upscale_sampler_clip_42
type: Text To Image
frequency: 2
level: weak
coverage: 0.867
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, ConditioningZeroOut, EmptyLatentImage, GetImageSize, ImpactInt, KSampler, LoadImage, Qwen3VL_Advanced, SaveImage, ShowText|pysssss, String Literal, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE高清超强生图_1995183324647841794.json, 图片生成/文生图/z-image手动+反推+高清超强生图_1995144168718655490.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE高清超强生图_1995183324647841794.json、图片生成/文生图/z-image手动+反推+高清超强生图_1995144168718655490.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `Qwen3VL_Advanced`
- `SaveImage`
- `ShowText|pysssss`
- `String Literal`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
