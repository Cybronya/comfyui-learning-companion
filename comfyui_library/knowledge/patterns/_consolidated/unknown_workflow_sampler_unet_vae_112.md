---
name: unknown_workflow_sampler_unet_vae_112
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.641273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3 关键帧视频动画_2106371268684636162.json, 视频生成/文生视频/MINIMAX-H3-多参考生视频_2084144392893452289.json, 视频生成/文生视频/MINIMAX-H3工作流合集_2084536680941441025.json, 视频生成/文生视频/MINIMAX-H3工作流合集_2084552719951556609.json, 视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json, 视频生成/文生视频/MiniMax H3 二采去油不爆音加速工作流_2096198192596606977.json, 视频生成/文生视频/MiniMax H3 全能视频V3_2095061357325545474.json, 视频生成/文生视频/MiniMax H3 多合一全能生视频极速+二采优化版_2097343290071928833.json, 视频生成/文生视频/MiniMax H3 武戏全能视频V3_2095388978387185666.json, 视频生成/文生视频/Minimax H3 双采样全能参考高清工作流｜超分放大｜4倍加速｜8倍加速_2092731840196079618.json, 视频生成/文生视频/Minimax H3 双采样全能参考｜真实电影感｜超分高清放大｜4倍加速｜8倍加速_2094320738051383298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_112

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/H3 关键帧视频动画_2106371268684636162.json、视频生成/文生视频/MINIMAX-H3-多参考生视频_2084144392893452289.json、视频生成/文生视频/MINIMAX-H3工作流合集_2084536680941441025.json、视频生成/文生视频/MINIMAX-H3工作流合集_2084552719951556609.json、视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 10/11 个有
- `LoadAudio` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `CreateVideo` —— 7/11 个有
- `GetNode` —— 7/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `LTXVConcatAVLatent` —— 6/11 个有
- `LTXVSeparateAVLatent` —— 6/11 个有
- `MinimaxH3LatentUpscaler3D` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 5/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `SplitSigmas` —— 5/11 个有
- `MiniMaxH3SigmaShift` —— 4/11 个有
- `Text` —— 4/11 个有
- `VHS_VideoCombine` —— 4/11 个有
- `H3SigmaRefiner` —— 3/11 个有
- `MiniMaxLowVRAMAttention` —— 3/11 个有
- `easy float` —— 3/11 个有
- `忽略多组孤海` —— 3/11 个有
- `FlashVSRNode` —— 2/11 个有
- `HAIGC_VideoLoader` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `Sleep` —— 2/11 个有
- `孤海注释` —— 2/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `ExtendIntermediateSigmas` —— 1/11 个有
- `MiniMaxChunkFeedForward` —— 1/11 个有
- `MiniMaxH3TurboSampler` —— 1/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `SaveImage` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
