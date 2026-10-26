---
name: unknown_workflow_upscale_lora_sampler_43
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9242
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, JWFloat, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3ChunkFeedForwardT8Advanced, MiniMaxH3ChunkedTwoPassPlanT8Advanced, MiniMaxH3ChunkedTwoPassUpscaleT8Advanced, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PreviewAny, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/低显存直出4k-MiniMax H3双采多参生视频_2113461682122092545.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100787039317876737.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100884384172830721.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100928696604520449.json, 视频生成/图生视频/MiniMax H3双采参考生视频-低显存版本_2104091652603338754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/低显存直出4k-MiniMax H3双采多参生视频_2113461682122092545.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100787039317876737.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100884384172830721.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100928696604520449.json、视频生成/图生视频/MiniMax H3双采参考生视频-低显存版本_2104091652603338754.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `JWFloat`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced`
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PreviewAny`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `GetNode` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `RH_DLSS5Enhance` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
