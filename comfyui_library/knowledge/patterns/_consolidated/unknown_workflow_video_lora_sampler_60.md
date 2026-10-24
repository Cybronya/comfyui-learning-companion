---
name: unknown_workflow_video_lora_sampler_60
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.754
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/123_2107820492894855170.json, 视频生成/图生视频/CGDselflift+2xVAE+锐化放大模型工作流_2110638154041618433.json, 视频生成/图生视频/CGD加电影lora_2104927511938428929.json, 视频生成/图生视频/H3-8STEP-双采-音频_2102375764057481217.json, 视频生成/图生视频/H3-8STEP-双采_2101940350767165442.json, 视频生成/图生视频/LAOBA  黑科技加速双采-self-lift工作流_2099340731876986882.json, 视频生成/图生视频/MICAS西游：Camera 3_2103441968356483073.json, 视频生成/图生视频/MiniMax H3_selflift+2xVAE+锐化放大工作流_2105110415595364353.json, 视频生成/图生视频/Minimax H3 + Self-lift双采快速超长工作流_2104549240100970498.json, 视频生成/图生视频/Minimax-H3_2109624727416430594.json, 视频生成/图生视频/MinimaxH3-图生视频-高清2K_2105896544250720257.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104877137932148737.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104929413359030273.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104933693600129025.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2110566290069999618.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2111010022284161026.json, 视频生成/文生视频/MimaxH3锐化高清放大采样工作流_2105086382539624449.json, 视频生成/文生视频/MiniMaxH3-极速多参视频制作_2099705642452865026.json, 视频生成/视频生视频/MiniMaxH3-极速多参视频制作_2099705642452865026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/123_2107820492894855170.json、视频生成/图生视频/CGDselflift+2xVAE+锐化放大模型工作流_2110638154041618433.json、视频生成/图生视频/CGD加电影lora_2104927511938428929.json、视频生成/图生视频/H3-8STEP-双采-音频_2102375764057481217.json、视频生成/图生视频/H3-8STEP-双采_2101940350767165442.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 16/19 个有
- `LTXVSeparateAVLatent` —— 13/19 个有
- `MiniMaxH3VAEDecodeFast` —— 13/19 个有
- `QwenH3PromptLocal` —— 13/19 个有
- `RunningHub Deepcleaner` —— 13/19 个有
- `SelfLiftAvatarH3Sampler` —— 12/19 个有
- `PreviewAny` —— 11/19 个有
- `Fast Groups Muter (rgthree)` —— 9/19 个有
- `PrimitiveStringMultiline` —— 8/19 个有
- `Image Comparer (rgthree)` —— 7/19 个有
- `ImageFromBatch` —— 7/19 个有
- `SelfLiftH3Sampler` —— 7/19 个有
- `CreateVideo` —— 6/19 个有
- `LoadAudio` —— 4/19 个有
- `easy showAnything` —— 4/19 个有
- `GetNode` —— 3/19 个有
- `SetNode` —— 3/19 个有
- `Fast Groups Bypasser (rgthree)` —— 2/19 个有
- `JjkText` —— 2/19 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/19 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/19 个有
- `SaveVideo` —— 2/19 个有
- `VHS_LoadVideo` —— 2/19 个有
- `VHS_VideoInfoLoaded` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `Text` —— 1/19 个有
- `忽略多组孤海` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
