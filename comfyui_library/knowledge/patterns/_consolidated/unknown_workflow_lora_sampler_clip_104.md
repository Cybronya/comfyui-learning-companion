---
name: unknown_workflow_lora_sampler_clip_104
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Translator, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Aspect Ratio, easy cleanGpuUsed, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1929527506691375106.json, 图片生成/文生图/1952660935905357826.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1929527506691375106.json、图片生成/文生图/1952660935905357826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RH_Translator`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Aspect Ratio` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 17.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、easy cleanGpuUsed、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
