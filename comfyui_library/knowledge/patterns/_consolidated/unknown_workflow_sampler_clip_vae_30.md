---
name: unknown_workflow_sampler_clip_vae_30
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model]
members: [图片生成/文生图/1927591797424283649.json, 图片生成/文生图/1952670790871396354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1927591797424283649.json、图片生成/文生图/1952670790871396354.json）

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
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 57% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
