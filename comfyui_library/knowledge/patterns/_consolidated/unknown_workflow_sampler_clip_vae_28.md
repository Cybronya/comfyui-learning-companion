---
name: unknown_workflow_sampler_clip_vae_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CR Text, DeepTranslatorTextNode, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1910162390728568834.json, 图片生成/文生图/1911987218066669570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1910162390728568834.json、图片生成/文生图/1911987218066669570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CR Text`
- `DeepTranslatorTextNode`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SDXLAspectRatioSelector` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
