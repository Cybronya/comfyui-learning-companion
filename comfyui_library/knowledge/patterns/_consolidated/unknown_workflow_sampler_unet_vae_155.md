---
name: unknown_workflow_sampler_unet_vae_155
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.63975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json, 视频生成/图生视频/老秦的声音克隆数字人_2097164544790589442.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json, 视频生成/文生视频/MiniMax_H3_Ref2VA全功能_官方提示词版_2084288422902059010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json、视频生成/图生视频/老秦的声音克隆数字人_2097164544790589442.json、视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json、视频生成/文生视频/MiniMax_H3_Ref2VA全功能_官方提示词版_2084288422902059010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：64%

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
- `PathchSageAttentionKJ` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImageScaleDownToSize` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy positive` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
