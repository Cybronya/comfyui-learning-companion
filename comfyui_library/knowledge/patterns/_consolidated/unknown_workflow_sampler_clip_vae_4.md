---
name: unknown_workflow_sampler_clip_vae_4
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.858154
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Note _O]
members: [图片生成/文生图/1909949768628666370.json, 图片生成/文生图/1910140152096747522.json, 图片生成/文生图/1910229372215750657.json, 图片生成/文生图/1910272215428886529.json, 图片生成/文生图/1910318940827123714.json, 图片生成/文生图/1910558383181656066.json, 图片生成/文生图/1910647097245298690.json, 图片生成/文生图/1911400407372103681.json, 图片生成/文生图/1923752379836264449.json, 图片生成/文生图/1927931879364935681.json, 图片生成/文生图/1929809956793434113.json, 图片生成/文生图/1947113386972327938.json, 图片生成/文生图/1954524753786761217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1909949768628666370.json、图片生成/文生图/1910140152096747522.json、图片生成/文生图/1910229372215750657.json、图片生成/文生图/1910272215428886529.json、图片生成/文生图/1910318940827123714.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 12/13 个有
- `ModelSamplingFlux` —— 12/13 个有
- `NunchakuFluxLoraLoader` —— 12/13 个有
- `EmptySD3LatentImage` —— 10/13 个有
- `PreviewImage` —— 6/13 个有
- `EmptyLatentImage` —— 3/13 个有
- `ShowText|pysssss` —— 2/13 个有
- `ColorMatch` —— 1/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `DeepTranslatorTextNode` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `Note _O` —— 1/13 个有
- `RH_LLMAPI_NODE` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `UltimateSDUpscale` —— 1/13 个有
- `UpscaleModelLoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1536 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Note _O
