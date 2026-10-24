---
name: unknown_workflow_upscale_latent_upscale_lora_34
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.882333
common_nodes: [BasicGuider, CLIPLoader, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json, 视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json, 视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json, 视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_多人同框_2102308527359479809.json, 视频生成/图生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2100950589130760193.json, 视频生成/图生视频/四只兔子_H3_高动态双采放大专属_2096882401648668673.json, 视频生成/文生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2095962479263309826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_34

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json、视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json、视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json、视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json、视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 7/9 个有
- `ModelPreviewOverrideKJ` —— 7/9 个有
- `SolAttnMiniMax` —— 7/9 个有
- `GetImageSize` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `LoadAudio` —— 6/9 个有
- `MiniMaxH3OutputTrimT8` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `ComfyMathExpression` —— 5/9 个有
- `MiniMaxH3DurationPlannerT8` —— 4/9 个有
- `CreateVideo` —— 3/9 个有
- `ResolutionSelector` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `MiniMaxH3AudioWindowT8` —— 2/9 个有
- `MiniMaxH3TwoPassAudioAuditT8Advanced` —— 2/9 个有
- `SoundFlow_GetLength` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `PreviewImage` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `easy loraStack` —— 1/9 个有
- `easy loraStackApply` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
