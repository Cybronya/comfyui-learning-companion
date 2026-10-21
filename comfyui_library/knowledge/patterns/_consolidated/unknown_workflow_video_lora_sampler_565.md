---
name: unknown_workflow_video_lora_sampler_565
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8495
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/银河系小王文生视频V1_2094272713035706370.json, 视频生成/文生视频/高动态战斗王者(极速高清)MiniMax H3参考生视频_2098258737172664322.json, 视频生成/文生视频/（音频驱动-10Eros-Max Beta3）MiniMax H3数字人加速版V1_2092512922332389378.json, 视频生成/视频生视频/MiniMax H3 人物替换_lora版__2106317435786842113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_565

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/银河系小王文生视频V1_2094272713035706370.json、视频生成/文生视频/高动态战斗王者(极速高清)MiniMax H3参考生视频_2098258737172664322.json、视频生成/文生视频/（音频驱动-10Eros-Max Beta3）MiniMax H3数字人加速版V1_2092512922332389378.json、视频生成/视频生视频/MiniMax H3 人物替换_lora版__2106317435786842113.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 3/4 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 3/4 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 3/4 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `JWStringToFloat` —— 1/4 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/4 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
