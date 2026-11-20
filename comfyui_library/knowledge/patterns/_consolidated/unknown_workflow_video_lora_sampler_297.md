---
name: unknown_workflow_video_lora_sampler_297
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5058
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Text, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频_2090311300034424833.json, 视频生成/文生视频/MiniMax H3(全能多图参考生视频)4步Lora超级加速版_2085360950907064321.json, 视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json, 视频生成/文生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085458700025815041.json, 视频生成/文生视频/MiniMax H3官方工作流 _ 文生视频_2090001932441178113.json, 视频生成/文生视频/MiniMax H3文生视频-电商带货-手机取物换装_2107724379915374594.json, 视频生成/文生视频/MiniMax H3首尾帧（单图）工作流_2096917787607396353.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107269860387545089.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107472060179107841.json, 视频生成/文生视频/【中近景特写使用】MiniMax H3单采去油腻_2094069348838232066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_297

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频_2090311300034424833.json、视频生成/文生视频/MiniMax H3(全能多图参考生视频)4步Lora超级加速版_2085360950907064321.json、视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json、视频生成/文生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085458700025815041.json、视频生成/文生视频/MiniMax H3官方工作流 _ 文生视频_2090001932441178113.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 10 个 workflow 都包含：
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
- `Text`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `VAEDecode` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `PrimitiveFloat` —— 7/10 个有
- `LoadImage` —— 5/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `Float` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `SigmasGraph` —— 3/10 个有
- `EmptyImage` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `MiniMaxH3AVDecodeT8` —— 2/10 个有
- `RunningHub Deepcleaner` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `SplitSigmas` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
