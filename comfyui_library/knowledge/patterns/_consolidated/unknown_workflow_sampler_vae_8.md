---
name: unknown_workflow_sampler_vae_8
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.870931
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2078283699623391233.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json, 视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2092340433505574914.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2096278611857862657.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频_2092343211615412226.json, 视频生成/图生视频/minimaxH3开源版首尾帧(20step)_2092293644232519681.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2092310874190073858.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2092935184156024834.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2105856274675093506.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2109460890293727233.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2109652415707443202.json, 视频生成/图生视频/minimaxH3开源版首帧生视频(8step加速)_2092324995224662017.json, 视频生成/图生视频/minimaxH3开源版首帧生视频_2092326575885869057.json, 视频生成/图生视频/minimax_h3_lightx2v正式版 参考模式_2085761824204607490.json, 视频生成/图生视频/minimax_h3_r2v完美视频工作流一_2084929898988269569.json, 视频生成/图生视频/minimax_h3_ref2v_3_2092280813852385282.json, 视频生成/图生视频/minimax_h3_ref2v_4_2092280828972855298.json, 视频生成/图生视频/minimax_h3_ref2v_5_2092280840322637826.json, 视频生成/图生视频/minimax_h3_ref2v_6_2092280852507095041.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2104901215766278145.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2106317299799121921.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2109508856144551937.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2110247938256625666.json, 视频生成/图生视频/minnimax h3 首尾帧生视频（4步加速）_2085544529314271234.json, 视频生成/图生视频/minnimax h3 首帧生视频（8步加速）_2085549343964221442.json, 视频生成/图生视频/首尾帧参考生视频 无色差版 Minimax H3_2088976531933712385.json, 视频生成/文生视频/生产文字特效视频 minimax H3_2088261863363670018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json、视频生成/图生视频/minimax-h3首尾帧工作流_2078283699623391233.json、视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json、视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json、视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2092340433505574914.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 29 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 28/29 个有
- `UNETLoader` —— 25/29 个有
- `MiniMaxH3ImageToVideo` —— 18/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/29 个有
- `LoraLoaderModelOnly` —— 16/29 个有
- `PrimitiveStringMultiline` —— 14/29 个有
- `MiniMaxH3ReferenceToVideo` —— 11/29 个有
- `MiniMaxH3SigmaShift` —— 6/29 个有
- `ExtendIntermediateSigmas` —— 4/29 个有
- `LoadAudio` —— 4/29 个有
- `PathchSageAttentionKJ` —— 4/29 个有
- `ResizeImageMaskNode` —— 4/29 个有
- `PreviewImage` —— 3/29 个有
- `ImageResizeKJv2` —— 2/29 个有
- `MiniMaxH3HybridLoader` —— 2/29 个有
- `PreviewAny` —— 2/29 个有
- `Text` —— 2/29 个有
- `UnetLoaderGGUF` —— 2/29 个有
- `MiniMaxH3TurboLoRA` —— 1/29 个有
- `ModelAttentionBackend` —— 1/29 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
