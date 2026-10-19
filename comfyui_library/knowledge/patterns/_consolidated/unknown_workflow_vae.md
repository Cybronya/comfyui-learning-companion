---
name: unknown_workflow_vae
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.825526
common_nodes: [BasicScheduler, CLIPLoader, CreateVideo, LoadImage, MiniMaxH3ReferenceToVideo, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3 360°环绕与卡片旋转视频_2109661372345831426.json, 视频生成/图生视频/minimax多图生视频_2102951424215834626.json, 视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json, 视频生成/图生视频/video_minimax_h3_r2v_2084534320714313730.json, 视频生成/图生视频/video_minimax_h3_r2v_turbo 多参加速_2100758868111486978.json, 视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json, 视频生成/图生视频/全模态多图片生视频MiniMax H3_2084270450250702850.json, 视频生成/图生视频/单图参考生视频 生产力版 MiniMax+H3+H25+Hybrid_2088526268315820034.json, 视频生成/图生视频/参考生视频_MiniMax H3_2084453784557809665.json, 视频生成/图生视频/漫剧林辰_2103760332870217729.json, 视频生成/图生视频/电商4图参考考生视频  minimax h3 加速版_2089612691093676034.json, 视频生成/图生视频/电商双图参考考生视频  minimax h3 加速版_2088445593055219714.json, 视频生成/图生视频/短剧漫剧参考图生视频_2103117172716429314.json, 视频生成/图生视频/自我介绍_2110222353635561474.json, 视频生成/图生视频/走秀_2110212966074376193.json, 视频生成/图生视频/超自然超细节-H3的服装展示(dasiwa)_2101210281803337729.json, 视频生成/文生视频/DsiwaV2 +selflift二采+小脸优化_2101450792984207362.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2107756287479074818.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2108505430593986562.json]
source: knowledge_consolidation
---

# unknown_workflow_vae

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3 360°环绕与卡片旋转视频_2109661372345831426.json、视频生成/图生视频/minimax多图生视频_2102951424215834626.json、视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json、视频生成/图生视频/video_minimax_h3_r2v_2084534320714313730.json、视频生成/图生视频/video_minimax_h3_r2v_turbo 多参加速_2100758868111486978.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 18/19 个有
- `PrimitiveFloat` —— 18/19 个有
- `ResolutionSelector` —— 18/19 个有
- `KSamplerSelect` —— 17/19 个有
- `UNETLoader` —— 16/19 个有
- `BasicGuider` —— 15/19 个有
- `RandomNoise` —— 15/19 个有
- `SamplerCustomAdvanced` —— 15/19 个有
- `LoraLoaderModelOnly` —— 14/19 个有
- `PrimitiveStringMultiline` —— 13/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/19 个有
- `MiniMaxH3SigmaShift` —— 8/19 个有
- `PathchSageAttentionKJ` —— 7/19 个有
- `CR Text` —— 5/19 个有
- `MiniMaxChunkFeedForward` —— 5/19 个有
- `MiniMaxH3TurboLoRA` —— 5/19 个有
- `MiniMaxLowVRAMAttention` —— 5/19 个有
- `ConditioningZeroOut` —— 4/19 个有
- `ModelPreviewOverrideKJ` —— 4/19 个有
- `SelfLiftAvatarH3Sampler` —— 4/19 个有
- `easy seed` —— 4/19 个有
- `MiniMaxH3HybridLoader` —— 3/19 个有
- `MiniMaxH3TurboSampler` —— 2/19 个有
- `PreviewAny` —— 2/19 个有
- `DF_Integer` —— 1/19 个有
- `H3SigmaRefiner` —— 1/19 个有
- `LoadAudio` —— 1/19 个有
- `LoraLoaderBypassModelOnly` —— 1/19 个有
- `VHS_LoadVideo` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
