---
name: unknown_workflow_sampler_vae_14
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.869111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2078283699623391233.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json, 视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json, 视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json, 视频生成/图生视频/minimax_h3_i2v  加速多参考视频生成_2106315178865422338.json, 视频生成/图生视频/minimax_h3_i2v  加速首位帧_2106309679268843522.json, 视频生成/图生视频/minimax_h3_r2v完美视频工作流一_2084929898988269569.json, 视频生成/图生视频/minimax_h3_ref2v_3_2092280813852385282.json, 视频生成/图生视频/minimax_h3_ref2v_4_2092280828972855298.json, 视频生成/图生视频/minimax_h3_ref2v_5_2092280840322637826.json, 视频生成/图生视频/minimax_h3_ref2v_6_2092280852507095041.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2104901215766278145.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2106317299799121921.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2109508856144551937.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2110247938256625666.json, 视频生成/图生视频/minnimax h3 首尾帧生视频（4步加速）_2085544529314271234.json, 视频生成/图生视频/minnimax h3 首帧生视频（8步加速）_2085549343964221442.json, 视频生成/文生视频/minmaxH3单采+1参考视频_2105350818894536705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/2078283699623391233.json、视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json、视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json、视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json、视频生成/图生视频/minimax_h3_i2v  加速多参考视频生成_2106315178865422338.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 16/18 个有
- `PrimitiveStringMultiline` —— 15/18 个有
- `MiniMaxH3ReferenceToVideo` —— 11/18 个有
- `MiniMaxH3ImageToVideo` —— 8/18 个有
- `LoraLoaderModelOnly` —— 6/18 个有
- `MiniMaxH3SigmaShift` —— 6/18 个有
- `ExtendIntermediateSigmas` —— 5/18 个有
- `LoadAudio` —— 5/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/18 个有
- `ResizeImageMaskNode` —— 4/18 个有
- `ModelAttentionBackend` —— 2/18 个有
- `PathchSageAttentionKJ` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `UnetLoaderGGUF` —— 2/18 个有
- `AudioCrop` —— 1/18 个有
- `EmptyMiniMaxH3LatentAV` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `MiniMaxH3TurboLoRA` —— 1/18 个有
- `Text` —— 1/18 个有
- `VHS_LoadVideo` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
