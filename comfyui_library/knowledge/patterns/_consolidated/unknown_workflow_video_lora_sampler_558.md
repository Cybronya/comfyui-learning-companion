---
name: unknown_workflow_video_lora_sampler_558
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78275
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, DiffusionModelLoaderKJ, Fast Groups Bypasser (rgthree), KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UniBlockSwap, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json, 视频生成/文生视频/MiniMax+H3+文生_图生视频_首尾帧+双采高清加速版+_2087401112684027906.json, 视频生成/文生视频/MiniMax+H3多参双采latent放大版_2090080342467235842.json, 视频生成/文生视频/MiniMax+H3文生视频双采latent放大版_2090080368669057026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_558

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json、视频生成/文生视频/MiniMax+H3+文生_图生视频_首尾帧+双采高清加速版+_2087401112684027906.json、视频生成/文生视频/MiniMax+H3多参双采latent放大版_2090080342467235842.json、视频生成/文生视频/MiniMax+H3文生视频双采latent放大版_2090080368669057026.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UniBlockSwap`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CS-MultiImageLoader` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LTXVConcatAVLatent` —— 2/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `ManualSigmas` —— 2/4 个有
- `MiniMaxH3AVDecodeT8` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `MinimaxH3LatentUpscaler3D` —— 2/4 个有
- `PT_H3ConcatAVLatent` —— 2/4 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 2/4 个有
- `RunningHub Deepcleaner` —— 2/4 个有
- `ShowText|fofo` —— 2/4 个有
- `VAEDecodeAudio` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `VAEEncodeAudio` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `UNETLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
