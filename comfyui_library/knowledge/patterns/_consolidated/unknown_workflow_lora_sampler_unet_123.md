---
name: unknown_workflow_lora_sampler_unet_123
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.871714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json, 视频生成/文生视频/Minimax H3-文生视频（高动态去噪点）_2089345292486402050.json, 视频生成/文生视频/Minimax h3 4 步 lora2 加速版_2092076952441151490.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json, 视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速工作流_2084217093255421954.json, 视频生成/文生视频/Minmax H3参考加速工作流_2086695240752263170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_123

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 文生视频_2084263974157242369.json、视频生成/文生视频/Minimax H3-文生视频（高动态去噪点）_2089345292486402050.json、视频生成/文生视频/Minimax h3 4 步 lora2 加速版_2092076952441151490.json、视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json、视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/7 个有
- `MiniMaxH3ImageToVideo` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `H3SigmaRefiner` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `MuyeTextEditOutput` —— 2/7 个有
- `easy int` —— 2/7 个有
- `ExtendIntermediateSigmas` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Int` —— 1/7 个有
- `MiniMaxH3ReferenceToVideo` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SigmasPreview` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
