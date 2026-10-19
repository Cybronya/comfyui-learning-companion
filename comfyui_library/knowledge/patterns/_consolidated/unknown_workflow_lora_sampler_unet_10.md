---
name: unknown_workflow_lora_sampler_unet_10
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.678
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json, 视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json, 视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091830576230780930.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2089513420025589761.json, 视频生成/图生视频/海螺H3 小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091875924642975746.json, 视频生成/图生视频/短剧助手：MiniMax H3 双模双采资源面板加载生成视频_2093912808089014274.json, 视频生成/文生视频/海螺H3优化 小脸 打斗 浅空间_2091512771916681217.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json、视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json、视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json、视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json、视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091830576230780930.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `GetNode` —— 8/9 个有
- `LTXVConcatAVLatent` —— 8/9 个有
- `LTXVSeparateAVLatent` —— 8/9 个有
- `MiniMaxLowVRAMAttention` —— 8/9 个有
- `MinimaxH3LatentUpscaler3D` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `SplitSigmas` —— 8/9 个有
- `H3SigmaRefiner` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `MiniMaxH3ReferenceToVideo` —— 7/9 个有
- `PrimitiveFloat` —— 7/9 个有
- `VAEDecodeAudio` —— 7/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `ModelPreviewOverrideKJ` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `LoadAudio` —— 3/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `MiniMaxChunkFeedForward` —— 2/9 个有
- `MiniMaxH3Unified` —— 2/9 个有
- `SolAttnPatch` —— 2/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `DF_Integer` —— 1/9 个有
- `Int` —— 1/9 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/9 个有
- `MiniMaxH3ReferenceSplitter` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
