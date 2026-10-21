---
name: unknown_workflow_sampler_clip_unet_251
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.89
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, DF_Integer, JjkText, KSampler, MathExpression|pysssss, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader, Wan22ImageToVideoLatent]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1950069954751152129.json, 视频生成/文生视频/1950094689354563586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_251

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1950069954751152129.json、视频生成/文生视频/1950094689354563586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `DF_Integer`
- `JjkText`
- `KSampler`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `Wan22ImageToVideoLatent`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
