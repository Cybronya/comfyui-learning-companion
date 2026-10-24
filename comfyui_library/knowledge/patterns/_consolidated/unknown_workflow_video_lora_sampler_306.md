---
name: unknown_workflow_video_lora_sampler_306
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.846714
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json, 视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json, 视频生成/图生视频/常规万能流直出1080p 最高质量版 -MMH3 Selflift_2103534009916674049.json, 视频生成/图生视频/短剧制作 直出1080p 最高质量版 -MMH3 Selflift_2106389437042221057.json, 视频生成/文生视频/H3视频生成self-lift加速双采工作流_2097856577159127042.json, 视频生成/文生视频/啊癫 黑科技加速双采-self-lift工作流_2097728195679309825.json, 视频生成/文生视频/海螺H3最新融合模型+黑科技加速双采-self-lift工作流_2097523746214080514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_306

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json、视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json、视频生成/图生视频/常规万能流直出1080p 最高质量版 -MMH3 Selflift_2103534009916674049.json、视频生成/图生视频/短剧制作 直出1080p 最高质量版 -MMH3 Selflift_2106389437042221057.json、视频生成/文生视频/H3视频生成self-lift加速双采工作流_2097856577159127042.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `H3SigmaRefiner` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `VAEDecodeAudio` —— 5/7 个有
- `LoadAudio` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `SelfLiftAvatarH3Sampler` —— 4/7 个有
- `SelfLiftH3Sampler` —— 3/7 个有
- `CreateVideo` —— 2/7 个有
- `JWStringToFloat` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/7 个有
- `MiniMaxH3Unified` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
