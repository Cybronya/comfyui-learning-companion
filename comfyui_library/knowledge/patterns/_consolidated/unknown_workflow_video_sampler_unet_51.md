---
name: unknown_workflow_video_sampler_unet_51
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.478167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/官方 全能参考版单采_2104530172652380161.json, 视频生成/文生视频/工作流lin_2099078938155896833.json, 视频生成/文生视频/直播带货知识分享（混合模型+结构lora+二采潜空间放大）_2094570516450471938.json, 视频生成/文生视频/知识分享单人视频生成器_2103751628326260737.json, 视频生成/文生视频/视频生成API_2099703467815292929.json, 视频生成/视频生视频/-MiniMax H3-多参考生视频-优化版_2106660994788446209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_51

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/官方 全能参考版单采_2104530172652380161.json、视频生成/文生视频/工作流lin_2099078938155896833.json、视频生成/文生视频/直播带货知识分享（混合模型+结构lora+二采潜空间放大）_2094570516450471938.json、视频生成/文生视频/知识分享单人视频生成器_2103751628326260737.json、视频生成/文生视频/视频生成API_2099703467815292929.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 5/6 个有
- `LTXVSeparateAVLatent` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MinimaxH3LatentUpscaler3D` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `easy float` —— 5/6 个有
- `Text` —— 4/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `忽略多组孤海` —— 3/6 个有
- `Text Multiline` —— 2/6 个有
- `AudioSeparation` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Float` —— 1/6 个有
- `Lora Loader Stack (rgthree)` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `SolAttnMiniMax` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
