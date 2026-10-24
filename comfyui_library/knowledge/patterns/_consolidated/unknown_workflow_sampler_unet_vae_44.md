---
name: unknown_workflow_sampler_unet_vae_44
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.905067
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json, 视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json, 视频生成/图生视频/Minimax-H3-图生视频(双时钟+8步极速)_2085725669090217986.json, 视频生成/图生视频/Minimax-H3极速2分钟出5秒-图生_多参生视频(双时钟-8步lora)_2085608744465035265.json, 视频生成/图生视频/Minimax图生视频_2088591493631135746.json, 视频生成/图生视频/Minimax图生视频（Lightx2v正式版8步lora+双时钟）_2087718729126862850.json, 视频生成/图生视频/Minimax海螺h3开源版 8步高质量极速图生视频加速优化版_2085679906003968001.json, 视频生成/图生视频/Minmax h3-10Eros-max-Sigmas值调度_2088833172883722242.json, 视频生成/图生视频/QHDMinimax-H3加速版_2086351325427748866.json, 视频生成/图生视频/Vdn MiniMax H3极速参考生视频_2096241438156742657.json, 视频生成/图生视频/minimax三图工作流_2092594675935956993.json, 视频生成/图生视频/minimax参考生视频-4张图官方案例（light2v8步lora正式版+双时钟）_2087937856227602434.json, 视频生成/图生视频/minimax图生视频（light2v8步lora正式版+双时钟）_2087533230470811649.json, 视频生成/图生视频/v3 minimax h3超级加强！清晰度天花板_2088502342512631810.json, 视频生成/图生视频/v4 minimax h3-Sigmas 区间控制_2089033224172425217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_44

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json、视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json、视频生成/图生视频/Minimax-H3-图生视频(双时钟+8步极速)_2085725669090217986.json、视频生成/图生视频/Minimax-H3极速2分钟出5秒-图生_多参生视频(双时钟-8步lora)_2085608744465035265.json、视频生成/图生视频/Minimax图生视频_2088591493631135746.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 13/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 12/15 个有
- `VHS_VideoCombine` —— 12/15 个有
- `LoraLoaderBypassModelOnly` —— 11/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `ModelAttentionBackend` —— 7/15 个有
- `LoraLoaderModelOnly` —— 4/15 个有
- `CreateVideo` —— 3/15 个有
- `ExtendIntermediateSigmas` —— 3/15 个有
- `H3SigmaRefiner` —— 3/15 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 3/15 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 3/15 个有
- `SaveVideo` —— 3/15 个有
- `SolAttnMiniMax` —— 3/15 个有
- `BasicScheduler` —— 2/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `KSamplerSelect` —— 2/15 个有
- `LoadAudio` —— 2/15 个有
- `PT_H3ConcatAVLatent` —— 2/15 个有
- `VAEEncodeTiled` —— 2/15 个有
- `ModelPreviewOverrideKJ` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `solarL_VideoFrameRelay` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
