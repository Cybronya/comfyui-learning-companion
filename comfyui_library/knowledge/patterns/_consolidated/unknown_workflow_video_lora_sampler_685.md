---
name: unknown_workflow_video_lora_sampler_685
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.586667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedNode, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json, 视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json, 视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_685

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json、视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json、视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedNode`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有
- `MMH3LatentUpscaleWithModelParams` —— 2/3 个有
- `MMH3SpatialSplitParams` —— 2/3 个有
- `MMH3TemporalSplitParams` —— 2/3 个有
- `MMH3UltimateUpscale` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `H3FaceStitch` —— 1/3 个有
- `H3FaceTrackCrop` —— 1/3 个有
- `H3InjectVideoLatent` —— 1/3 个有
- `H3PerFrameDenoise` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `Textbox` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VedaSparseAttention` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
