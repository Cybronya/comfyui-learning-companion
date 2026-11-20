---
name: unknown_workflow_video_lora_sampler_175
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.790364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, DiffusionModelLoaderKJ, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UniBlockSwap, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MiniMax_H3_活人爱神8步_2098940180483891201.json, 图片生成/图生图/MiniMax_H3_活人爱神8步_2099052125048365057.json, 图片生成/图生图/MiniMax_H3_活人爱神8步_2099677604700844034.json, 视频生成/图生视频/H3 八步图生视频｜5秒预检版_2098722980808445953.json, 视频生成/文生视频/MiniMax H3 活人感多合一视频工作流_2103421922276106242.json, 视频生成/文生视频/MiniMax H3 活人爱神8步_2097733630738128897.json, 视频生成/文生视频/MiniMax H3一键直出活人感女友二采工作流_2098322238746480641.json, 视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json, 视频生成/文生视频/MiniMax+H3+文生_图生视频_首尾帧+双采高清加速版+_2087401112684027906.json, 视频生成/文生视频/MiniMax+H3多参双采latent放大版_2090080342467235842.json, 视频生成/文生视频/MiniMax+H3文生视频双采latent放大版_2090080368669057026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_175

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/MiniMax_H3_活人爱神8步_2098940180483891201.json、图片生成/图生图/MiniMax_H3_活人爱神8步_2099052125048365057.json、图片生成/图生图/MiniMax_H3_活人爱神8步_2099677604700844034.json、视频生成/图生视频/H3 八步图生视频｜5秒预检版_2098722980808445953.json、视频生成/文生视频/MiniMax H3 活人感多合一视频工作流_2103421922276106242.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UniBlockSwap`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/11 个有
- `Label (rgthree)` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `SaveImage` —— 10/11 个有
- `CS-MultiImageLoader` —— 9/11 个有
- `LTXVConcatAVLatent` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 9/11 个有
- `MiniMaxH3ReferenceToVideo` —— 9/11 个有
- `MinimaxH3LatentUpscaler3D` —— 9/11 个有
- `VAEDecodeAudio` —— 9/11 个有
- `LoadAudio` —— 8/11 个有
- `ManualSigmas` —— 8/11 个有
- `VHS_LoadVideo` —— 8/11 个有
- `ModelAttentionBackend` —— 7/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/11 个有
- `EmptyImage` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `MiniMaxH3AVDecodeT8` —— 2/11 个有
- `MiniMaxH3ImageToVideo` —— 2/11 个有
- `PT_H3ConcatAVLatent` —— 2/11 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 2/11 个有
- `RunningHub Deepcleaner` —— 2/11 个有
- `ShowText|fofo` —— 2/11 个有
- `VAEEncode` —— 2/11 个有
- `VAEEncodeAudio` —— 2/11 个有
- `UNETLoader` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
