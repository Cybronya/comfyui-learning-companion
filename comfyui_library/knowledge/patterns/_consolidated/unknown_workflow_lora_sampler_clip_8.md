---
name: unknown_workflow_lora_sampler_clip_8
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.829636
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Note _O, CR Overlay Text, easy cleanGpuUsed]
members: [图片生成/文生图/1904465680211611649.json, 图片生成/文生图/1909669429062631425.json, 图片生成/文生图/1909854047942209538.json, 图片生成/文生图/1910140152096747522.json, 图片生成/文生图/1910229372215750657.json, 图片生成/文生图/1910272215428886529.json, 图片生成/文生图/1910318940827123714.json, 图片生成/文生图/1910558383181656066.json, 图片生成/文生图/1910647097245298690.json, 图片生成/文生图/1942467291403464705.json, 图片生成/文生图/1954518475970625537.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1904465680211611649.json、图片生成/文生图/1909669429062631425.json、图片生成/文生图/1909854047942209538.json、图片生成/文生图/1910140152096747522.json、图片生成/文生图/1910229372215750657.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/11 个有
- `ShowText|pysssss` —— 4/11 个有
- `RH_Translator` —— 3/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `CR Overlay Text` —— 1/11 个有
- `ColorMatch` —— 1/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `DeepTranslatorTextNode` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `Int` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `Note _O` —— 1/11 个有
- `UltimateSDUpscale` —— 1/11 个有
- `UpscaleModelLoader` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Note _O、CR Overlay Text、easy cleanGpuUsed
