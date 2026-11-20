---
name: unknown_workflow_lora_sampler_vae_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8105
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/【MinimaxH3】首尾帧视频-5倍急速版（25→5分钟）_2087187021684101121.json, 视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/【MinimaxH3】首尾帧视频-5倍急速版（25→5分钟）_2087187021684101121.json、视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `DiffusionModelLoaderKJ` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `SolAttnPatch` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
