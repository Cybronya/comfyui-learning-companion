---
name: unknown_workflow_lora_sampler_vae_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1911779747029024769.json, 图片生成/文生图/1914962492102012929.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1911779747029024769.json、图片生成/文生图/1914962492102012929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `CLIPTextEncodeFlux` —— 1/2 个有
- `JjkShowText` —— 1/2 个有
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1408 | - | 2 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
