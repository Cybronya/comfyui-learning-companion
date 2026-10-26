---
name: unknown_workflow_lora_sampler_clip_300
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ApplyFBCacheOnModel, ArgosTranslateTextNode, BasicScheduler, CFGGuider, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, PAGAttention, PreviewTextNode, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux细节增强艺术Lora图生图_1879829555153432577.json, 图片生成/文生图/Flux细节增强艺术Lora文生图_1879815572992258050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_300

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux细节增强艺术Lora图生图_1879829555153432577.json、图片生成/文生图/Flux细节增强艺术Lora文生图_1879815572992258050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `ArgosTranslateTextNode`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PAGAttention`
- `PreviewTextNode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AegisFlow/aflogo` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 720 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
