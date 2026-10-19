---
name: unknown_workflow_sampler_unet_vae_82
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.867125
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model]
members: [comfyui-workflow-templates-json/flux_redux_model_example.json, 图片生成/文生图/1907499231920156674.json, 图片生成/文生图/1932779421604401154.json, 图片生成/文生图/1951132199200432130.json, 图片生成/文生图/1966782963511930881.json, 图片生成/文生图/1966878604049125377.json, 图片生成/文生图/Redux角色一致性_1901277660763275265.json, 图片生成/文生图/双 redux 随意搭配_1890040180156379137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_redux_model_example.json、图片生成/文生图/1907499231920156674.json、图片生成/文生图/1932779421604401154.json、图片生成/文生图/1951132199200432130.json、图片生成/文生图/1966782963511930881.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `ModelSamplingFlux` —— 6/8 个有
- `EmptySD3LatentImage` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `CLIPVisionEncode` —— 3/8 个有
- `CLIPVisionLoader` —— 3/8 个有
- `EmptyLatentImage` —— 3/8 个有
- `StyleModelApply` —— 3/8 个有
- `StyleModelLoader` —— 3/8 个有
- `CLIPTextEncodeFlux` —— 1/8 个有
- `DeepTranslatorTextNode` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `LatentToWidthHeight` —— 1/8 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/8 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1360 | 3 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1360，3 个样本，取值集中（一致性 86%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: LoadJoyCaptionBeta1Model
