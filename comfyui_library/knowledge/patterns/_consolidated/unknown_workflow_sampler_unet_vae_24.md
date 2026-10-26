---
name: unknown_workflow_sampler_unet_vae_24
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.821389
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json, 视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086413769206489090.json, 视频生成/文生视频/MiniMax H3 文生视频（开源版）_2084993426063450113.json, 视频生成/文生视频/MiniMax H3图生视频（支持文生视频，首_尾帧生成）_2084161667742654466.json, 视频生成/文生视频/MiniMax H3文生视频KJ加速版_2085281989065793537.json, 视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json, 视频生成/文生视频/MiniMax H3文生视频_2087738976793882626.json, 视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json, 视频生成/文生视频/MiniMax H3稳定4步lora加速版_2085635166550188033.json, 视频生成/文生视频/MiniMax H3｜5图多参考快速出片｜5-15秒｜稳定版_2091107780571783170.json, 视频生成/文生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2088628478857015297.json, 视频生成/文生视频/Minimax H3 文生视频 最新8步增速工作流_2087823188460920833.json, 视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json, 视频生成/文生视频/战斗双采首尾帧模式_2094373774731862018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_24

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json、视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 17/18 个有
- `ResolutionSelector` —— 17/18 个有
- `VAEDecode` —— 17/18 个有
- `BasicScheduler` —— 16/18 个有
- `CreateVideo` —— 16/18 个有
- `KSamplerSelect` —— 16/18 个有
- `SaveVideo` —— 16/18 个有
- `MiniMaxH3ImageToVideo` —— 15/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/18 个有
- `LoadImage` —— 6/18 个有
- `LoraLoaderBypassModelOnly` —— 6/18 个有
- `PrimitiveStringMultiline` —— 5/18 个有
- `CR Text` —— 4/18 个有
- `VHS_VideoCombine` —— 4/18 个有
- `Label (rgthree)` —— 3/18 个有
- `LoraLoaderModelOnly` —— 3/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/18 个有
- `DisableNoise` —— 2/18 个有
- `MiniMaxH3ReferenceToVideo` —— 2/18 个有
- `PrimitiveInt` —— 2/18 个有
- `easy cleanGpuUsed` —— 2/18 个有
- `ExtendIntermediateSigmas` —— 1/18 个有
- `LayerUtility: TextBox` —— 1/18 个有
- `MiniMaxH3AudioConditioningT8` —— 1/18 个有
- `SplitSigmas` —— 1/18 个有
- `SplitSigmasDenoise` —— 1/18 个有
- `VAEDecodeTiled` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
