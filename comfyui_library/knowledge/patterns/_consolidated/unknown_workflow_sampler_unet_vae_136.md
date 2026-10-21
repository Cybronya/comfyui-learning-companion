---
name: unknown_workflow_sampler_unet_vae_136
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.845
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 生成场景 8 视图（可以场景中某物为中心）_2092374389412155393.json, 视频生成/图生视频/Minimax H3 生成角色 6 视图 + 360°旋转+人脸特写 视频_2092354483618672642.json, 视频生成/图生视频/【老金驿站】MinimaxH3生成人物三视图工作流_2089550852343291906.json, 视频生成/文生视频/H3 关键帧视频动画_2106371268684636162.json, 视频生成/文生视频/minmaxH3单采+1参考视频_2105350818894536705.json, 视频生成/文生视频/minmaxH3单采加速_2105257162896404482.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_136

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 生成场景 8 视图（可以场景中某物为中心）_2092374389412155393.json、视频生成/图生视频/Minimax H3 生成角色 6 视图 + 360°旋转+人脸特写 视频_2092354483618672642.json、视频生成/图生视频/【老金驿站】MinimaxH3生成人物三视图工作流_2089550852343291906.json、视频生成/文生视频/H3 关键帧视频动画_2106371268684636162.json、视频生成/文生视频/minmaxH3单采+1参考视频_2105350818894536705.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `ComfyMathExpression` —— 3/6 个有
- `ImageFromBatch` —— 3/6 个有
- `ImageStitch` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `StringConcatenate` —— 3/6 个有
- `ExtendIntermediateSigmas` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `VAEDecodeAudio` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `BatchImagesNode` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `Text` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
