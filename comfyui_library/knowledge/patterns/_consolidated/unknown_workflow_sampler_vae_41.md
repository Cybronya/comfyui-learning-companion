---
name: unknown_workflow_sampler_vae_41
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8155
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json, 视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json, 视频生成/图生视频/MiniMax H3 图生视频｜一采生成 + 二采精修｜音画同步高清工作流_2086606849025073153.json, 视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json, 视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json, 视频生成/图生视频/MiniMax H3全能参考（图片、音频、视频皆可参考）_2084166446040567809.json, 视频生成/图生视频/MiniMax+H3+图生视频_首尾帧低显存加速版(6~8GB)_2085705273888559106.json, 视频生成/文生视频/MINIMAX-H3 sage+sol att双加速低显存全功能工作流_2084920261798879233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_41

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json、视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json、视频生成/图生视频/MiniMax H3 图生视频｜一采生成 + 二采精修｜音画同步高清工作流_2086606849025073153.json、视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json、视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `MiniMaxH3ImageToVideo` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `MiniMaxH3ReferenceToVideo` —— 4/8 个有
- `DiffusionModelLoaderKJ` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `UniBlockSwap` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `LTXVConcatAVLatent` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有
- `UniBlockSwapTE` —— 1/8 个有
- `VAEEncode` —— 1/8 个有
- `VAEEncodeAudio` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
