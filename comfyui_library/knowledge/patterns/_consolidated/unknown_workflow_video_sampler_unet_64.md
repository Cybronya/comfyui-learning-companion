---
name: unknown_workflow_video_sampler_unet_64
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8105
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json, 视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json, 视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json, 视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json、视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json、视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json、视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Label (rgthree)` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Float` —— 1/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `SolAttnMiniMax` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
