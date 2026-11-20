---
name: unknown_workflow_sampler_unet_vae_261
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8662
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json, 平台全量/H3-DMAD 4步文生视频_2117540373450018817.json, 平台全量/H3-DMAD 8步文生视频_2117536220883546113.json, 视频生成/文生视频/fastvideo_fasth3_文生视频-9：16口播5秒_2101846484743450626.json, 视频生成/文生视频/fastvideo_fasth3_文生视频_2101835354880962561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_261

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json、平台全量/H3-DMAD 4步文生视频_2117540373450018817.json、平台全量/H3-DMAD 8步文生视频_2117536220883546113.json、视频生成/文生视频/fastvideo_fasth3_文生视频-9：16口播5秒_2101846484743450626.json、视频生成/文生视频/fastvideo_fasth3_文生视频_2101835354880962561.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `BlockSparseAttention` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `GetVideoComponents` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `MiniMaxChunkFeedForward` —— 1/5 个有
- `MiniMaxLowVRAMAttention` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
