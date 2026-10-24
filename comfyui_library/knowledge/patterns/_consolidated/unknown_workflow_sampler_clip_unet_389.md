---
name: unknown_workflow_sampler_clip_unet_389
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.905
common_nodes: [BasicScheduler, CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, ModelSamplingFlux, SamplerCustom, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/lens 文生图_2061455655948611586.json, 图片生成/文生图/【遇见AI】Lens文生图模型基础流_2062821372929335298.json, 图片生成/文生图/微软lens文生图_2060639156652568577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_389

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/lens 文生图_2061455655948611586.json、图片生成/文生图/【遇见AI】Lens文生图模型基础流_2062821372929335298.json、图片生成/文生图/微软lens文生图_2060639156652568577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | 1080 - 1440 | 3 | 87% |
| 高度 | 1440 | 1440 - 1920 | 3 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1440，观测区间 1080 - 1440，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1440，观测区间 1440 - 1920，3 个样本，取值集中（一致性 86%）
