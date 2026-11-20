---
name: unknown_workflow_sampler_unet_vae_309
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.670667
common_nodes: [BasicGuider, BasicScheduler, EmptyLatentImage, FluxGuidance, GetNode, Int, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux 模特一键换装_1996539076419403778.json, 平台全量/【企鹅AI】逃出画框📷_1857601930347622401.json, 平台全量/食谱原料可视化_1853096809848856577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_309

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux 模特一键换装_1996539076419403778.json、平台全量/【企鹅AI】逃出画框📷_1857601930347622401.json、平台全量/食谱原料可视化_1853096809848856577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetNode`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `Seed Everywhere` —— 2/3 个有
- `SplitSigmasDenoise` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `ImpactFloat` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `MergeLayers` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextCombinerSix` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| LoRA 模型强度 | 0.38 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
