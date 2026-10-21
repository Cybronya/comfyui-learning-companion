---
name: unknown_workflow_video_upscale_latent_upscale_12
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.424789
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy float]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-图生视频_2103135562264834050.json, 视频生成/图生视频/MiniMax H3-多参考生视频 快速高质量_2098739556991455233.json, 视频生成/图生视频/MiniMax H3-多参考生视频-720p_2094616194417516546.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2094397865706737666.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108223200814518274.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108234638559899650.json, 视频生成/图生视频/MiniMax H3-多参考生视频-去油王版_2094419718181572610.json, 视频生成/图生视频/MiniMax H3-多参考生视频-去油王版_2111461486425100290.json, 视频生成/图生视频/MiniMax H3-多参考生视频-自用_2099876679551377409.json, 视频生成/图生视频/MiniMax H3-多参考生视频-高质量hybrid_2095884837700853761.json, 视频生成/图生视频/MiniMax H3多参生视频优化版_支持参考9图3音3视频_2094385613003911169.json, 视频生成/图生视频/MiniMax H3开源-多参考生视频-优化版_2094015909143867394.json, 视频生成/图生视频/MiniMax H3开源-多参考生视频-优化版_2094045987265404929.json, 视频生成/图生视频/MiniMax H3｜让每一帧，都有电影感_2099151915912359938.json, 视频生成/图生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-二优化版_2104051225640660993.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-优化版_2099771867585409025.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-优化版_2100032660772057090.json, 视频生成/图生视频/双倍高清放大MiniMax H3-多参考生视频-字节DMAD加速版_2106606807736209409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_12

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-图生视频_2103135562264834050.json、视频生成/图生视频/MiniMax H3-多参考生视频 快速高质量_2098739556991455233.json、视频生成/图生视频/MiniMax H3-多参考生视频-720p_2094616194417516546.json、视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2094397865706737666.json、视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108223200814518274.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：42%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 18/19 个有
- `VHS_LoadVideo` —— 18/19 个有
- `忽略多组孤海` —— 18/19 个有
- `孤海注释` —— 5/19 个有
- `llama_cpp_instruct_adv` —— 4/19 个有
- `llama_cpp_model_loader` —— 4/19 个有
- `llama_cpp_parameters` —— 4/19 个有
- `ShowText|pysssss` —— 3/19 个有
- `easy cleanGpuUsed` —— 3/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/19 个有
- `PreviewAny` —— 2/19 个有
- `Astra` —— 1/19 个有
- `CR Text` —— 1/19 个有
- `CreateVideo` —— 1/19 个有
- `EmptyImage` —— 1/19 个有
- `ImageFromBatch` —— 1/19 个有
- `ImageScale` —— 1/19 个有
- `Int` —— 1/19 个有
- `JjkText` —— 1/19 个有
- `LoadVideo` —— 1/19 个有
- `MiniMaxH3AVDecodeT8` —— 1/19 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/19 个有
- `SaveVideo` —— 1/19 个有
- `easy showAnything` —— 1/19 个有
- `获取视频信息` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
