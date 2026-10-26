---
name: unknown_workflow_sampler_unet_vae_296
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.699
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json, 视频生成/文生视频/MiniMax H3全能参考工作流_2084202154499338242.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_296

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json、视频生成/文生视频/MiniMax H3全能参考工作流_2084202154499338242.json、视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
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
- `GetNode` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `SpectrumSDXLBatch` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
