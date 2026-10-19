---
name: unknown_workflow_video_lora_sampler_500
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.63125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json, 视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json, 视频生成/文生视频/Minimax-H3VDN-R2V 视频生成工作流（RH在线流）_2096816318430404609.json, 视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_500

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json、视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json、视频生成/文生视频/Minimax-H3VDN-R2V 视频生成工作流（RH在线流）_2096816318430404609.json、视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MMH3LatentUpscaleWithModelParams` —— 3/4 个有
- `MMH3SpatialSplitParams` —— 3/4 个有
- `MMH3TemporalSplitParams` —— 3/4 个有
- `MMH3UltimateUpscale` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `SeedNode` —— 3/4 个有
- `VAEDecodeTiled` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy clearCacheAll` —— 3/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `SolAttnPatch` —— 1/4 个有
- `Textbox` —— 1/4 个有
- `VedaSparseAttention` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
