---
name: unknown_workflow_video_upscale_latent_upscale_4
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.714174
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/02_H3首帧对白视频_1至5人_2101612649518813185.json, 视频生成/图生视频/02_H3首帧对白视频_1至5人_2113238126385778690.json, 视频生成/图生视频/MiniMax H3-不油文剧工作流_2096934850723926018.json, 视频生成/图生视频/MiniMax H3参考生视频-10Eros turbo动态叙事工作流_2095011453865652225.json, 视频生成/图生视频/MiniMax H3参考生视频-武戏战斗版_2098232096543297537.json, 视频生成/图生视频/MiniMax H3双采参考生视频-8步turbo分镜叙事工作流_2095007873272209409.json, 视频生成/图生视频/MiniMax H3双采参考生视频（(Dasiwa v2版本）_2100154364542414850.json, 视频生成/图生视频/MiniMax H3双采多图参考生视频_2104183600680890369.json, 视频生成/图生视频/MiniMax H3双采数字人-双Pass高清精修口播工作流_2094984969503465474.json, 视频生成/图生视频/MiniMax H3（自用）_2099416401143492609.json, 视频生成/图生视频/MiniMax+H3参考生视频-最强战斗效果-多图参考_2096436150956285954.json, 视频生成/图生视频/MiniMax+H3双采全能工作流V2-音频驱动数字人-参考生视频_2111113734084190209.json, 视频生成/图生视频/MiniMaxH3_双采参考生视频_2104941388239560705.json, 视频生成/图生视频/MiniMax_H3双采全能工作流V2-音频驱动数字人-参考生视频_2100139084525166593.json, 视频生成/图生视频/MiniMax_H3双采全能工作流V2-音频驱动数字人-参考生视频_2101871299831357442.json, 视频生成/图生视频/minimax H3 文戏工作流（急速版）_2106909033222459394.json, 视频生成/图生视频/minimaxh3高动文武双修工作流_2110566903226916866.json, 视频生成/图生视频/minimaxh3高动文武双修工作流_2111010562334355457.json, 视频生成/图生视频/【MINIMAX H3】武戏-高动态_极速高清_2107175289238409217.json, 视频生成/文生视频/9月30日目前最强武戏-高动态_极速高清_ 自动提示词+手动提示词2选1_2104942695335682050.json, 视频生成/文生视频/minimax H3 文戏工作流（急速版）_2106909033222459394.json, 视频生成/文生视频/minimaxh3高动文武双修工作流_2106006102767915010.json, 视频生成/文生视频/【MINIMAX H3】武戏-高动态_极速高清_ 全自动输出_2104519856463900674.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/02_H3首帧对白视频_1至5人_2101612649518813185.json、视频生成/图生视频/02_H3首帧对白视频_1至5人_2113238126385778690.json、视频生成/图生视频/MiniMax H3-不油文剧工作流_2096934850723926018.json、视频生成/图生视频/MiniMax H3参考生视频-10Eros turbo动态叙事工作流_2095011453865652225.json、视频生成/图生视频/MiniMax H3参考生视频-武戏战斗版_2098232096543297537.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 23 个 workflow 都包含：
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
- `ModelAttentionBackend` —— 21/23 个有
- `ResolutionSelector` —— 21/23 个有
- `SolAttnMiniMax` —— 21/23 个有
- `LoraLoaderBypassModelOnly` —— 20/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 20/23 个有
- `LoraLoaderModelOnly` —— 18/23 个有
- `Float` —— 15/23 个有
- `ConcatTextOfUtils` —— 13/23 个有
- `GetNode` —— 11/23 个有
- `SetNode` —— 11/23 个有
- `Fast Groups Bypasser (rgthree)` —— 10/23 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 10/23 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 10/23 个有
- `PreviewImage` —— 9/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/23 个有
- `PreviewAny` —— 8/23 个有
- `RH_LLMAPI_Pro_Node` —— 8/23 个有
- `LoadAudio` —— 6/23 个有
- `VAEDecode` —— 5/23 个有
- `VAEDecodeAudio` —— 5/23 个有
- `easy cleanGpuUsed` —— 5/23 个有
- `easy anythingIndexSwitch` —— 4/23 个有
- `ImpactSwitch` —— 3/23 个有
- `CR Text Concatenate` —— 2/23 个有
- `GetImageSize` —— 2/23 个有
- `ImageScaleToTotalPixels` —— 2/23 个有
- `ImpactInt` —— 2/23 个有
- `MiniMaxH3DurationPlannerT8` —— 2/23 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 2/23 个有
- `EmptyImage` —— 1/23 个有
- `Text Multiline` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
