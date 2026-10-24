---
name: unknown_workflow_video_lora_sampler_285
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.775286
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2111005025232310273.json, 图片生成/图生图/舞蹈短片丨MiniMax H3丨首帧驱动·音画同生_2112107711432318977.json, 视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2084203498043957249.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2110889409909452801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_285

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2111005025232310273.json、图片生成/图生图/舞蹈短片丨MiniMax H3丨首帧驱动·音画同生_2112107711432318977.json、视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json、视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json、视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
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
- `JjkText` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `DF_Int_to_Float` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `ResolutionSelector` —— 4/7 个有
- `RTXVideoFrameGeneration` —— 3/7 个有
- `EmptyImage` —— 1/7 个有
- `MiniMaxH3ImageToVideo` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/7 个有
- `int _O` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
