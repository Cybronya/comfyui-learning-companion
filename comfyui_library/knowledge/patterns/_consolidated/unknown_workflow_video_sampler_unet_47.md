---
name: unknown_workflow_video_sampler_unet_47
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.889625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3-双角色+指定背景3图生视频！加速版！_2089258074396774402.json, 视频生成/图生视频/MiniMaxH3多参MV生成工作流 By 像素幻想Lab_2087128116820013058.json, 视频生成/图生视频/MiniMaxH3首尾帧工作流 By 像素幻想Lab_2087128132951298049.json, 视频生成/图生视频/Minimax-H3 多参考图  电商服装视频_2089669546205601794.json, 视频生成/图生视频/Minimax-H3 多参考图_2085260972230537218.json, 视频生成/图生视频/minMax+H3+二采放大_2091513919167885314.json, 视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2100863837363851266.json, 视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2101132610901733377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3-双角色+指定背景3图生视频！加速版！_2089258074396774402.json、视频生成/图生视频/MiniMaxH3多参MV生成工作流 By 像素幻想Lab_2087128116820013058.json、视频生成/图生视频/MiniMaxH3首尾帧工作流 By 像素幻想Lab_2087128132951298049.json、视频生成/图生视频/Minimax-H3 多参考图  电商服装视频_2089669546205601794.json、视频生成/图生视频/Minimax-H3 多参考图_2085260972230537218.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `JjkText` —— 3/8 个有
- `LoadAudio` —— 2/8 个有
- `LoraLoaderBypassModelOnly` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 2/8 个有
- `Audio Duration (mtb)` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `LTXVConcatAVLatent` —— 1/8 个有
- `LTXVSeparateAVLatent` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `MinimaxH3LatentUpscaler3D` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
