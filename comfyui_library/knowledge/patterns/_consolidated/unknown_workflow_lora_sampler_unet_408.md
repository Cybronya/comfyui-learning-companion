---
name: unknown_workflow_lora_sampler_unet_408
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.847
common_nodes: [AudioConcatenate, BasicGuider, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, ImageBatch, Label (rgthree), LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MultiRateSamplerEXPT8, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader, VRAM_Debug, easy cleanGpuUsed, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3超级长视频1-10顺序生成v2_2115580486679613441.json, 视频生成/文生视频/MiniMax-H3超级长视频1-10顺序生成v2_2098594729884741634.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_408

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3超级长视频1-10顺序生成v2_2115580486679613441.json、视频生成/文生视频/MiniMax-H3超级长视频1-10顺序生成v2_2098594729884741634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcatenate`
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `ImageBatch`
- `Label (rgthree)`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `VRAM_Debug`
- `easy cleanGpuUsed`
- `忽略多组孤海`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
