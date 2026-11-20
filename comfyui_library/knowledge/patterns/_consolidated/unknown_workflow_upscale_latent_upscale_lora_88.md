---
name: unknown_workflow_upscale_latent_upscale_lora_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.886
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/视频同款滔博MV工作流_2092323200792358913.json, 视频生成/文生视频/MiniMax_H3_REF2VA-Upscale 双采样视频生成工作流_2092581047509807105.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频同款滔博MV工作流_2092323200792358913.json、视频生成/文生视频/MiniMax_H3_REF2VA-Upscale 双采样视频生成工作流_2092581047509807105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `1hew_AudioDuration` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LatentUpscale` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MiniMaxChunkFeedForward` —— 1/2 个有
- `MiniMaxH3AudioConditioningT8` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
