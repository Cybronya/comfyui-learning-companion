---
name: unknown_workflow_lora_sampler_unet_109
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.589714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadAudio, LoraLoaderModelOnly, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json, 视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json, 视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json, 视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json, 视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_109

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/MinimaxH3二采超快无脑数字人流程_2111169741544050690.json、视频生成/图生视频/MinimaxH3数字人-唱歌说话快速高效_2110366154089910274.json、视频生成/图生视频/minimax h3 二菜 1080p 工作流_2097150473840193537.json、视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json、视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `LTXVConcatAVLatent` —— 6/7 个有
- `LTXVSeparateAVLatent` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `MiniMaxChunkFeedForward` —— 6/7 个有
- `MinimaxH3LatentUpscaler3D` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `SolAttnPatch` —— 6/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 6/7 个有
- `Int` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `VAEDecodeAudio` —— 5/7 个有
- `Any Switch (rgthree)` —— 4/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `MiniMaxH3ImageToVideo` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `忽略多组孤海` —— 4/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `MiniMaxH3Unified` —— 2/7 个有
- `ModelPreviewOverrideKJ` —— 2/7 个有
- `SplitSigmas` —— 2/7 个有
- `H3SigmaRefiner` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ImpactConditionalBranch` —— 1/7 个有
- `ManualSigmas` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `easy boolean` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `布尔孤海` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
