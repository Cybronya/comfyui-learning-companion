---
name: unknown_workflow_video_upscale_latent_upscale_120
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.664333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/【终极版本】MiniMax H3 双采高清工作流 提速不降质【AI小王子】_2095420966586376194.json, 视频生成/文生视频/动漫短剧文戏最佳组合（混合模型+结构lora+二采潜空间放大）_2094308569922498562.json, 视频生成/文生视频/动漫短剧武戏最强工作流（模型、提示词二选一）_2095498147790417922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_120

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/【终极版本】MiniMax H3 双采高清工作流 提速不降质【AI小王子】_2095420966586376194.json、视频生成/文生视频/动漫短剧文戏最佳组合（混合模型+结构lora+二采潜空间放大）_2094308569922498562.json、视频生成/文生视频/动漫短剧武戏最强工作流（模型、提示词二选一）_2095498147790417922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
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
- `ExtendIntermediateSigmas` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `H3SigmaRefiner` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `LamSwitcherCase` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
