---
name: unknown_workflow_sampler_unet_vae_86
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.811154
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json, 视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086413769206489090.json, 视频生成/文生视频/MiniMax H3 文生视频（开源版）_2084993426063450113.json, 视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json, 视频生成/文生视频/MiniMax H3文生视频KJ加速版_2085281989065793537.json, 视频生成/文生视频/MiniMax H3文生视频_2087738976793882626.json, 视频生成/文生视频/MiniMax H3稳定4步lora加速版_2085635166550188033.json, 视频生成/文生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2088628478857015297.json, 视频生成/文生视频/Minimax H3 文生视频 最新8步增速工作流_2087823188460920833.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_86

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json、视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/13 个有
- `MiniMaxH3ImageToVideo` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `SaveVideo` —— 12/13 个有
- `BasicScheduler` —— 11/13 个有
- `KSamplerSelect` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `LoraLoaderBypassModelOnly` —— 6/13 个有
- `CR Text` —— 3/13 个有
- `LoadImage` —— 3/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/13 个有
- `Label (rgthree)` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `VHS_VideoCombine` —— 2/13 个有
- `LayerUtility: TextBox` —— 1/13 个有
- `MiniMaxH3AudioConditioningT8` —— 1/13 个有
- `PlaySound|pysssss` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `ResizeImagesByLongerEdge` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
