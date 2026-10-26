---
name: unknown_workflow_video_lora_sampler_196
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.521636
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MINIMAX-H3 多参+二采2K直出-官方API_2086843177985732610.json, 视频生成/文生视频/MINIMAX-H3 多参+高清2采工作流_2084593623919845377.json, 视频生成/文生视频/MiniMax H3官方工作流_多参考生成视频_2090004683493560321.json, 视频生成/文生视频/MiniMax H3开源 超级多合一 文生图生多参合一工作流-官方版_2086415506692722689.json, 视频生成/文生视频/MiniMax H3超级多合一工作流（加速rola+二采）_2087353258498158593.json, 视频生成/文生视频/MiniMax+H3多参全能整合工作流_2090073717442441217.json, 视频生成/文生视频/MiniMax+H3超级多合_2086713203135967234.json, 视频生成/文生视频/MiniMax+H3超级多合一工作流-官方版V2_2088289193456922626.json, 视频生成/文生视频/MiniMaxH3官方版超级多合一工作流ENG+ENG_2087111558542479361.json, 视频生成/文生视频/李哈哈自用3_2087402730037014530.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_196

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MINIMAX-H3 多参+二采2K直出-官方API_2086843177985732610.json、视频生成/文生视频/MINIMAX-H3 多参+高清2采工作流_2084593623919845377.json、视频生成/文生视频/MiniMax H3官方工作流_多参考生成视频_2090004683493560321.json、视频生成/文生视频/MiniMax H3开源 超级多合一 文生图生多参合一工作流-官方版_2086415506692722689.json、视频生成/文生视频/MiniMax H3超级多合一工作流（加速rola+二采）_2087353258498158593.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 10/11 个有
- `LoadAudio` —— 10/11 个有
- `PT_H3ConcatAVLatent` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `VAEEncode` —— 10/11 个有
- `VHS_LoadVideo` —— 10/11 个有
- `GetNode` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `MiniMaxH3AVDecodeT8` —— 8/11 个有
- `Text` —— 8/11 个有
- `VAEDecode` —— 8/11 个有
- `VAEEncodeAudio` —— 8/11 个有
- `孤海注释` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `RunningHub Deepcleaner` —— 7/11 个有
- `MiniMaxH3ImageToVideo` —— 6/11 个有
- `CreateVideo` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `VAEDecodeAudio` —— 3/11 个有
- `Int` —— 2/11 个有
- `SaveVideo` —— 2/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `DapaoH3LocalPromptNode` —— 1/11 个有
- `Int2String` —— 1/11 个有
- `JjkShowText` —— 1/11 个有
- `MiniMaxChunkFeedForward` —— 1/11 个有
- `MiniMaxLowVRAMAttention` —— 1/11 个有
- `MuyeLoadImage` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `PrimitiveString` —— 1/11 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/11 个有
- `忽略多组孤海` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
