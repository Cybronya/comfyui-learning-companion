---
name: unknown_workflow_lora_sampler_unet_332
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Text Multiline, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed, easy saveVideo]
problems: []
missing: []
members: [视频生成/图生视频/无限长视频生成 1 开头 Minimax H3_2091358451745251329.json, 视频生成/图生视频/无限长视频生成 2 延长 Minimax H3_2091357546257932290.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_332

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/无限长视频生成 1 开头 Minimax H3_2091358451745251329.json、视频生成/图生视频/无限长视频生成 2 延长 Minimax H3_2091357546257932290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageFromBatch`
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
- `SaveImage`
- `Text Multiline`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy saveVideo`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MotionContext` —— 1/2 个有
- `MiniMaxH3MotionContextTrim` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
