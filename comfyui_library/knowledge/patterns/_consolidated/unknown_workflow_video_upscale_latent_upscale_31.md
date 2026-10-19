---
name: unknown_workflow_video_upscale_latent_upscale_31
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.879333
common_nodes: [BasicGuider, CLIPLoader, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json, 视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json, 视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json, 视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json, 视频生成/图生视频/03_BUNNY_已有配音驱动_多人同框_2102308527359479809.json, 视频生成/图生视频/银河系小王参考生视频-自用_2094346923468738561.json, 视频生成/图生视频/银河系小王图生视频-自用_2094273549614800897.json, 视频生成/图生视频/首帧生视频_2099038054504812545.json, 视频生成/图生视频/（Minimax H3）Remix版文戏工作流_2096586271111081985.json, 视频生成/文生视频/MiniMax H3双采全能参考视频｜真实电影质感｜文武双修均衡版_2096132560068894721.json, 视频生成/文生视频/Minimax H3 音频驱动数字人对口型｜唱歌说话口播｜Remix文戏版_2094609192823906305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_31

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2102237008474230785.json、视频生成/图生视频/01_BUNNY_首帧视频_原生声音_2104442997843783681.json、视频生成/图生视频/02_BUNNY_1人音色参考_生成新对白_2102300239691599874.json、视频生成/图生视频/02_BUNNY_2人音色参考_生成新对白_2102237076006719490.json、视频生成/图生视频/03_BUNNY_已有配音驱动_单人镜头_2102237115760332802.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/12 个有
- `LoadAudio` —— 7/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `CR Prompt Text` —— 6/12 个有
- `GetImageSize` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 6/12 个有
- `MiniMaxH3OutputTrimT8` —— 6/12 个有
- `ModelPreviewOverrideKJ` —— 6/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `ResolutionSelector` —— 6/12 个有
- `MiniMaxH3DurationPlannerT8` —— 4/12 个有
- `MiniMaxH3AudioWindowT8` —— 2/12 个有
- `MiniMaxH3TwoPassAudioAuditT8Advanced` —— 2/12 个有
- `SoundFlow_GetLength` —— 2/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `SetNode` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
