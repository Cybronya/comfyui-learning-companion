---
name: unknown_workflow_sampler_unet_vae_115
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.794667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [数字人/数字人/H3数字人单人可做MV、口播等_2084869137700052993.json, 数字人/数字人/MiniMAX3参考音频对口型-8月8日版_2086535599267344386.json, 数字人/数字人/MiniMax H3  数字人_单人版_2085223953907404802.json, 数字人/数字人/MiniMax H3-数字人_2084880448492228609.json, 数字人/数字人/MiniMax H3-数字人_2111474246617751554.json, 数字人/数字人/MiniMax h3音频驱动数字人对口型-自动写提示词+全节点注释_2089689798725423105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/H3数字人单人可做MV、口播等_2084869137700052993.json、数字人/数字人/MiniMAX3参考音频对口型-8月8日版_2086535599267344386.json、数字人/数字人/MiniMax H3  数字人_单人版_2085223953907404802.json、数字人/数字人/MiniMax H3-数字人_2084880448492228609.json、数字人/数字人/MiniMax H3-数字人_2111474246617751554.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `SoundFlow_GetLength` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `PreviewAudio` —— 3/6 个有
- `AudioConcat` —— 2/6 个有
- `EmptyAudio` —— 2/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `JoinStringMulti` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `SpectrumApplyMiniMaxH3` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `ToString` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
