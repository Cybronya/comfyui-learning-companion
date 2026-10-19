---
name: unknown_workflow_video_sampler_vae_65
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.842
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3文生视频V2_2088958815235559426.json, 视频生成/文生视频/MiniMax_H3文生视频自动提示词版_2084361115349372930.json, 视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json, 视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json, 视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json, 视频生成/文生视频/Minimax_H3文生视频图生视频_2095439213532639234.json, 视频生成/文生视频/minimax_h3_turbo_lora_4步工作流_2085539352125464578.json, 视频生成/文生视频/【MinimaxH3】首尾帧视频-5倍急速版（25→5分钟）_2087187021684101121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_65

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3文生视频V2_2088958815235559426.json、视频生成/文生视频/MiniMax_H3文生视频自动提示词版_2084361115349372930.json、视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json、视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json、视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `UNETLoader` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `DiffusionModelLoaderKJ` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `SolAttnPatch` —— 3/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `INTConstant` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `MiniMaxLowVRAMAttention` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `SpectrumApplyMiniMaxH3` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
