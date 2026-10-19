---
name: unknown_workflow_sampler_clip_vae_22
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.711
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: []
missing: [CR Simple Image Compare, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, easy cleanGpuUsed]
members: [图片生成/文生图/1924342937822687234.json, 图片生成/文生图/1924756669698330625.json, 图片生成/文生图/1943500030101626881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1924342937822687234.json、图片生成/文生图/1924756669698330625.json、图片生成/文生图/1943500030101626881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Simple Image Compare、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model
