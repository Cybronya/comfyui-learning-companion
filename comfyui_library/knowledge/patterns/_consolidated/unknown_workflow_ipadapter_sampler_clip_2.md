---
name: unknown_workflow_ipadapter_sampler_clip_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9425
common_nodes: [ApplyIPAdapterFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, IPAdapterFluxLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1910501378597552130.json, 图片生成/文生图/1919985800077836289.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1910501378597552130.json、图片生成/文生图/1919985800077836289.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyIPAdapterFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `IPAdapterFluxLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ChinesePrompt_Mix` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxResolutionNode` —— 1/2 个有
- `JjkShowText` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `scale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | - | 2 | 80% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
