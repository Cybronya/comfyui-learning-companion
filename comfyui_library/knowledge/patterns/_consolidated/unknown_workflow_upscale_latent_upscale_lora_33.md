---
name: unknown_workflow_upscale_latent_upscale_lora_33
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9048
common_nodes: [BasicGuider, CLIPLoader, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json, 视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json, 视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json, 视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_多人同框_2102308527359479809.json, 视频生成/图生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2100950589130760193.json, 视频生成/图生视频/双参战斗版 MiniMax H3开源 参考生视频_2095814447255347202.json, 视频生成/图生视频/尾帧生视频_2099041242926632962.json, 视频生成/文生视频/10Eros Beta5 + FL2VA_Ref2VA小脸去油二采精修流_2101605881900261377.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json、视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json、视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json、视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json、视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `ComfyMathExpression` —— 6/10 个有
- `GetImageSize` —— 6/10 个有
- `ImageScaleToTotalPixels` —— 6/10 个有
- `LoadAudio` —— 6/10 个有
- `MiniMaxH3OutputTrimT8` —— 6/10 个有
- `MiniMaxH3DurationPlannerT8` —— 4/10 个有
- `ResolutionSelector` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `CreateVideo` —— 2/10 个有
- `MiniMaxH3AudioWindowT8` —— 2/10 个有
- `MiniMaxH3TwoPassAudioAuditT8Advanced` —— 2/10 个有
- `SaveVideo` —— 2/10 个有
- `SoundFlow_GetLength` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `ConcatTextOfUtils` —— 1/10 个有
- `GetVideoComponents` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `Video Slice` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
