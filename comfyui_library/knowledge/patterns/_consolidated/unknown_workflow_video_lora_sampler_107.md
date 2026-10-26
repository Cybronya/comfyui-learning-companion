---
name: unknown_workflow_video_lora_sampler_107
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.870812
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/FastH3 VSA文生视频优化版V1_2096244135350067201.json, 视频生成/文生视频/H3文生视频-融合模型10Eros-加速lora+双时钟_2087828994078105602.json, 视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频(9图3视频3音频)_2088583576190279681.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频(9图3视频3音频)_2091128915946459138.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频_2086885673054855170.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频_2091121872074272770.json, 视频生成/文生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2086881972470767617.json, 视频生成/文生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091109259294629890.json, 视频生成/文生视频/MiniMax H3-加速版-参考生视频-长视频直出-单采_2100882071358103553.json, 视频生成/文生视频/MiniMax H3双采全能参考视频｜真实电影质感｜文武双修均衡版_2096132560068894721.json, 视频生成/文生视频/MiniMax H3双采多参V2（均衡版）_2096028522333696002.json, 视频生成/文生视频/Minimax H3 音频驱动数字人对口型｜唱歌说话口播｜Remix文戏版_2094609192823906305.json, 视频生成/文生视频/xinlingjitang_2097652872459669506.json, 视频生成/文生视频/去油-文武全能图音参考(10eros beta5版)MiniMax H3双采生视频_2100432792248213505.json, 视频生成/文生视频/文武双全全能(10eros beta5版)MiniMax H3双采多参考生视频_2100271114697142273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/FastH3 VSA文生视频优化版V1_2096244135350067201.json、视频生成/文生视频/H3文生视频-融合模型10Eros-加速lora+双时钟_2087828994078105602.json、视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json、视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频(9图3视频3音频)_2088583576190279681.json、视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频(9图3视频3音频)_2091128915946459138.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DualClockSamplerT8` —— 15/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/16 个有
- `LoadImage` —— 12/16 个有
- `LoadAudio` —— 9/16 个有
- `ModelAttentionBackend` —— 9/16 个有
- `LoraLoaderModelOnly` —— 8/16 个有
- `SolAttnMiniMax` —— 7/16 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 6/16 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 6/16 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 6/16 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 6/16 个有
- `GetNode` —— 5/16 个有
- `SetNode` —— 5/16 个有
- `GetVideoComponents` —— 4/16 个有
- `LoadVideo` —— 4/16 个有
- `孤海注释` —— 4/16 个有
- `Float` —— 3/16 个有
- `AudioCrop` —— 2/16 个有
- `ConcatTextOfUtils` —— 2/16 个有
- `Int` —— 2/16 个有
- `easy anythingIndexSwitch` —— 2/16 个有
- `1hew_AudioDuration` —— 1/16 个有
- `CR Text Concatenate` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `LayerUtility: TextJoin` —— 1/16 个有
- `MathExpression|pysssss` —— 1/16 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/16 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/16 个有
- `ModelPreviewOverrideKJ` —— 1/16 个有
- `MuyeTextEditOutput` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
