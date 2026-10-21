---
name: unknown_workflow_sampler_vae_42
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.82
common_nodes: [CLIPLoader, EmptyLatentImage, EnhancedLoadDiffusionModel, Fast Groups Bypasser (rgthree), FastGroupsBypassSwitch, JjkText, KSamplerCacheable, LoadImage, PreviewImage, QwenImage21Cache, QwenPERewriteT8, ResolutionSelector, SaveImage, ShowAnything|Mie, TextEncodeQwenImage21, VAEDecode, VAELoader_Any]
problems: []
missing: [ShowAnything|Mie]
members: [图片生成/图生图/2103803289958703105.json, 图片生成/文生图/Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2103803289958703105.json、图片生成/文生图/Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `Fast Groups Bypasser (rgthree)`
- `FastGroupsBypassSwitch`
- `JjkText`
- `KSamplerCacheable`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `ShowAnything|Mie`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `VAELoader_Any`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 50 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
