---
name: unknown_workflow_lora_sampler_clip_118
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6765
common_nodes: [Anything Everywhere, Anything Everywhere3, BasicGuider, BasicScheduler, CLIPSetLastLayer, CLIPTextEncode, CR Text, CR Text Concatenate, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, Int, KSamplerSelect, Lora Loader, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Float To String, CR Text, CR Text Concatenate, Create Grid Image from Batch, MathExpression|pysssss, easy batchAnything, easy forLoopEnd, easy forLoopStart, Lora Loader]
members: [图片生成/文生图/1964375837015425025.json, 图片生成/文生图/1964596165473878018.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1964375837015425025.json、图片生成/文生图/1964596165473878018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `Int`
- `KSamplerSelect`
- `Lora Loader`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CR Float To String` —— 1/2 个有
- `Create Grid Image from Batch` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImpactFloat` —— 1/2 个有
- `ImpactMakeImageBatch` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Float To String、CR Text、CR Text Concatenate、Create Grid Image from Batch、MathExpression|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
