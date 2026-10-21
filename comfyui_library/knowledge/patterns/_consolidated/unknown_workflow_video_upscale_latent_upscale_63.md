---
name: unknown_workflow_video_upscale_latent_upscale_63
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.916
common_nodes: [BasicGuider, CLIPLoader, GetImageSize, ImageScaleToTotalPixels, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3OutputTrimT8, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json, 视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json, 视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json, 视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_多人同框_2102308527359479809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_63

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json、视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json、视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json、视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json、视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 4/6 个有
- `MiniMaxH3DurationPlannerT8` —— 4/6 个有
- `ComfyMathExpression` —— 2/6 个有
- `MiniMaxH3AudioWindowT8` —— 2/6 个有
- `MiniMaxH3TwoPassAudioAuditT8Advanced` —— 2/6 个有
- `SoundFlow_GetLength` —— 2/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
