---
name: text_to_image_sampler_clip_unet_244
type: Text To Image
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/动漫anima正式版 文生图_2056020880639176705.json, 图片生成/文生图/文生图_2016773236125605889.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_244

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/动漫anima正式版 文生图_2056020880639176705.json、图片生成/文生图/文生图_2016773236125605889.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21.5 | - | 2 | 14% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1344 | - | 2 | 57% |
| 高度 | 1204 | - | 2 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 21.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1344，样本不足，未给区间，2 个样本
- 高度 中位数 1204，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
