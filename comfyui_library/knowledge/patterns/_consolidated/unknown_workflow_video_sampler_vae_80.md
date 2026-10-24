---
name: unknown_workflow_video_sampler_vae_80
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.877
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json, 视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json, 视频生成/文生视频/Minimax_H3文生视频图生视频_2095439213532639234.json, 视频生成/文生视频/Minimax_h3_文生视频_2084506740581818369.json, 视频生成/文生视频/Minimax_h3_文生视频_2094242510569828353.json, 视频生成/文生视频/minimax_h3_turbo_lora_4步工作流_2085539352125464578.json, 视频生成/文生视频/【MinimaxH3】首尾帧视频-5倍急速版（25→5分钟）_2087187021684101121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_80

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json、视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json、视频生成/文生视频/Minimax_H3文生视频图生视频_2095439213532639234.json、视频生成/文生视频/Minimax_h3_文生视频_2084506740581818369.json、视频生成/文生视频/Minimax_h3_文生视频_2094242510569828353.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `MiniMaxLowVRAMAttention` —— 3/7 个有
- `SolAttnPatch` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `DiffusionModelLoaderKJ` —— 2/7 个有
- `MiniMaxChunkFeedForward` —— 2/7 个有
- `ModelPreviewOverrideKJ` —— 2/7 个有
- `EasyCache` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `PainterVRAM` —— 1/7 个有
- `SpectrumApplyMiniMaxH3` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
