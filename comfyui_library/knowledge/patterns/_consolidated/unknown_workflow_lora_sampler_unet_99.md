---
name: unknown_workflow_lora_sampler_unet_99
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.822625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3 海螺 4步lightx2v加速lora 多重提速 图生视频工作流_2084221979170795521.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2084154545424388098.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2087935494813478914.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2099783471219699713.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-文生+图生视频（支持首尾帧）_2084260178744139778.json, 视频生成/图生视频/minimax H3巨物图生视频_2093886571169796098.json, 视频生成/图生视频/minimax H3巨物图生视频_2097867227113541634.json, 视频生成/图生视频/minimaxH3首尾帧视频工作流（超级加速版）_2084965664602804226.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_99

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3 海螺 4步lightx2v加速lora 多重提速 图生视频工作流_2084221979170795521.json、视频生成/图生视频/MinimaxH3图生视频8步工作流_2084154545424388098.json、视频生成/图生视频/MinimaxH3图生视频8步工作流_2087935494813478914.json、视频生成/图生视频/MinimaxH3图生视频8步工作流_2099783471219699713.json、视频生成/图生视频/lightx2v 300%加速 MinimaxH3-文生+图生视频（支持首尾帧）_2084260178744139778.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `Label (rgthree)` —— 4/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `SolAttnPatch` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ManualSigmas` —— 2/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `RHLLMChatNode` —— 2/8 个有
- `SplitSigmas` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `StariAI-MiniMaxH3-Skill` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
