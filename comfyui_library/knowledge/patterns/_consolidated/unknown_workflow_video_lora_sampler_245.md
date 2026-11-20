---
name: unknown_workflow_video_lora_sampler_245
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.689455
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ResolutionSelector, UNETLoader, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（文戏）_2116092028240093186.json, 视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562.json, 视频生成/图生视频/【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113.json, 视频生成/图生视频/啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882.json, 视频生成/图生视频/啊癫 融合模型-self-lift工作流_2115106829108858881.json, 视频生成/图生视频/常规万能流直出1080p 最高质量版 -MMH3 Selflift_2103534009916674049.json, 视频生成/图生视频/短剧制作 直出1080p 最高质量版 -MMH3 Selflift_2106389437042221057.json, 视频生成/图生视频/锐化工作流_2113864371016392706.json, 视频生成/文生视频/MimaxH3锐化高清放大采样工作流_2105086382539624449.json, 视频生成/文生视频/MiniMaxH3-极速多参视频制作_2099705642452865026.json, 视频生成/视频生视频/MiniMaxH3-极速多参视频制作_2099705642452865026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_245

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（文戏）_2116092028240093186.json、视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562.json、视频生成/图生视频/【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113.json、视频生成/图生视频/啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882.json、视频生成/图生视频/啊癫 融合模型-self-lift工作流_2115106829108858881.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SelfLiftAvatarH3Sampler` —— 10/11 个有
- `H3SigmaRefiner` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 9/11 个有
- `LoadAudio` —— 9/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `ModelPreviewOverrideKJ` —— 8/11 个有
- `VAEDecode` —— 8/11 个有
- `MiniMaxH3VAEDecodeFast` —— 7/11 个有
- `RunningHub Deepcleaner` —— 7/11 个有
- `BlockSparseAttention` —— 6/11 个有
- `Fast Groups Muter (rgthree)` —— 5/11 个有
- `GetNode` —— 4/11 个有
- `PreviewAny` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `CreateVideo` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `JWStringToFloat` —— 2/11 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/11 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/11 个有
- `QwenH3PromptLocal` —— 2/11 个有
- `SaveVideo` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `VHS_VideoInfoLoaded` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ImageFromBatch` —— 1/11 个有
- `SelfLiftH3Sampler` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
