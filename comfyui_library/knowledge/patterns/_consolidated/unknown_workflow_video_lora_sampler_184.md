---
name: unknown_workflow_video_lora_sampler_184
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8357
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json, 视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104877137932148737.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104929413359030273.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104933693600129025.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2110566290069999618.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2111010022284161026.json, 视频生成/图生视频/【变态加速高清版2.0】MinMaxH3 全能参考-推荐_2106435863944196098.json, 视频生成/文生视频/MimaxH3锐化高清放大采样工作流_2105086382539624449.json, 视频生成/文生视频/【变态加速高清版2.0】MinMaxH3 全能参考-推荐_2106435863944196098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_184

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json、视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json、视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104877137932148737.json、视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104929413359030273.json、视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104933693600129025.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `LTXVSeparateAVLatent` —— 8/10 个有
- `MiniMaxH3VAEDecodeFast` —— 8/10 个有
- `RunningHub Deepcleaner` —— 8/10 个有
- `VAEDecode` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `LoadImage` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 7/10 个有
- `PrimitiveFloat` —— 7/10 个有
- `Fast Groups Muter (rgthree)` —— 6/10 个有
- `PreviewAny` —— 6/10 个有
- `QwenH3PromptLocal` —— 6/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `ImageFromBatch` —— 3/10 个有
- `MiniMaxH3Unified` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `Float` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/10 个有
- `LoadAudio` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
