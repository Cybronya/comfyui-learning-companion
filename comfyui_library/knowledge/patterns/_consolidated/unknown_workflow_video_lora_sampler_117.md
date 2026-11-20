---
name: unknown_workflow_video_lora_sampler_117
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.820312
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, UNETLoader, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/常规万能流直出1080p_最高质量版_-MMH3_Selflift_2113451414457507841.json, 图片生成/图生图/短剧制作_直出1080p_最高质量版_-MMH3_Selflift_2113451009522626561.json, 图片生成/图生图/黑科技加速双采-self-lift工作流_2115655225251024897.json, 图片生成/图生图/黑科技加速双采-self-lift工作流_2115676565978836993.json, 平台全量/MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994.json, 平台全量/Minimax H3 SelfLift 文生视频_2120051964783452162.json, 视频生成/图生视频/123_2107820492894855170.json, 视频生成/图生视频/CGDselflift+2xVAE+锐化放大模型工作流_2110638154041618433.json, 视频生成/图生视频/MiniMax H3_selflift+2xVAE+锐化放大工作流_2105110415595364353.json, 视频生成/图生视频/Minimax-H3_2109624727416430594.json, 视频生成/图生视频/MinimaxH3-图生视频-高清2K_2105896544250720257.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104877137932148737.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104929413359030273.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104933693600129025.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2110566290069999618.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2111010022284161026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_117

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/常规万能流直出1080p_最高质量版_-MMH3_Selflift_2113451414457507841.json、图片生成/图生图/短剧制作_直出1080p_最高质量版_-MMH3_Selflift_2113451009522626561.json、图片生成/图生图/黑科技加速双采-self-lift工作流_2115655225251024897.json、图片生成/图生图/黑科技加速双采-self-lift工作流_2115676565978836993.json、平台全量/MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/16 个有
- `SelfLiftAvatarH3Sampler` —— 15/16 个有
- `H3SigmaRefiner` —— 14/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `QwenH3PromptLocal` —— 13/16 个有
- `VAEDecode` —— 13/16 个有
- `LTXVSeparateAVLatent` —— 12/16 个有
- `PreviewAny` —— 12/16 个有
- `MiniMaxH3VAEDecodeFast` —— 10/16 个有
- `RunningHub Deepcleaner` —— 10/16 个有
- `Fast Groups Muter (rgthree)` —— 8/16 个有
- `Image Comparer (rgthree)` —— 7/16 个有
- `ImageFromBatch` —— 7/16 个有
- `PrimitiveStringMultiline` —— 7/16 个有
- `SelfLiftH3Sampler` —— 5/16 个有
- `BlockSparseAttention` —— 4/16 个有
- `easy showAnything` —— 3/16 个有
- `EmptyImage` —— 2/16 个有
- `JjkText` —— 2/16 个有
- `LoadAudio` —— 2/16 个有
- `PreviewImage` —— 2/16 个有
- `VideoCompareSlider` —— 2/16 个有
- `Int` —— 1/16 个有
- `JWStringToFloat` —— 1/16 个有
- `Text` —— 1/16 个有
- `easy float` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
