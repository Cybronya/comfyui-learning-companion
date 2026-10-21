---
name: unknown_workflow_sampler_clip_unet_242
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/室内建筑景观高质感文生图_2067220940961964033.json, 图片生成/文生图/文生图V2_2087151483677659138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_242

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/室内建筑景观高质感文生图_2067220940961964033.json、图片生成/文生图/文生图V2_2087151483677659138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoader|pysssss` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1564 | - | 2 | 69% |
| 高度 | 1472 | - | 2 | 70% |
| LoRA 模型强度 | 0.5 | - | 2 | 0% |
| LoRA 文本强度 | 0.51 | - | 2 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1564，样本不足，未给区间，2 个样本
- 高度 中位数 1472，样本不足，未给区间，2 个样本
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 0.51，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
