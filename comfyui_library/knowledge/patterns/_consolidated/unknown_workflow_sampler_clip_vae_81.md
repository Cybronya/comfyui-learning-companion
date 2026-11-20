---
name: unknown_workflow_sampler_clip_vae_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FSampler, LayerUtility: PurgeVRAM, LayerUtility: TextJoin, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, TextInput_, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen千问 图生图海报洗图_1985596159756578818.json, 平台全量/电商产品海报+详情页 首图参考设计  Qwen-Image_1997201134026690561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen千问 图生图海报洗图_1985596159756578818.json、平台全量/电商产品海报+详情页 首图参考设计  Qwen-Image_1997201134026690561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FSampler`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextJoin`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `TextInput_`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JanusImage2Text` —— 1/2 个有
- `JanusImageUnderstanding` —— 1/2 个有
- `JanusModelLoader` —— 1/2 个有
- `LoadJanusModel` —— 1/2 个有
- `NunchakuQwenImageLoraLoader` —— 1/2 个有
- `NunchakuQwenImageLoraLoader1` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1440 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1440，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
