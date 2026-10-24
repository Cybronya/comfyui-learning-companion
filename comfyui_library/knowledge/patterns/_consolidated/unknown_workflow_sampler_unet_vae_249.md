---
name: unknown_workflow_sampler_unet_vae_249
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.73475
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json, 视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json, 视频生成/文生视频/Minimax_h3官方多参视频生成工作流_2084688064726781954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_249

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json、视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json、视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json、视频生成/文生视频/Minimax_h3官方多参视频生成工作流_2084688064726781954.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
