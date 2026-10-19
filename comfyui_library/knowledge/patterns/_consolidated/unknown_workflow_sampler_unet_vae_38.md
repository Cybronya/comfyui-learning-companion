---
name: unknown_workflow_sampler_unet_vae_38
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.701
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3文生视频工作流_2084125341651660801.json, 视频生成/文生视频/MinimaxH3文生视频工作流_2085581292334305282.json, 视频生成/文生视频/MinimaxH3文生视频工作流_2087915972308066305.json, 视频生成/文生视频/MinimaxH3首尾帧2倍速_2085198819909791746.json, 视频生成/文生视频/MinimaxT2V_2084151579204214786.json, 视频生成/文生视频/Minimax_H3-t2v_创意时装大片文生视频_2087432801984540673.json, 视频生成/文生视频/Minimax_h3_文生视频_2084276192676507650.json, 视频生成/文生视频/Minimax_h3_文生视频_2088656070670643202.json, 视频生成/文生视频/Minimax_h3_文生视频_2094242510569828353.json, 视频生成/文生视频/Minimax_h3_超级加速文生视频_2084160987023896578.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频工作流_2086348400169148418.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3文生视频工作流_2084125341651660801.json、视频生成/文生视频/MinimaxH3文生视频工作流_2085581292334305282.json、视频生成/文生视频/MinimaxH3文生视频工作流_2087915972308066305.json、视频生成/文生视频/MinimaxH3首尾帧2倍速_2085198819909791746.json、视频生成/文生视频/MinimaxT2V_2084151579204214786.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/14 个有
- `SaveVideo` —— 11/14 个有
- `PathchSageAttentionKJ` —— 9/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `EasyCache` —— 5/14 个有
- `GetNode` —— 5/14 个有
- `LoadImage` —— 5/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/14 个有
- `SetNode` —— 5/14 个有
- `VHS_VideoCombine` —— 5/14 个有
- `Any Switch (rgthree)` —— 4/14 个有
- `MiniMaxChunkFeedForward` —— 4/14 个有
- `MiniMaxH3ReferenceToVideo` —— 4/14 个有
- `MiniMaxLowVRAMAttention` —— 4/14 个有
- `PrimitiveStringMultiline` —— 4/14 个有
- `孤海注释` —— 4/14 个有
- `忽略多组孤海` —— 4/14 个有
- `CR Text` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `Int` —— 3/14 个有
- `PainterVRAM` —— 3/14 个有
- `SolAttnPatch` —— 3/14 个有
- `ImageResizeKJv2` —— 2/14 个有
- `LTXVConcatAVLatent` —— 2/14 个有
- `LTXVSeparateAVLatent` —— 2/14 个有
- `LoadAudio` —— 2/14 个有
- `MiniMaxH3SigmaShift` —— 2/14 个有
- `MinimaxH3LatentUpscaler3D` —— 2/14 个有
- `ModelAttentionBackend` —— 2/14 个有
- `VHS_LoadVideo` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `ManualSigmas` —— 1/14 个有
- `PT_H3ConcatAVLatent` —— 1/14 个有
- `VAEEncode` —— 1/14 个有
- `VAEEncodeAudio` —— 1/14 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
