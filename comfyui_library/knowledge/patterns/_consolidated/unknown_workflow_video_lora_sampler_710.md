---
name: unknown_workflow_video_lora_sampler_710
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.885
common_nodes: [BasicGuider, BetaSamplingScheduler, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, ModelPreviewOverrideKJ, Power Lora Loader (rgthree), PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MiniMax - T2V_2087875413392580609.json, 视频生成/图生视频/Hunyuan3D+Minimax-h3Video_2088154761152520193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_710

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/MiniMax - T2V_2087875413392580609.json、视频生成/图生视频/Hunyuan3D+Minimax-h3Video_2088154761152520193.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BetaSamplingScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `ModelPreviewOverrideKJ`
- `Power Lora Loader (rgthree)`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `EmptyLatentHunyuan3Dv2` —— 1/2 个有
- `Hunyuan3Dv2Conditioning` —— 1/2 个有
- `Hy3DRenderSingleView` —— 1/2 个有
- `ImageOnlyCheckpointLoader` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MESHToTrimesh` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveGLB` —— 1/2 个有
- `VAEDecodeHunyuan3D` —— 1/2 个有
- `VoxelToMesh` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |
| 宽度 | 3072 | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
