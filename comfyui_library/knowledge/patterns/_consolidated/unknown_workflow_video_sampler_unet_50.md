---
name: unknown_workflow_video_sampler_unet_50
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.657333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json, 视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json, 视频生成/图生视频/MiNiMaxH3_六图+三音频参考_2111108549219799042.json, 视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json, 视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json, 视频生成/图生视频/【MINIMAX-H3】最强W版武戏-极速版_2111450852316770305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json、视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json、视频生成/图生视频/MiNiMaxH3_六图+三音频参考_2111108549219799042.json、视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json、视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
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
- `LoadAudio` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `ExtendIntermediateSigmas` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `H3SigmaRefiner` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `忽略多组孤海` —— 4/6 个有
- `LoraLoaderBypassModelOnly` —— 2/6 个有
- `SolAttnMiniMax` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3BlockCacheT8` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text` —— 1/6 个有
- `VOSR2ModelLoader` —— 1/6 个有
- `VOSR2Upscale` —— 1/6 个有
- `XB_BatchImages` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
