---
name: unknown_workflow_upscale_latent_upscale_lora_63
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.706
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/minimax_h3综合型工作流第一人称，男友视角_2114997856431067137.json, 图片生成/图生图/小脸不崩！打斗不糊！H3_sigma强化+潜空间放大工作流（不油啦！）_2113788878191681537.json, 图片生成/文生图/MINIMAX-H3 显存终极优化工作流_2090698454728269825.json, 视频生成/图生视频/4k+二采新condition+同模双采+H3+动态修复_2108509040342028289.json, 视频生成/图生视频/LMS测试+二采新condition+同模双采+语义桥_2100942089772163074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_63

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/minimax_h3综合型工作流第一人称，男友视角_2114997856431067137.json、图片生成/图生图/小脸不崩！打斗不糊！H3_sigma强化+潜空间放大工作流（不油啦！）_2113788878191681537.json、图片生成/文生图/MINIMAX-H3 显存终极优化工作流_2090698454728269825.json、视频生成/图生视频/4k+二采新condition+同模双采+H3+动态修复_2108509040342028289.json、视频生成/图生视频/LMS测试+二采新condition+同模双采+语义桥_2100942089772163074.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `MiniMaxChunkFeedForward` —— 3/5 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/5 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/5 个有
- `MiniMaxLowVRAMAttention` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `SolAttnMiniMax` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `ConcatTextOfUtils` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `MiniMaxH3TurboLoRA` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `Astra` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `JjkShowText` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/5 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/5 个有
- `MiniMaxH3VAEDecodeFast` —— 1/5 个有
- `QwenH3PromptLocal` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
