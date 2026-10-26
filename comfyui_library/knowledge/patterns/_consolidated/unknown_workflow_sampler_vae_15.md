---
name: unknown_workflow_sampler_vae_15
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8774
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json, 视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json, 视频生成/图生视频/MiniMax_H3_Fast_2114224611851329538.json, 视频生成/图生视频/MiniMax_H3_R2V_3参考图_LightX2V_4步_2090336616714956801.json, 视频生成/图生视频/Minimax H3 多参生视频_2084365914140659713.json, 视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json, 视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2092363444539453442.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2092936286209396737.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2094336398261309442.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2109218798602641409.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2099778923717550082.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2100038725966319618.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2104901215766278145.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2106317299799121921.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2109508856144551937.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2110247938256625666.json, 视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json, 视频生成/文生视频/MiniMax H3 H25 Hybrid 多参8步最优对比测试_2088184113558806529.json, 视频生成/文生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2088303974402318338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json、视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json、视频生成/图生视频/MiniMax_H3_Fast_2114224611851329538.json、视频生成/图生视频/MiniMax_H3_R2V_3参考图_LightX2V_4步_2090336616714956801.json、视频生成/图生视频/Minimax H3 多参生视频_2084365914140659713.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 19/20 个有
- `PrimitiveFloat` —— 19/20 个有
- `UNETLoader` —— 18/20 个有
- `PrimitiveStringMultiline` —— 14/20 个有
- `LoraLoaderModelOnly` —— 12/20 个有
- `LoadVideo` —— 11/20 个有
- `PathchSageAttentionKJ` —— 11/20 个有
- `GetVideoComponents` —— 9/20 个有
- `MiniMaxH3SigmaShift` —— 8/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/20 个有
- `EasyCache` —— 6/20 个有
- `CR Prompt Text` —— 5/20 个有
- `ExtendIntermediateSigmas` —— 4/20 个有
- `TrimAudioDuration` —— 4/20 个有
- `Video Slice` —— 4/20 个有
- `AddLabel` —— 3/20 个有
- `ImageScaleToTotalPixels` —— 3/20 个有
- `MiniMaxH3HybridLoader` —— 3/20 个有
- `MiniMaxH3TurboLoRA` —— 1/20 个有
- `ModelAttentionBackend` —— 1/20 个有
- `PrimitiveInt` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
