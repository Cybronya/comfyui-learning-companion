---
name: unknown_workflow_video_lora_sampler_166
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.761083
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json, 视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json, 视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json, 视频生成/图生视频/黑科技加速双采-self-lift-Heng_2100234461106499585.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-3图1音_2102289015847350274.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-4图1音_2102284106150273026.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-5图1音_2108825320408309761.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-6图1音_2108828857859141634.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2097859473883881474.json, 视频生成/图生视频/（修脸极速）黑科技加速minimax h3 self-lift双采多参生视频_2098223404263497730.json, 视频生成/文生视频/MiniMaxH3-极速多参视频制作_2099705642452865026.json, 视频生成/视频生视频/MiniMaxH3-极速多参视频制作_2099705642452865026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_166

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json、视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json、视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json、视频生成/图生视频/黑科技加速双采-self-lift-Heng_2100234461106499585.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-3图1音_2102289015847350274.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `ResolutionSelector` —— 11/12 个有
- `PrimitiveStringMultiline` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `CreateVideo` —— 9/12 个有
- `SelfLiftH3Sampler` —— 9/12 个有
- `LoadImage` —— 7/12 个有
- `LoadAudio` —— 5/12 个有
- `Int` —— 4/12 个有
- `SDVN Load Image Url` —— 4/12 个有
- `VHS_LoadAudio` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `GetNode` —— 3/12 个有
- `SelfLiftAvatarH3Sampler` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `LTXVSeparateAVLatent` —— 2/12 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/12 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/12 个有
- `MiniMaxH3VAEDecodeFast` —— 2/12 个有
- `RunningHub Deepcleaner` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `VHS_VideoInfoLoaded` —— 2/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `MiniMaxH3SigmaShift` —— 1/12 个有
- `MiniMaxH3Unified` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `easy float` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
