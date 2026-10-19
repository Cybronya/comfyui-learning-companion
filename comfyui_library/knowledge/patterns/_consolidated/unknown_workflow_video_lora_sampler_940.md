---
name: unknown_workflow_video_lora_sampler_940
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.612
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedNode, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json, 视频生成/文生视频/MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_940

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json、视频生成/文生视频/MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
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
- `MiniMaxH3SigmaShift`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
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
- `ApplyVDNH3Advanced` —— 1/2 个有
- `DLSS5EnhanceImages` —— 1/2 个有
- `DLSS5Settings` —— 1/2 个有
- `FrameInterpolate` —— 1/2 个有
- `FrameInterpolationModelLoader` —— 1/2 个有
- `H3FaceStitch` —— 1/2 个有
- `H3FaceTrackCrop` —— 1/2 个有
- `H3InjectVideoLatent` —— 1/2 个有
- `H3PerFrameDenoise` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `RH_DLSS5FrameInterpolation` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
