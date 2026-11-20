---
name: unknown_workflow_lora_sampler_vae_7
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.598273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json, 视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json, 视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json, 视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091830576230780930.json, 视频生成/图生视频/海螺H3 小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091875924642975746.json, 视频生成/文生视频/(0823修复）海螺H3 sigma强化+潜空间放大+高清人脸工作流_2091505787058348034.json, 视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json, 视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_7

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json、视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json、视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json、视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json、视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 11 个 workflow 都包含：
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
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `LTXVConcatAVLatent` —— 10/11 个有
- `LTXVSeparateAVLatent` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `MinimaxH3LatentUpscaler3D` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 9/11 个有
- `MiniMaxLowVRAMAttention` —— 9/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `VAEDecodeAudio` —— 9/11 个有
- `ComfyMathExpression` —— 8/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `SplitSigmas` —— 8/11 个有
- `H3SigmaRefiner` —— 7/11 个有
- `ModelPreviewOverrideKJ` —— 7/11 个有
- `LoadAudio` —— 6/11 个有
- `MiniMaxChunkFeedForward` —— 5/11 个有
- `SolAttnPatch` —— 5/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `孤海注释` —— 4/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `Int` —— 3/11 个有
- `MiniMaxH3ImageToVideo` —— 3/11 个有
- `PathchSageAttentionKJ` —— 3/11 个有
- `忽略多组孤海` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `MiniMaxH3Unified` —— 2/11 个有
- `SolAttnMiniMax` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `VHS_VideoCombine` —— 2/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `ImpactConditionalBranch` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `MiniMaxH3HybridLoader` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有
- `easy boolean` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `布尔孤海` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
