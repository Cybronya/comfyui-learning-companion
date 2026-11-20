---
name: unknown_workflow_video_upscale_latent_upscale_23
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.875
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/02_H3首帧对白视频_1至5人_2101612649518813185.json, 视频生成/图生视频/02_H3首帧对白视频_1至5人_2113238126385778690.json, 视频生成/图生视频/MiniMax H3-不油文剧工作流_2096934850723926018.json, 视频生成/图生视频/MiniMax H3参考生视频-10Eros turbo动态叙事工作流_2095011453865652225.json, 视频生成/图生视频/MiniMax H3参考生视频-武戏战斗版_2098232096543297537.json, 视频生成/图生视频/MiniMax H3双采参考生视频-8步turbo分镜叙事工作流_2095007873272209409.json, 视频生成/图生视频/MiniMax H3双采参考生视频支持参考音频和视频_2102401654355218433.json, 视频生成/图生视频/MiniMax H3双采参考生视频格莱美慢镜头_2103902789440196610.json, 视频生成/图生视频/MiniMax H3双采多图参考生视频_2104183600680890369.json, 视频生成/图生视频/（可调节动态-均衡版+高清化）MiniMax H3双采参考生视频V1_2103917510214119426.json, 视频生成/图生视频/（可调节动态-均衡版）MiniMax H3双采参考生视频V1_2102340152520699905.json, 视频生成/文生视频/OrbTv全能模型_优化版_2104845409087746049.json, 视频生成/文生视频/orb全能模型_2098320359996092418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/02_H3首帧对白视频_1至5人_2101612649518813185.json、视频生成/图生视频/02_H3首帧对白视频_1至5人_2113238126385778690.json、视频生成/图生视频/MiniMax H3-不油文剧工作流_2096934850723926018.json、视频生成/图生视频/MiniMax H3参考生视频-10Eros turbo动态叙事工作流_2095011453865652225.json、视频生成/图生视频/MiniMax H3参考生视频-武戏战斗版_2098232096543297537.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 11/13 个有
- `ModelAttentionBackend` —— 11/13 个有
- `ResolutionSelector` —— 11/13 个有
- `SolAttnMiniMax` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/13 个有
- `ConcatTextOfUtils` —— 8/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `Float` —— 7/13 个有
- `easy anythingIndexSwitch` —— 7/13 个有
- `LoadAudio` —— 5/13 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 5/13 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 5/13 个有
- `VHS_LoadVideo` —— 5/13 个有
- `ImpactInt` —— 4/13 个有
- `ImpactSwitch` —— 4/13 个有
- `CR Text Concatenate` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `ImageScaleToTotalPixels` —— 2/13 个有
- `MiniMaxH3DurationPlannerT8` —— 2/13 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 2/13 个有
- `workflow><Picture 2>` —— 2/13 个有
- `workflow><Picture 3>` —— 2/13 个有
- `workflow><Picture 4>` —— 2/13 个有
- `workflow><Picture 5>` —— 2/13 个有
- `workflow><Picture 6>` —— 2/13 个有
- `Fast Muter (rgthree)` —— 1/13 个有
- `ImageCrop` —— 1/13 个有
- `ImageFromBatch` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `TrimAudioDuration` —— 1/13 个有
- `workflow><Picture 7>` —— 1/13 个有
- `workflow><Picture 8>` —— 1/13 个有
- `workflow><Picture 9>` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
