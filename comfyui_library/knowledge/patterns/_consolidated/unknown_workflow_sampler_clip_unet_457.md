---
name: unknown_workflow_sampler_clip_unet_457
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/joycaptionBetaOne反推_1927591797424283649.json, 图片生成/文生图/低显存Flux文生图工作流_1900451456095498241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_457

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/joycaptionBetaOne反推_1927591797424283649.json、图片生成/文生图/低显存Flux文生图工作流_1900451456095498241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有

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
