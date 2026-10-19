---
name: unknown_workflow_sampler_unet_vae_143
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6624
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json, 视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json, 视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json, 视频生成/文生视频/MiniMax H3 全能参考+文生_首尾帧合集_2085595735755681793.json, 视频生成/文生视频/MiniMax H3 全能参考_2084592147357061122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_143

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json、视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json、视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json、视频生成/文生视频/MiniMax H3 全能参考+文生_首尾帧合集_2085595735755681793.json、视频生成/文生视频/MiniMax H3 全能参考_2084592147357061122.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `MiniMaxH3ImageToVideo` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `GetVideoComponents` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Image Batch` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
