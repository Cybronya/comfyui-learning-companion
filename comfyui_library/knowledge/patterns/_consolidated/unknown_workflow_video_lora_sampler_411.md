---
name: unknown_workflow_video_lora_sampler_411
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7616
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2084203498043957249.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2110889409909452801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_411

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json、视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json、视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json、视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2084203498043957249.json、视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2110889409909452801.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DF_Int_to_Float` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `JjkText` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ResolutionSelector` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/5 个有
- `RTXVideoFrameGeneration` —— 1/5 个有
- `int _O` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
