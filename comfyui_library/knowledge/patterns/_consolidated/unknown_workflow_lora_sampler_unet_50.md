---
name: unknown_workflow_lora_sampler_unet_50
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.904667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json, 视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json, 视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 高质感低显存文生视频｜16G_24G 可跑｜真人感优化_2105308028953255937.json、视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json、视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `CreateVideo` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxH3ContextIR` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
