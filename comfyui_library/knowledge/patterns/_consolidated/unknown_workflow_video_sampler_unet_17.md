---
name: unknown_workflow_video_sampler_unet_17
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.767421
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/（Pai-8步T8版开源版）MiniMax H3参考生视频加速版v1_2092793444803629057.json, 视频生成/图生视频/（Pai-8步T8版开源版）MiniMax H3图生视频加速版v1_2092875854232768514.json, 视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050.json, 视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2092517840787169282.json, 视频生成/图生视频/（文戏武戏低显存适配版）MiniMax H3双采参考生视频V2_2098587613547556866.json, 视频生成/图生视频/（电影感Zs05）Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092882505149018113.json, 视频生成/图生视频/🦖MiniMax H3双采参考生视频_2098230851896168450.json, 视频生成/文生视频/(10eros v5版)MiniMax H3双采参考生视频_2099438471583719426.json, 视频生成/文生视频/(文武双修均衡版)MiniMax H3双采参考生视频V2_2103225875335565314.json, 视频生成/文生视频/(最佳动态-新版战斗V2)MiniMax H3文生视频_2095552521501757442.json, 视频生成/文生视频/(服装换衣省钱预览版)MiniMax H3双采参考生视频_2097920668905074689.json, 视频生成/文生视频/0905动漫短剧文武双修均衡版（MiniMax H3双采参考生视频）_2096049183974318082.json, 视频生成/文生视频/MINIMAX H3 双采全能参考_2094111351902924801.json, 视频生成/文生视频/MINIMAX-H3全能参考-高配文戏版_2095291262697033729.json, 视频生成/文生视频/MiniMax H3 全能参考生视频｜最佳动态V3极速高清版_2098184624500461569.json, 视频生成/文生视频/MiniMax H3 全能文武戏工作流全能工作流-文戏不油 武戏动态强_2104228828628475905.json, 视频生成/文生视频/MiniMax H3-动态最强-文生视频-V1_2094749351989043201.json, 视频生成/文生视频/OrbTv全能模型_优化版_2104845409087746049.json, 视频生成/文生视频/orb全能模型_2098320359996092418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/（Pai-8步T8版开源版）MiniMax H3参考生视频加速版v1_2092793444803629057.json、视频生成/图生视频/（Pai-8步T8版开源版）MiniMax H3图生视频加速版v1_2092875854232768514.json、视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050.json、视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2092517840787169282.json、视频生成/图生视频/（文戏武戏低显存适配版）MiniMax H3双采参考生视频V2_2098587613547556866.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 17/19 个有
- `MiniMaxH3DualClockSamplerT8` —— 17/19 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 17/19 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 17/19 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 17/19 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 17/19 个有
- `LoraLoaderModelOnly` —— 12/19 个有
- `Float` —— 9/19 个有
- `GetNode` —— 6/19 个有
- `SetNode` —— 6/19 个有
- `ConcatTextOfUtils` —— 5/19 个有
- `LoadAudio` —— 5/19 个有
- `孤海注释` —— 4/19 个有
- `VHS_LoadVideo` —— 3/19 个有
- `easy anythingIndexSwitch` —— 3/19 个有
- `Fast Groups Bypasser (rgthree)` —— 2/19 个有
- `ImpactInt` —— 2/19 个有
- `ImpactSwitch` —— 2/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/19 个有
- `MiniMaxH3PDD8StepSetupT8Advanced` —— 2/19 个有
- `PreviewImage` —— 2/19 个有
- `workflow><Picture 2>` —— 2/19 个有
- `workflow><Picture 3>` —— 2/19 个有
- `workflow><Picture 4>` —— 2/19 个有
- `workflow><Picture 5>` —— 2/19 个有
- `workflow><Picture 6>` —— 2/19 个有
- `ImpactConditionalBranch` —— 1/19 个有
- `SaveVideoNode` —— 1/19 个有
- `workflow><Picture 7>` —— 1/19 个有
- `workflow><Picture 8>` —— 1/19 个有
- `workflow><Picture 9>` —— 1/19 个有
- `布尔孤海` —— 1/19 个有
- `忽略多组孤海` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
