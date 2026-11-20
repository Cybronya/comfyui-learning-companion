---
name: unknown_workflow_lora_sampler_unet_95
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.748889
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/H3-TR极速双采pika版（修复网格）_2117488183788261377.json, 平台全量/H3_单图_Pika_Relay二次元anime sr放大_2118946582942011393.json, 平台全量/H3_多模态视频_Pika_Relay二次元放大_2117980988839120897.json, 平台全量/【MiniMax H3】Pika+二采_优化版_2119268786401529857.json, 平台全量/【MiniMax H3】直出30秒！！！Pika加速_2118612467529117697.json, 平台全量/【MiniMax H3】直出30秒！！！Pika加速_2118965865478705153.json, 平台全量/【MiniMax H3】直出30秒！！！Pika加速_2118982190116724737.json, 视频生成/图生视频/H3-TR极速双采pika版（修复网格）_2116043302754672642.json, 视频生成/图生视频/H3-极速TR双采-文戏流_2115617446710300673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_95

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/H3-TR极速双采pika版（修复网格）_2117488183788261377.json、平台全量/H3_单图_Pika_Relay二次元anime sr放大_2118946582942011393.json、平台全量/H3_多模态视频_Pika_Relay二次元放大_2117980988839120897.json、平台全量/【MiniMax H3】Pika+二采_优化版_2119268786401529857.json、平台全量/【MiniMax H3】直出30秒！！！Pika加速_2118612467529117697.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 8/9 个有
- `BlockSparseAttention` —— 7/9 个有
- `MiniMaxChunkFeedForward` —— 7/9 个有
- `MiniMaxLowVRAMAttention` —— 7/9 个有
- `ModelAttentionBackend` —— 7/9 个有
- `ModelPreviewOverrideKJ` —— 7/9 个有
- `MiniMaxH3SigmaShift` —— 6/9 个有
- `ExtendIntermediateSigmas` —— 5/9 个有
- `Any Switch (rgthree)` —— 4/9 个有
- `BasicScheduler` —— 4/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `DisableNoise` —— 4/9 个有
- `ImageScale` —— 4/9 个有
- `MiniMaxH3LatentUpscaleCombined` —— 4/9 个有
- `忽略多组孤海` —— 4/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `FastDeropeTAELoader` —— 2/9 个有
- `H3RelayHires` —— 2/9 个有
- `ImageCrop` —— 2/9 个有
- `LTXVSeparateAVLatent` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `SplitSigmas` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有
- `VHS_LoadVideoFFmpeg` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
