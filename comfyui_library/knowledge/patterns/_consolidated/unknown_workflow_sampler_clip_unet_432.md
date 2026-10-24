---
name: unknown_workflow_sampler_clip_unet_432
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.747
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CM_FloatToInt, CM_FloatUnaryOperation, CM_IntToFloat, CR Prompt Text, EmptyFlux2LatentImage, FL_ImageBatchToGrid, Flux2Scheduler, GetImageSizeAndCount, ImageListToBatch+, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveStringMultiline, RH_LLMAPI_NODE, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生图-单图多分镜自动-FLUX2-Klein_2017907866056794114.json, 图片生成/图生图/生图-单图循环生成多分镜-FLUX2-Klein_2017907859081666562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_432

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/生图-单图多分镜自动-FLUX2-Klein_2017907866056794114.json、图片生成/图生图/生图-单图循环生成多分镜-FLUX2-Klein_2017907859081666562.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_FloatUnaryOperation`
- `CM_IntToFloat`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `FL_ImageBatchToGrid`
- `Flux2Scheduler`
- `GetImageSizeAndCount`
- `ImageListToBatch+`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `GetLatentRangeFromBatch` —— 1/2 个有
- `GetLatentSizeAndCount` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `IntMath` —— 1/2 个有
- `JWIntegerToString` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `Qwen3_VQA_Plus` —— 1/2 个有
- `ToString` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
