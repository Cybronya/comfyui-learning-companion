---
name: unknown_workflow_video_lora_sampler_409
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.872
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/pika+minimax二采_2116691928606662657.json, 图片生成/图生图/道真数字人多场景通用版_2112188090025598978.json, 图片生成/图生图/🦞天下武功，唯快不破-H3最强打斗工作流_2111630069474086913.json, 视频生成/图生视频/10.16高尚最强武打（minimax最强动作）_2110787369631834114.json, 视频生成/图生视频/pika+minimax二采_2116414380308000770.json, 视频生成/图生视频/pika+minimax二采_2116662273380012033.json, 视频生成/文生视频/H3官流（单采极速文戏）_2106642679642812418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_409

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/pika+minimax二采_2116691928606662657.json、图片生成/图生图/道真数字人多场景通用版_2112188090025598978.json、图片生成/图生图/🦞天下武功，唯快不破-H3最强打斗工作流_2111630069474086913.json、视频生成/图生视频/10.16高尚最强武打（minimax最强动作）_2110787369631834114.json、视频生成/图生视频/pika+minimax二采_2116414380308000770.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 5/7 个有
- `MiniMaxH3SigmaShift` —— 5/7 个有
- `BasicScheduler` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `DisableNoise` —— 3/7 个有
- `MiniMaxChunkFeedForward` —— 3/7 个有
- `MiniMaxH3LatentUpscaleCombined` —— 3/7 个有
- `MiniMaxLowVRAMAttention` —— 3/7 个有
- `AudioConcat` —— 2/7 个有
- `EasyCache` —— 2/7 个有
- `ExtendIntermediateSigmas` —— 2/7 个有
- `GetImageRangeFromBatch` —— 2/7 个有
- `ImageBatchMulti` —— 2/7 个有
- `MiniMaxH3AddGuide` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `SaveAudioAdvanced` —— 2/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
