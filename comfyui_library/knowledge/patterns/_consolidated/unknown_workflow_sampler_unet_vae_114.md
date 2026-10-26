---
name: unknown_workflow_sampler_unet_vae_114
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.910222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json, 视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json, 视频生成/文生视频/MiniMax H3 文生视频 8步加速_2085538844547575810.json, 视频生成/文生视频/MiniMax H3 文生视频_2084489178611539970.json, 视频生成/文生视频/MiniMax H3 文生视频_2084544656423088130.json, 视频生成/文生视频/MiniMax H3 首尾帧图生视频_2084850865038520322.json, 视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json, 视频生成/文生视频/MiniMax+H3+首帧图生视频_2084850825154875394.json, 视频生成/文生视频/minimax 首尾帧加速版_2084471697830404098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_114

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json、视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json、视频生成/文生视频/MiniMax H3 文生视频 8步加速_2085538844547575810.json、视频生成/文生视频/MiniMax H3 文生视频_2084489178611539970.json、视频生成/文生视频/MiniMax H3 文生视频_2084544656423088130.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `EasyCache` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `Int` —— 3/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/9 个有
- `ResizeImagesByLongerEdge` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `SolAttnPatch` —— 3/9 个有
- `ImageResize+` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 1/9 个有
- `PlaySound|pysssss` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
