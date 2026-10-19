---
name: unknown_workflow_video_lora_sampler_444
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4988
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, PurgeVRAM_UTK, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/minimax h3多图参考2K高清工作流_2099029207962701826.json, 视频生成/图生视频/minimax_h3多图参考2K高清工作流_2099786197458575361.json, 视频生成/图生视频/minimax_h3多图参考2K高清工作流_2100042314185003010.json, 视频生成/文生视频/H3 全能多参+4步加速+提示词优化_2087394908050124802.json, 视频生成/文生视频/MiniMaxH3加速版+尾帧做参考+4步加速_2095352841354432513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_444

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/minimax h3多图参考2K高清工作流_2099029207962701826.json、视频生成/图生视频/minimax_h3多图参考2K高清工作流_2099786197458575361.json、视频生成/图生视频/minimax_h3多图参考2K高清工作流_2100042314185003010.json、视频生成/文生视频/H3 全能多参+4步加速+提示词优化_2087394908050124802.json、视频生成/文生视频/MiniMaxH3加速版+尾帧做参考+4步加速_2095352841354432513.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 3/5 个有
- `LTXVSeparateAVLatent` —— 3/5 个有
- `MinimaxH3LatentUpscaler3D` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `SplitSigmas` —— 3/5 个有
- `UniBlockSwap` —— 3/5 个有
- `VHS_LoadAudioUpload` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `easy float` —— 3/5 个有
- `easy ifElse` —— 3/5 个有
- `JoinStringMulti` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `StringConcatenate` —— 2/5 个有
- `ToString` —— 2/5 个有
- `BatchImagesNode` —— 1/5 个有
- `GetLastFrameNode` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `ModelPreviewOverrideKJ` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `workflow>2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
