---
name: unknown_workflow_sampler_clip_unet_309
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9365
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Y-flux1_krea_dev-workflow_1980452246066540546.json, 图片生成/文生图/flux_dev_full_极致质量文生图_1959355153205899265.json, 图片生成/文生图/flux标准工作流_1985548530460860417.json, 图片生成/文生图/人物一致性1.0_1917390442533687298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_309

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Y-flux1_krea_dev-workflow_1980452246066540546.json、图片生成/文生图/flux_dev_full_极致质量文生图_1959355153205899265.json、图片生成/文生图/flux标准工作流_1985548530460860417.json、图片生成/文生图/人物一致性1.0_1917390442533687298.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/4 个有
- `CLIPAttentionMultiply` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `SDXL Resolutions (JPS)` —— 1/4 个有
- `SeargePromptCombiner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 768 - 1920 | 3 | 60% |
| 高度 | 1024 | 1024 - 1080 | 3 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1920，3 个样本
- 高度 中位数 1024，观测区间 1024 - 1080，3 个样本，取值集中（一致性 97%）
