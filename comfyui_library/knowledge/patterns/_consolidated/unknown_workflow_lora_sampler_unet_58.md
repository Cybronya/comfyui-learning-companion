---
name: unknown_workflow_lora_sampler_unet_58
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.785333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, ExtractLinesByIndex, ImageFromBatch+, Int, JjkText, KSamplerSelect, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SaveVideo, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/一键生成一分钟产品宣传视频 文字版 Minimax H3_2092214066478665730.json, 视频生成/图生视频/一键生成一分钟双人播客视频 Minimax H3_2091884900138962946.json, 视频生成/文生视频/一键生成一分钟MV视频  Minimax H3_2092618341969129473.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/一键生成一分钟产品宣传视频 文字版 Minimax H3_2092214066478665730.json、视频生成/图生视频/一键生成一分钟双人播客视频 Minimax H3_2091884900138962946.json、视频生成/文生视频/一键生成一分钟MV视频  Minimax H3_2092618341969129473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `ExtractLinesByIndex`
- `ImageFromBatch+`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `String to Float` —— 2/3 个有
- `Float` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `Int Literal` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MiniMaxH3ImageToVideo` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `MiniMaxH3MotionContext` —— 1/3 个有
- `MiniMaxH3MotionContextTrim` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `ToFloat` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有
- `easy saveVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
