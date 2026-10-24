---
name: unknown_workflow_sampler_unet_vae_180
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.910833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json, 视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json, 视频生成/文生视频/MiniMax H3 文生视频 8步加速_2085538844547575810.json, 视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json, 视频生成/文生视频/MiniMax-H3文生视频人物类特效数字人工作流_2090000867746476033.json, 视频生成/文生视频/minimax 首尾帧加速版_2084471697830404098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_180

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json、视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json、视频生成/文生视频/MiniMax H3 文生视频 8步加速_2085538844547575810.json、视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json、视频生成/文生视频/MiniMax-H3文生视频人物类特效数字人工作流_2090000867746476033.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `ComfyMathExpression` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `Int` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `ResizeImagesByLongerEdge` —— 3/6 个有
- `ImageResize+` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
