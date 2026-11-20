---
name: unknown_workflow_upscale_latent_upscale_lora_81
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.833667
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/四只兔子_H3_高动态双采放大专属_2096882401648668673.json, 视频生成/文生视频/10Eros Beta5 + FL2VA_Ref2VA小脸去油二采精修流_2101605881900261377.json, 视频生成/文生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2095962479263309826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_81

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/四只兔子_H3_高动态双采放大专属_2096882401648668673.json、视频生成/文生视频/10Eros Beta5 + FL2VA_Ref2VA小脸去油二采精修流_2101605881900261377.json、视频生成/文生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2095962479263309826.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `SolAttnMiniMax` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `Video Slice` —— 1/3 个有
- `easy loraStack` —— 1/3 个有
- `easy loraStackApply` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
