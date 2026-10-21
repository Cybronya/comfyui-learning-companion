---
name: unknown_workflow_lora_sampler_unet_61
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.882
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/无限长视频生成 1 开头 Minimax H3_2091358451745251329.json, 视频生成/图生视频/无限长视频生成 2 延长 Minimax H3_2091357546257932290.json, 视频生成/图生视频/老李多参生视频_2104266943242002434.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/无限长视频生成 1 开头 Minimax H3_2091358451745251329.json、视频生成/图生视频/无限长视频生成 2 延长 Minimax H3_2091357546257932290.json、视频生成/图生视频/老李多参生视频_2104266943242002434.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy saveVideo` —— 2/3 个有
- `MiniMaxH3MotionContext` —— 1/3 个有
- `MiniMaxH3MotionContextTrim` —— 1/3 个有
- `Text` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
