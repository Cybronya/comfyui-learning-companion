---
name: unknown_workflow_sampler_vae_25
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8346
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3_T2V_lora加速_2090640077063020545.json, 视频生成/文生视频/MiniMax_H3文生视频V1_2087411429900120065.json, 视频生成/文生视频/MiniMax_H3文生视频V2_2088958815235559426.json, 视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json, 视频生成/文生视频/Minimax H3 文生视频 8步加速Lora+sage双重加速工作流_2089325283299119105.json, 视频生成/文生视频/Minimax H3 文生视频_2084236059835195394.json, 视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json, 视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速工作流_2084217093255421954.json, 视频生成/文生视频/Minimax_h3_文生视频_2084506740581818369.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3_T2V_lora加速_2090640077063020545.json、视频生成/文生视频/MiniMax_H3文生视频V1_2087411429900120065.json、视频生成/文生视频/MiniMax_H3文生视频V2_2088958815235559426.json、视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json、视频生成/文生视频/Minimax H3 文生视频 8步加速Lora+sage双重加速工作流_2089325283299119105.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `ResolutionSelector` —— 8/10 个有
- `UNETLoader` —— 8/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `CreateVideo` —— 5/10 个有
- `SaveVideo` —— 5/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `easy int` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `DiffusionModelLoaderKJ` —— 2/10 个有
- `MiniMaxChunkFeedForward` —— 2/10 个有
- `MiniMaxLowVRAMAttention` —— 2/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
