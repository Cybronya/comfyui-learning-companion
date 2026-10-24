---
name: unknown_workflow_upscale_latent_upscale_lora_48
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.702667
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json, 视频生成/图生视频/iniMax H3 六图可选图生视频｜混合模型 潜空间高清直出_2095018141456879618.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2089513420025589761.json, 视频生成/图生视频/海螺H3 小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091875924642975746.json, 视频生成/图生视频/短剧助手：MiniMax H3 双模双采资源面板加载生成视频_2093912808089014274.json, 视频生成/文生视频/Minimax H3优化！浅空间二次放大！优化小脸和打斗_2087552804436140033.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_48

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json、视频生成/图生视频/iniMax H3 六图可选图生视频｜混合模型 潜空间高清直出_2095018141456879618.json、视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2089513420025589761.json、视频生成/图生视频/海螺H3 小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091875924642975746.json、视频生成/图生视频/短剧助手：MiniMax H3 双模双采资源面板加载生成视频_2093912808089014274.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `H3SigmaRefiner` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxLowVRAMAttention` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `ModelPreviewOverrideKJ` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `Anything Everywhere` —— 1/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CFGGuider` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `DF_Integer` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/6 个有
- `MiniMaxH3ReferenceSplitter` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `VRAM_Debug` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
