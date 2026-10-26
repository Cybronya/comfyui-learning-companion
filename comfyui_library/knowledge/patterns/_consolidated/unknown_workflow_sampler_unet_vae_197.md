---
name: unknown_workflow_sampler_unet_vae_197
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.879
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json, 视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json, 视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084540140541792258.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084680217980915713.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速工作流_2084217093255421954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_197

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json、视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json、视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json、视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084540140541792258.json、视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084680217980915713.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ResolutionSelector` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `Float` —— 2/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `RTXVideoSuperResolution` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `easy int` —— 2/6 个有
- `INTConstant` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
