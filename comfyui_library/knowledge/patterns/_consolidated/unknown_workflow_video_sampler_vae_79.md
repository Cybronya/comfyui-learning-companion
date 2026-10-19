---
name: unknown_workflow_video_sampler_vae_79
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.887429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/文戏多图参考生视频-MINIMAX-H3 -手动版_2094987834829660161.json, 视频生成/文生视频/MINIMAX-H3 图参考生视频_2091357639291785217.json, 视频生成/文生视频/MINIMAX-H3 多参+二采2K直出-官方API_2086843177985732610.json, 视频生成/文生视频/MINIMAX-H3 多参+高清2采工作流_2084593623919845377.json, 视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json, 视频生成/文生视频/MiniMax+H3+文生_图生视频_首尾帧+双采高清加速版+_2087401112684027906.json, 视频生成/文生视频/啊癫 MINIMAX-H3 多参生视频-二采版_2090845897457487873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_79

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/文戏多图参考生视频-MINIMAX-H3 -手动版_2094987834829660161.json、视频生成/文生视频/MINIMAX-H3 图参考生视频_2091357639291785217.json、视频生成/文生视频/MINIMAX-H3 多参+二采2K直出-官方API_2086843177985732610.json、视频生成/文生视频/MINIMAX-H3 多参+高清2采工作流_2084593623919845377.json、视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `VAEDecode` —— 5/7 个有
- `VAEEncodeAudio` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `ExtendIntermediateSigmas` —— 3/7 个有
- `H3SigmaRefiner` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `LoraLoaderBypassModelOnly` —— 3/7 个有
- `VAEDecodeAudio` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `DiffusionModelLoaderKJ` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `RunningHub Deepcleaner` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `UniBlockSwap` —— 2/7 个有
- `CS-MultiImageLoader` —— 1/7 个有
- `CreateVideo` —— 1/7 个有
- `MiniMaxH3ImageToVideo` —— 1/7 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/7 个有
- `SaveVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
