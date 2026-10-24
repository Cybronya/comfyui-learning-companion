---
name: unknown_workflow_sampler_unet_vae_21
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8487
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json, 视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json, 视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json, 视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json, 视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json, 视频生成/图生视频/MINIMAX-H3 多参工作流包含加速流程和完美克隆音频最终版_2087190952204132354.json, 视频生成/图生视频/MINIMAX-H3 多图生成视频_2085523161088610305.json, 视频生成/图生视频/MINIMAX-H3_2084691718737317889.json, 视频生成/图生视频/MiniMax H3 8步加速 智能参考娃娃穿搭视频生成_2085536956800397314.json, 视频生成/图生视频/MiniMax H3 R2V-8步 comfyorg_2087532854384349186.json, 视频生成/图生视频/MiniMax H3 Ref2VA多图参考生视频_2053733634456207362.json, 视频生成/图生视频/MiniMax H3 【参考图+参考音频】4步生视频_2090646084061323265.json, 视频生成/图生视频/MiniMax H3 双角色+背景+自定义音频输入 视频生成工作流_2084953803597635586.json, 视频生成/图生视频/MiniMax H3 多参考生视频 8步加速版_2084190473446580225.json, 视频生成/图生视频/MiniMax H3全能参考工作流_2086738528175747074.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2104901215766278145.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2106317299799121921.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2109508856144551937.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2110247938256625666.json, 视频生成/文生视频/minmaxH3单采+1参考视频_2105350818894536705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_21

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json、视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json、视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json、视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json、视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 19/20 个有
- `VAEDecode` —— 19/20 个有
- `ComfyMathExpression` —— 18/20 个有
- `CreateVideo` —— 18/20 个有
- `PrimitiveFloat` —— 18/20 个有
- `PrimitiveStringMultiline` —— 18/20 个有
- `SaveVideo` —— 18/20 个有
- `LoadAudio` —— 16/20 个有
- `LoraLoaderModelOnly` —— 12/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/20 个有
- `VHS_LoadVideo` —— 8/20 个有
- `MiniMaxH3SigmaShift` —— 7/20 个有
- `ExtendIntermediateSigmas` —— 5/20 个有
- `Fast Groups Bypasser (rgthree)` —— 3/20 个有
- `PathchSageAttentionKJ` —— 3/20 个有
- `VHS_VideoCombine` —— 3/20 个有
- `JjkText` —— 2/20 个有
- `ModelAttentionBackend` —— 2/20 个有
- `LTXVSeparateAVLatent` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `MiniMaxH3TurboLoRA` —— 1/20 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/20 个有
- `PreviewAny` —— 1/20 个有
- `PrimitiveInt` —— 1/20 个有
- `RHLLMChatNode` —— 1/20 个有
- `VAEDecodeTiled` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
