---
name: unknown_workflow_sampler_vae_36
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.841
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3_T2V_lora加速_2090640077063020545.json, 视频生成/文生视频/MiniMax_H3文生视频V1_2087411429900120065.json, 视频生成/文生视频/MiniMax_H3文生视频V2_2088958815235559426.json, 视频生成/文生视频/Minimax H3 文生视频_2084236059835195394.json, 视频生成/文生视频/Minimax H3 文生视频标准版_2094294196017524737.json, 视频生成/文生视频/Minimax H3 极速文生视频_2085290047233945602.json, 视频生成/文生视频/MinimaxH3文生视频8步工作流_2087038591577972737.json, 视频生成/文生视频/MinimaxH3文生视频8步工作流_2099773191228051457.json, 视频生成/文生视频/Minimax_H3文生视频图生视频_2095439213532639234.json, 视频生成/文生视频/Minimax_h3_文生视频_2084506740581818369.json, 视频生成/文生视频/minimax_h3_turbo_lora_4步工作流_2085539352125464578.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_36

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3_T2V_lora加速_2090640077063020545.json、视频生成/文生视频/MiniMax_H3文生视频V1_2087411429900120065.json、视频生成/文生视频/MiniMax_H3文生视频V2_2088958815235559426.json、视频生成/文生视频/Minimax H3 文生视频_2084236059835195394.json、视频生成/文生视频/Minimax H3 文生视频标准版_2094294196017524737.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/11 个有
- `UNETLoader` —— 8/11 个有
- `CreateVideo` —— 6/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/11 个有
- `SaveVideo` —— 6/11 个有
- `SolAttnPatch` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `DiffusionModelLoaderKJ` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `MiniMaxLowVRAMAttention` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `LoadImage` —— 2/11 个有
- `MiniMaxChunkFeedForward` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `CacheDiT_Model_Optimizer` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `ModelPreviewOverrideKJ` —— 1/11 个有
- `SpectrumApplyMiniMaxH3` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
