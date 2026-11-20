---
name: unknown_workflow_video_lora_sampler_957
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, Int, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 四合一二采高清版_2086559082231713794.json, 视频生成/文生视频/minimax h3 二采高清工作流_2089238048839131137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_957

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 四合一二采高清版_2086559082231713794.json、视频生成/文生视频/minimax h3 二采高清工作流_2089238048839131137.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3AudioConditioningT8` —— 1/2 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TT_img_enc_v2` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
