---
name: unknown_workflow_video_sampler_unet_47
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6406
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json, 视频生成/文生视频/MINIMAX-H3-文生视频_2084191170879643650.json, 视频生成/文生视频/MiniMax H3  文生视频工作流_2084912279681851394.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2092541585006354433.json, 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json, 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json, 视频生成/文生视频/Minimax-H3VDN-R2V 视频生成工作流（RH在线流）_2096816318430404609.json, 视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json、视频生成/文生视频/MINIMAX-H3-文生视频_2084191170879643650.json、视频生成/文生视频/MiniMax H3  文生视频工作流_2084912279681851394.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `PathchSageAttentionKJ` —— 7/10 个有
- `MiniMaxH3ImageToVideo` —— 6/10 个有
- `LoadImage` —— 5/10 个有
- `MiniMaxH3SigmaShift` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `Label (rgthree)` —— 4/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `MiniMaxH3ReferenceToVideo` —— 4/10 个有
- `LoadAudio` —— 3/10 个有
- `StringConcatenate` —— 3/10 个有
- `Text` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `MiniMaxChunkFeedForward` —— 2/10 个有
- `ModelPatchTorchSettings` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `H3FaceStitch` —— 1/10 个有
- `H3FaceTrackCrop` —— 1/10 个有
- `H3InjectVideoLatent` —— 1/10 个有
- `H3PerFrameDenoise` —— 1/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/10 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `PainterVRAM` —— 1/10 个有
- `SeedNode` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
