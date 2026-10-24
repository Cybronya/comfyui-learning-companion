---
name: unknown_workflow_sampler_unet_vae_243
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.907
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json, 数字人/数字人/首尾帧逻辑_2087967441874931713.json, 视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json, 视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_243

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json、数字人/数字人/首尾帧逻辑_2087967441874931713.json、视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json、视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
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
- `LoadImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 3/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `GetVideoComponents` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3AddGuide` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
