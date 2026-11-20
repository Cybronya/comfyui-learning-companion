---
name: unknown_workflow_controlnet_sampler_clip_47
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [ACN_AdvancedControlNetApply, AIO_Preprocessor, BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, CR Latent Batch Size, CheckpointLoaderSimple, ControlNetLoader, ImageResize+, KSamplerAdvanced, LineArtPreprocessor, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [平台全量/魅力创意-动漫转COS-高清版_1931683025577246721.json, 平台全量/魅力创意-动漫转COS-高清版_1977336965299359746.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/魅力创意-动漫转COS-高清版_1931683025577246721.json、平台全量/魅力创意-动漫转COS-高清版_1977336965299359746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `AIO_Preprocessor`
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPSetLastLayer`
- `CR Latent Batch Size`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `ImageResize+`
- `KSamplerAdvanced`
- `LineArtPreprocessor`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 40 | - | 2 | 100% |
| 采样算法 | 8 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
