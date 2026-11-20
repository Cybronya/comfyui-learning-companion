---
name: unknown_workflow_sampler_107
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.933
common_nodes: [CreateVideo, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageSize+, GetVideoComponents, Image Comparer (rgthree), ImageScaleBy, JWImageExtractFromBatch, LoadVideo, SaveVideo, Seed Generator, easy int, easy seed]
problems: []
missing: []
members: [平台全量/FlashVSR视频高清放大修复低显存长视频支持优化版_1987091235418648577.json, "视频生成/文生视频/FlashVSR视频放大,低显存&长视频支持_1981634759593992194.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_107

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FlashVSR视频高清放大修复低显存长视频支持优化版_1987091235418648577.json、视频生成/文生视频/FlashVSR视频放大,低显存&长视频支持_1981634759593992194.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageSize+`
- `GetVideoComponents`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `JWImageExtractFromBatch`
- `LoadVideo`
- `SaveVideo`
- `Seed Generator`
- `easy int`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.27337e+09 | - | 2 | 100% |
| Prompt 约束强度(CFG) | fixed | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.27337e+09，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 最常用 fixed，2 个样本，一致性 100%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.27337e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 7，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
