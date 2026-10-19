---
name: unknown_workflow_sampler_vae_29
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.849778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json, 视频生成/文生视频/MiniMaxH3文生视频工作流 By 像素幻想Lab_2087128147237105666.json, 视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json, 视频生成/文生视频/MiniMax_H3_T2V_lora加速_2090640077063020545.json, 视频生成/文生视频/MiniMax_H3文生视频V1_2087411429900120065.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2084608321469898754.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2092164049516711938.json, 视频生成/文生视频/MinimaxH3参考8步生成视频工作流_2087040392687611906.json, 视频生成/文生视频/Minimax_h3_文生视频_2084506740581818369.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_29

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json、视频生成/文生视频/MiniMaxH3文生视频工作流 By 像素幻想Lab_2087128147237105666.json、视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json、视频生成/文生视频/MiniMax_H3_T2V_lora加速_2090640077063020545.json、视频生成/文生视频/MiniMax_H3文生视频V1_2087411429900120065.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 8/9 个有
- `ResolutionSelector` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `LoadImage` —— 5/9 个有
- `MiniMaxH3ImageToVideo` —— 5/9 个有
- `VHS_VideoCombine` —— 5/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `MiniMaxH3ReferenceToVideo` —— 4/9 个有
- `MiniMaxChunkFeedForward` —— 2/9 个有
- `MiniMaxLowVRAMAttention` —— 2/9 个有
- `SolAttnPatch` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `GetImageSize+` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
