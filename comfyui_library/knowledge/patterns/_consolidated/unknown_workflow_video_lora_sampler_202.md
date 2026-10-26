---
name: unknown_workflow_video_lora_sampler_202
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5907
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/常规万能流直出1080p_最高质量版_-MMH3_Selflift_2113451414457507841.json, 图片生成/图生图/短剧制作_直出1080p_最高质量版_-MMH3_Selflift_2113451009522626561.json, 视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json, 视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json, 视频生成/图生视频/MICAS西游：Camera 3_2103441968356483073.json, 视频生成/图生视频/MiniMax_二采_selflift_急速工作流_2099671590920351746.json, 视频生成/图生视频/MiniMax_二采_selflift_急速工作流自用_2105654345877512193.json, 视频生成/图生视频/常规万能流直出1080p 最高质量版 -MMH3 Selflift_2103534009916674049.json, 视频生成/图生视频/短剧制作 直出1080p 最高质量版 -MMH3 Selflift_2106389437042221057.json, 视频生成/文生视频/H3视频生成self-lift加速双采工作流_2097856577159127042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_202

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/常规万能流直出1080p_最高质量版_-MMH3_Selflift_2113451414457507841.json、图片生成/图生图/短剧制作_直出1080p_最高质量版_-MMH3_Selflift_2113451009522626561.json、视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json、视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json、视频生成/图生视频/MICAS西游：Camera 3_2103441968356483073.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 10 个 workflow 都包含：
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
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `SelfLiftH3Sampler` —— 7/10 个有
- `H3SigmaRefiner` —— 5/10 个有
- `LTXVSeparateAVLatent` —— 5/10 个有
- `PreviewAny` —— 5/10 个有
- `PrimitiveFloat` —— 5/10 个有
- `SelfLiftAvatarH3Sampler` —— 4/10 个有
- `EmptyImage` —— 3/10 个有
- `JWStringToFloat` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `Int` —— 1/10 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/10 个有
- `int _O` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
