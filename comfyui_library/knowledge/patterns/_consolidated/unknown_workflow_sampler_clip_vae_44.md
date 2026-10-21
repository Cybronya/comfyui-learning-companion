---
name: unknown_workflow_sampler_clip_vae_44
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.904
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, NunchakuFluxDiTLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed, Text Multiline]
members: [图片生成/文生图/1922580731393097729.json, 图片生成/文生图/1982900132742070274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_44

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1922580731393097729.json、图片生成/文生图/1982900132742070274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `JJC_JoyCaption` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | - | 2 | 93% |
| 高度 | 1344 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 960，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 高度 中位数 1344，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、Text Multiline
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
