---
name: unknown_workflow_lora_sampler_clip_286
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8385
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/🥎Kontext 一键多选风格迁移🤹_1939617697955233794.json, 图片生成/图生图/🥎【Kntext优质】优质白膜一键渲染照片图🤹_1948222111977472001.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_286

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/🥎Kontext 一键多选风格迁移🤹_1939617697955233794.json、图片生成/图生图/🥎【Kntext优质】优质白膜一键渲染照片图🤹_1948222111977472001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImpactConditionalBranch` —— 1/2 个有
- `ImpactStringSelector` —— 1/2 个有
- `KepStringLiteral` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `Random Number` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
