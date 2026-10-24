---
name: unknown_workflow_video_lora_sampler_571
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.646
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 四合一二采高清版_2086559082231713794.json, 视频生成/图生视频/H3极速二采高质量参考生视频_2086495362298236929.json, 视频生成/文生视频/minimax h3 二采高清工作流_2089238048839131137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_571

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 四合一二采高清版_2086559082231713794.json、视频生成/图生视频/H3极速二采高质量参考生视频_2086495362298236929.json、视频生成/文生视频/minimax h3 二采高清工作流_2089238048839131137.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `MiniMaxH3AVDecodeT8` —— 2/3 个有
- `MiniMaxH3AudioConditioningT8` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VAEEncodeAudio` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/3 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `TT_img_enc_v2` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEDecodeAudio` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
