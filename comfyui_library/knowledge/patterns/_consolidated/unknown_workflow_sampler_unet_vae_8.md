---
name: unknown_workflow_sampler_unet_vae_8
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.850524
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json, 视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json, 视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json, 视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json, 视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json, 视频生成/图生视频/MINIMAX-H3 多参工作流包含加速流程和完美克隆音频最终版_2087190952204132354.json, 视频生成/图生视频/MINIMAX-H3 多图生成视频_2085523161088610305.json, 视频生成/图生视频/MINIMAX-H3-图片加音频参考生视频-有提示词模板-int8和fp8_2084515925415522306.json, 视频生成/图生视频/MINIMAX-H3_2084691718737317889.json, 视频生成/图生视频/MINIMAX-H3_多图参考生视频_2084844223446208514.json, 视频生成/图生视频/MiniMax H3 4图生视频+音频接入_2090184072877395969.json, 视频生成/图生视频/MiniMax H3 8步加速 智能参考娃娃穿搭视频生成_2085536956800397314.json, 视频生成/图生视频/MiniMax H3 R2V comfyorg_2085736828308643841.json, 视频生成/图生视频/MiniMax H3 R2V-8步 comfyorg_2087532854384349186.json, 视频生成/图生视频/2053733634456207362.json, 视频生成/图生视频/MiniMax H3 【参考图+参考音频】4步生视频_2090646084061323265.json, 视频生成/图生视频/MiniMax H3 多参考生视频 8步加速版_2084190473446580225.json, 视频生成/图生视频/MiniMax H3 多参考生视频（本地版）_2084663749595721729.json, 视频生成/图生视频/MiniMax H3全能参考工作流_2086738528175747074.json, 视频生成/文生视频/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2086280720103858177.json, 视频生成/文生视频/MiniMax H3加速优化版  全能参考（人物_场景_音频）_2085671993520771073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json、视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json、视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json、视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json、视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 21 个 workflow 都包含：
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
- `ResolutionSelector` —— 20/21 个有
- `VAEDecode` —— 20/21 个有
- `ComfyMathExpression` —— 19/21 个有
- `PrimitiveFloat` —— 19/21 个有
- `PrimitiveStringMultiline` —— 19/21 个有
- `LoadAudio` —— 18/21 个有
- `CreateVideo` —— 17/21 个有
- `SaveVideo` —— 17/21 个有
- `LoraLoaderModelOnly` —— 10/21 个有
- `VHS_LoadVideo` —— 10/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/21 个有
- `JjkText` —— 6/21 个有
- `VHS_VideoCombine` —— 5/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `RTXVideoSuperResolution` —— 3/21 个有
- `easy cleanGpuUsed` —— 3/21 个有
- `Fast Groups Muter (rgthree)` —— 2/21 个有
- `LoadVideo` —— 2/21 个有
- `MiniMaxH3SigmaShift` —— 2/21 个有
- `PathchSageAttentionKJ` —— 2/21 个有
- `PreviewAny` —— 2/21 个有
- `RHLLMChatNode` —— 2/21 个有
- `LTXVSeparateAVLatent` —— 1/21 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/21 个有
- `PrimitiveInt` —— 1/21 个有
- `VAEDecodeTiled` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
