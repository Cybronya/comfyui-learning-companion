---
name: unknown_workflow_sampler_unet_vae_54
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.835455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3文生视频KJ加速版_2085281989065793537.json, 视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json, 视频生成/文生视频/MiniMax H3文生视频_2087738976793882626.json, 视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json, 视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json, 视频生成/文生视频/MiniMax H3文生视频（Sage加速）2608_2085826303927869442.json, 视频生成/文生视频/MiniMaxT2V 文生视频超强稳定动作_2084482575703302145.json, 视频生成/文生视频/Minimax H3 文生视频_2085256821585039362.json, 视频生成/文生视频/MinimaxT2V_2084151579204214786.json, 视频生成/文生视频/Minimax_h3_文生视频_2084276192676507650.json, 视频生成/文生视频/Minimax_h3_文生视频_2094242510569828353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_54

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3文生视频KJ加速版_2085281989065793537.json、视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json、视频生成/文生视频/MiniMax H3文生视频_2087738976793882626.json、视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json、视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json…）

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
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/11 个有
- `CreateVideo` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `EasyCache` —— 5/11 个有
- `CR Text` —— 3/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `FlashVSRInitPipe` —— 1/11 个有
- `FlashVSRNodeAdv` —— 1/11 个有
- `MiniMaxChunkFeedForward` —— 1/11 个有
- `MiniMaxLowVRAMAttention` —— 1/11 个有
- `PainterVRAM` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `SpectrumSDXL` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
