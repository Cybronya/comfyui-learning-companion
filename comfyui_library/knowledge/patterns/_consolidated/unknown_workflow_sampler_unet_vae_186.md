---
name: unknown_workflow_sampler_unet_vae_186
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.895
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json, 视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json, 视频生成/文生视频/FastH3 文生视频_2100134500020867073.json, 视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json, 视频生成/文生视频/fastvideo_fasth3_文生视频-9：16口播5秒_2101846484743450626.json, 视频生成/文生视频/fastvideo_fasth3_文生视频_2101835354880962561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_186

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json、视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json、视频生成/文生视频/FastH3 文生视频_2100134500020867073.json、视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json、视频生成/文生视频/fastvideo_fasth3_文生视频-9：16口播5秒_2101846484743450626.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `BlockSparseAttention` —— 4/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `GetVideoComponents` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
