---
name: unknown_workflow_video_lora_sampler_1009
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8505
common_nodes: [AudioConcat, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), ImageBatchConcatNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent, MiniMaxH3MotionContextTrim, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowText|pysssss, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy int, 孤海注释]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax+H3+多参上下文一镜到底_2087872879705808897.json, 视频生成/文生视频/MiniMax+H3+首帧上下文连续长镜头_2087561493293395970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1009

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax+H3+多参上下文一镜到底_2087872879705808897.json、视频生成/文生视频/MiniMax+H3+首帧上下文连续长镜头_2087561493293395970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchConcatNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3MotionContextTrim`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy int`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `ZML_AnyTypeSwitchFive` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
