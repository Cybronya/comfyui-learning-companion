---
name: unknown_workflow_lora_sampler_vae_11
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.56075
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json, 视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json, 视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json, 视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json, 视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json、视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json、视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json、视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json、视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 8 个 workflow 都包含：
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
- `CreateVideo` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `LTXVConcatAVLatent` —— 7/8 个有
- `LTXVSeparateAVLatent` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `MiniMaxLowVRAMAttention` —— 7/8 个有
- `MinimaxH3LatentUpscaler3D` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `SolAttnPatch` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `MiniMaxChunkFeedForward` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 6/8 个有
- `Any Switch (rgthree)` —— 5/8 个有
- `ComfyMathExpression` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `Int` —— 5/8 个有
- `MiniMaxH3ImageToVideo` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `孤海注释` —— 5/8 个有
- `忽略多组孤海` —— 5/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `SplitSigmas` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `H3SigmaRefiner` —— 2/8 个有
- `MiniMaxH3Unified` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ImpactConditionalBranch` —— 1/8 个有
- `ManualSigmas` —— 1/8 个有
- `MiniMaxH3HybridLoader` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy boolean` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy ifElse` —— 1/8 个有
- `布尔孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
