---
name: unknown_workflow_video_sampler_unet_18
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.5573
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3 海螺 4步lightx2v加速lora 多重提速 图生视频工作流_2084221979170795521.json, 视频生成/图生视频/minimax H3巨物图生视频_2093886571169796098.json, 视频生成/图生视频/minimax H3巨物图生视频_2097867227113541634.json, 视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json, 视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json, 视频生成/文生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085602340672987137.json, 视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2092541585006354433.json, 视频生成/文生视频/MiniMax H3 手机取物换装 文生视频_2106940320041750529.json, 视频生成/文生视频/MiniMax H3 文生视频_2090311300034424833.json, 视频生成/文生视频/MiniMax H3(全能多图参考生视频)4步Lora超级加速版_2085360950907064321.json, 视频生成/文生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085458700025815041.json, 视频生成/文生视频/MiniMax H3文生视频-电商带货-手机取物换装_2107724379915374594.json, 视频生成/文生视频/MiniMax+H3  9 图_2085645558315831298.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107269860387545089.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107472060179107841.json, 视频生成/文生视频/【中近景特写使用】MiniMax H3单采去油腻_2094069348838232066.json, 视频生成/文生视频/【中远景使用】MiniMax H3 双采去油腻_2094069310686846977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_18

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3 海螺 4步lightx2v加速lora 多重提速 图生视频工作流_2084221979170795521.json、视频生成/图生视频/minimax H3巨物图生视频_2093886571169796098.json、视频生成/图生视频/minimax H3巨物图生视频_2097867227113541634.json、视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json、视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 17/20 个有
- `LoraLoaderModelOnly` —— 16/20 个有
- `GetNode` —— 15/20 个有
- `MiniMaxH3ImageToVideo` —— 15/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/20 个有
- `SetNode` —— 15/20 个有
- `Text` —— 15/20 个有
- `LoadImage` —— 12/20 个有
- `Label (rgthree)` —— 7/20 个有
- `MiniMaxH3ReferenceToVideo` —— 5/20 个有
- `ModelAttentionBackend` —— 4/20 个有
- `SplitSigmas` —— 4/20 个有
- `Float` —— 3/20 个有
- `ShowText|pysssss` —— 3/20 个有
- `SigmasGraph` —— 3/20 个有
- `EmptyImage` —— 2/20 个有
- `Fast Groups Bypasser (rgthree)` —— 2/20 个有
- `ManualSigmas` —— 2/20 个有
- `MuyeTextEditOutput` —— 2/20 个有
- `PreviewImage` —— 2/20 个有
- `RHLLMChatNode` —— 2/20 个有
- `LTXVConcatAVLatent` —— 1/20 个有
- `LTXVSeparateAVLatent` —— 1/20 个有
- `MinimaxH3LatentUpscaler3D` —— 1/20 个有
- `StariAI-MiniMaxH3-Skill` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
