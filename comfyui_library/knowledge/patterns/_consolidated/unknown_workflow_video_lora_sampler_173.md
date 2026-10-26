---
name: unknown_workflow_video_lora_sampler_173
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.52075
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json, 视频生成/文生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085458700025815041.json, 视频生成/文生视频/MiniMax H3官方工作流 _ 文生视频_2090001932441178113.json, 视频生成/文生视频/MiniMax H3文生视频-电商带货-手机取物换装_2107724379915374594.json, 视频生成/文生视频/MiniMax H3首尾帧（单图）工作流_2096917787607396353.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107269860387545089.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107472060179107841.json, 视频生成/文生视频/【中近景特写使用】MiniMax H3单采去油腻_2094069348838232066.json, 视频生成/文生视频/【中远景使用】MiniMax H3 双采去油腻_2094069310686846977.json, 视频生成/文生视频/动漫短剧文戏最佳组合（混合模型+结构lora+二采潜空间放大）_2094308569922498562.json, 视频生成/文生视频/直播带货知识分享（混合模型+结构lora+二采潜空间放大）_2094570516450471938.json, 视频生成/文生视频/知识分享单人视频生成器_2103751628326260737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_173

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json、视频生成/文生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085458700025815041.json、视频生成/文生视频/MiniMax H3官方工作流 _ 文生视频_2090001932441178113.json、视频生成/文生视频/MiniMax H3文生视频-电商带货-手机取物换装_2107724379915374594.json、视频生成/文生视频/MiniMax H3首尾帧（单图）工作流_2096917787607396353.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `VAEDecode` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `PrimitiveFloat` —— 9/12 个有
- `Text` —— 9/12 个有
- `LoadImage` —— 8/12 个有
- `MiniMaxH3ReferenceToVideo` —— 8/12 个有
- `SplitSigmas` —— 5/12 个有
- `LTXVConcatAVLatent` —— 4/12 个有
- `LTXVSeparateAVLatent` —— 4/12 个有
- `MiniMaxH3ImageToVideo` —— 4/12 个有
- `MinimaxH3LatentUpscaler3D` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `Float` —— 3/12 个有
- `ModelAttentionBackend` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `Text Multiline` —— 3/12 个有
- `easy float` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `LoadAudio` —— 2/12 个有
- `MiniMaxH3AVDecodeT8` —— 2/12 个有
- `RunningHub Deepcleaner` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `SigmasGraph` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
