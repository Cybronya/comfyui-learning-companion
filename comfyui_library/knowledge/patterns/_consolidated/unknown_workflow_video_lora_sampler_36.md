---
name: unknown_workflow_video_lora_sampler_36
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.70428
common_nodes: [BasicGuider, CLIPLoader, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3_Turbo_Stable_4V4A_2087928785877430274.json, 视频生成/文生视频/MiniMax H3 4步加速 文生视频_2086878121780924417.json, 视频生成/文生视频/MiniMax H3 4步加速 文生视频_2091083830605213698.json, 视频生成/文生视频/MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882.json, 视频生成/文生视频/MiniMax H3-加速版-参考生视频-长视频直出-单采_2100882071358103553.json, 视频生成/文生视频/MiniMax H3-文生视频V1-双时钟-8步高质量极速-step600_2086838165842780162.json, 视频生成/文生视频/MiniMax H3-文生视频V1-双时钟-8步高质量极速-step600_2087878612149161985.json, 视频生成/文生视频/MiniMax H3双采全能参考视频｜真实电影质感｜文武双修均衡版_2096132560068894721.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2096583694927622145.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-宫格图生视频_2099500409453891585.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-宫格图生视频_2099514636340121601.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-宫格图生视频_2100166099735240706.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-文生视频_2096561555252006913.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-文生视频_2101209510349201410.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-参考生视频_2097138677536354306.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-参考生视频_2097272057355653122.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-多人对话-二采_2100936331642888193.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-文生视频_2097144924377534466.json, 视频生成/文生视频/MiniMax H3双采参考生视频_2103091380615737346.json, 视频生成/文生视频/MiniMax H3双采多参V2（均衡版）_2096028522333696002.json, 视频生成/文生视频/MiniMax H3双采多图参考生成视频工作流V2-文戏不油，武戏动态强_2098769442292457473.json, 视频生成/文生视频/Minimax H3 音频驱动数字人对口型｜唱歌说话口播｜Remix文戏版_2094609192823906305.json, 视频生成/文生视频/去油-文武全能图音参考(10eros beta5版)MiniMax H3双采生视频_2100432792248213505.json, 视频生成/文生视频/文武双全全能(10eros beta5版)MiniMax H3双采多参考生视频_2100271114697142273.json, 音频生成/音频生成/MiniMax_H3双采全能工作流V2-音频驱动数字人-参考生视频_2100058854255063042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/文生视频/H3_Turbo_Stable_4V4A_2087928785877430274.json、视频生成/文生视频/MiniMax H3 4步加速 文生视频_2086878121780924417.json、视频生成/文生视频/MiniMax H3 4步加速 文生视频_2091083830605213698.json、视频生成/文生视频/MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882.json、视频生成/文生视频/MiniMax H3-加速版-参考生视频-长视频直出-单采_2100882071358103553.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 24/25 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 24/25 个有
- `PrimitiveFloat` —— 24/25 个有
- `ResolutionSelector` —— 24/25 个有
- `CR Prompt Text` —— 23/25 个有
- `LoadImage` —— 21/25 个有
- `ModelAttentionBackend` —— 19/25 个有
- `SolAttnMiniMax` —— 19/25 个有
- `LoraLoaderModelOnly` —— 18/25 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 18/25 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 18/25 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 18/25 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 18/25 个有
- `GetNode` —— 16/25 个有
- `SetNode` —— 16/25 个有
- `Float` —— 15/25 个有
- `孤海注释` —— 15/25 个有
- `Fast Groups Bypasser (rgthree)` —— 12/25 个有
- `LoadAudio` —— 11/25 个有
- `ConcatTextOfUtils` —— 3/25 个有
- `easy anythingIndexSwitch` —— 3/25 个有
- `AudioCrop` —— 2/25 个有
- `Int` —— 2/25 个有
- `Audio Cut (mtb)` —— 1/25 个有
- `CR Text Concatenate` —— 1/25 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/25 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/25 个有
- `ModelPreviewOverrideKJ` —— 1/25 个有
- `MuyeTextEditOutput` —— 1/25 个有
- `PrimitiveStringMultiline` —— 1/25 个有
- `VHS_LoadVideo` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
