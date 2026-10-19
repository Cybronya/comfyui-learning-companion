---
name: unknown_workflow_sampler_clip_unet_66
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.75325
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR SDXL Aspect Ratio, SDXL Resolutions (JPS)]
members: [图片生成/文生图/1951090280026058754.json, 图片生成/文生图/1955480075464577026.json, 图片生成/文生图/1959355153205899265.json, 图片生成/文生图/1980452246066540546.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1951090280026058754.json、图片生成/文生图/1955480075464577026.json、图片生成/文生图/1959355153205899265.json、图片生成/文生图/1980452246066540546.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

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
- `EmptyLatentImage` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SDXL Resolutions (JPS)` —— 1/4 个有
- `SeargePromptCombiner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 22 | 4 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 22，4 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio、SDXL Resolutions (JPS)
