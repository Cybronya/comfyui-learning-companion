---
name: unknown_workflow_sampler_unet_vae_39
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.880111
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json, 视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json, 视频生成/图生视频/Minimax-H3-图生视频(双时钟+8步极速)_2085725669090217986.json, 视频生成/图生视频/Minimax-H3极速2分钟出5秒-图生_多参生视频(双时钟-8步lora)_2085608744465035265.json, 视频生成/图生视频/Minimax-h3-T8转化版-4步极速-双时钟(80s极速出片)_2116956602208182274.json, 视频生成/图生视频/MinimaxH3_4步极速_首帧尾帧_2115009226912387074.json, 视频生成/图生视频/MinimaxH3_4步极速_首帧尾帧（无首尾帧则文生视频）_2114701415208808450.json, 视频生成/图生视频/MinimaxH3_极速_首帧+参考图+站位图_2116954854013890561.json, 视频生成/图生视频/MinimaxH3_极速_首帧+参考图_2116486895822786561.json, 视频生成/图生视频/MinimaxH3_极速_首帧+参考图_2116695021553545217.json, 视频生成/图生视频/Minimax图生视频_2088591493631135746.json, 视频生成/图生视频/Minimax图生视频（Lightx2v正式版8步lora+双时钟）_2087718729126862850.json, 视频生成/图生视频/Minimax海螺h3开源版 8步高质量极速图生视频加速优化版_2085679906003968001.json, 视频生成/图生视频/Minmax h3-10Eros-max-Sigmas值调度_2088833172883722242.json, 视频生成/图生视频/Vdn MiniMax H3极速参考生视频_2096241438156742657.json, 视频生成/图生视频/（4步极速)Minimax H3开源 双时钟参考图生视频 短剧广告片创意视频生成_2087498995835953154.json, 视频生成/图生视频/（4步极速)Minimax H3开源 双时钟参考图生视频 短剧广告片创意视频生成_2087519938717245441.json, 视频生成/文生视频/Dasiwa-MiniMax H3-动态最强-单采-文生视频_2094938114493083650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_39

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json、视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json、视频生成/图生视频/Minimax-H3-图生视频(双时钟+8步极速)_2085725669090217986.json、视频生成/图生视频/Minimax-H3极速2分钟出5秒-图生_多参生视频(双时钟-8步lora)_2085608744465035265.json、视频生成/图生视频/Minimax-h3-T8转化版-4步极速-双时钟(80s极速出片)_2116956602208182274.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
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
- `MiniMaxH3DualClockSamplerT8` —— 15/18 个有
- `VHS_VideoCombine` —— 15/18 个有
- `LoraLoaderBypassModelOnly` —— 14/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/18 个有
- `ModelAttentionBackend` —— 11/18 个有
- `ImageScale` —— 5/18 个有
- `CreateVideo` —— 3/18 个有
- `LoraLoaderModelOnly` —— 3/18 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 3/18 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 3/18 个有
- `SaveVideo` —— 3/18 个有
- `SolAttnMiniMax` —— 3/18 个有
- `孤海注释` —— 2/18 个有
- `ExtendIntermediateSigmas` —— 1/18 个有
- `H3SigmaRefiner` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
