---
name: unknown_workflow_video_lora_sampler_296
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.487
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3文生视频，首尾帧+放大_2086693311015907329.json, 视频生成/文生视频/MINIMAX-H3 多参+高清2采工作流_2084593623919845377.json, 视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json, 视频生成/文生视频/MiniMax H3 多参2采8步加速_2091443109673660417.json, 视频生成/文生视频/MiniMax H3 多图参考双采短剧视频生成工作流_2104589979459612673.json, 视频生成/文生视频/MiniMax H3官方工作流_多参考生成视频_2090004683493560321.json, 视频生成/文生视频/MiniMax H3开源 超级多合一 文生图生多参合一工作流-官方版_2086415506692722689.json, 视频生成/文生视频/MiniMax H3超级多合一工作流_2089374116016119810.json, 视频生成/文生视频/MiniMax H3超级多合一工作流（加速rola+二采）_2087353258498158593.json, 视频生成/文生视频/MiniMax+H3多参全能整合工作流_2090073717442441217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_296

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/H3文生视频，首尾帧+放大_2086693311015907329.json、视频生成/文生视频/MINIMAX-H3 多参+高清2采工作流_2084593623919845377.json、视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json、视频生成/文生视频/MiniMax H3 多参2采8步加速_2091443109673660417.json、视频生成/文生视频/MiniMax H3 多图参考双采短剧视频生成工作流_2104589979459612673.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `VAEEncode` —— 9/10 个有
- `VHS_LoadVideo` —— 9/10 个有
- `Text` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `VAEDecode` —— 7/10 个有
- `VAEEncodeAudio` —— 7/10 个有
- `PT_H3ConcatAVLatent` —— 6/10 个有
- `PreviewImage` —— 6/10 个有
- `MiniMaxH3AVDecodeT8` —— 5/10 个有
- `VAEDecodeAudio` —— 5/10 个有
- `MiniMaxH3ImageToVideo` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `LTXVConcatAVLatent` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `RunningHub Deepcleaner` —— 3/10 个有
- `孤海注释` —— 3/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `CreateVideo` —— 1/10 个有
- `DapaoH3LocalPromptNode` —— 1/10 个有
- `Float` —— 1/10 个有
- `Int` —— 1/10 个有
- `Int2String` —— 1/10 个有
- `JjkShowText` —— 1/10 个有
- `PrimitiveString` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `SaveVideo` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
