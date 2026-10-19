---
name: unknown_workflow_sampler_clip_vae_21
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.764
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, Note Plus (mtb), NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, Note Plus (mtb), CR Prompt Text, easy promptConcat, CR Combine Prompt]
members: [图片生成/文生图/1910667121410437122.json, 图片生成/文生图/1915461235243159553.json, 图片生成/文生图/1922302399132684289.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1910667121410437122.json、图片生成/文生图/1915461235243159553.json、图片生成/文生图/1922302399132684289.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `Note Plus (mtb)`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Combine Prompt` —— 1/3 个有
- `HiDreamSampler` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Note Plus (mtb)、CR Prompt Text、easy promptConcat、CR Combine Prompt
