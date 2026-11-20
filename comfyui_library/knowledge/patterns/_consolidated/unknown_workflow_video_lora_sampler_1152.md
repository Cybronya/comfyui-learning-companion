---
name: unknown_workflow_video_lora_sampler_1152
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.784
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, H3SigmaRefiner, INTConstant, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PT_H3ConcatAVLatent, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json, 视频生成/文生视频/啊癫 MINIMAX-H3 多参生视频-二采版_2090845897457487873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1152

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json、视频生成/文生视频/啊癫 MINIMAX-H3 多参生视频-二采版_2090845897457487873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `H3SigmaRefiner`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
