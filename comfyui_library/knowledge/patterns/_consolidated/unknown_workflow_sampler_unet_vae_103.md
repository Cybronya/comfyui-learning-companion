---
name: unknown_workflow_sampler_unet_vae_103
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.830375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3-turbo-T2V_2094630845184299009.json, 视频生成/文生视频/MinimaxH3文生视频8步工作流_2087038591577972737.json, 视频生成/文生视频/MinimaxH3文生视频8步工作流_2099773191228051457.json, 视频生成/文生视频/MinimaxH3文生视频工作流_2084125341651660801.json, 视频生成/文生视频/MinimaxH3文生视频工作流_2085581292334305282.json, 视频生成/文生视频/MinimaxH3文生视频工作流_2087915972308066305.json, 视频生成/文生视频/Minimax_H3-t2v_创意时装大片文生视频_2087432801984540673.json, 视频生成/文生视频/VividMuse_MiniMax_H3_文生视频_2084269402014437378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_103

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3-turbo-T2V_2094630845184299009.json、视频生成/文生视频/MinimaxH3文生视频8步工作流_2087038591577972737.json、视频生成/文生视频/MinimaxH3文生视频8步工作流_2099773191228051457.json、视频生成/文生视频/MinimaxH3文生视频工作流_2084125341651660801.json、视频生成/文生视频/MinimaxH3文生视频工作流_2085581292334305282.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
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
- `SolAttnPatch` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `LTXVConcatAVLatent` —— 1/8 个有
- `LTXVSeparateAVLatent` —— 1/8 个有
- `MinimaxH3LatentUpscaler3D` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `SplitSigmas` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
