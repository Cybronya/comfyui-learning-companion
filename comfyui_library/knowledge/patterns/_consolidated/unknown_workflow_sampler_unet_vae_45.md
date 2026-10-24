---
name: unknown_workflow_sampler_unet_vae_45
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.863
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json, 视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json, 视频生成/图生视频/MiniMax H3 图生视频｜一采生成 + 二采精修｜音画同步高清工作流_2086606849025073153.json, 视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json, 视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json, 视频生成/图生视频/MiniMax H3全能参考（图片、音频、视频皆可参考）_2084166446040567809.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频加速版_2098314026001461250.json, 视频生成/图生视频/MiniMax-图生视频-8步加速_2086020257013133313.json, 视频生成/图生视频/MiniMaxH3 图生视频！加速版！_2092799565484351490.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X2（二关键帧）视频生成工作流_2094650229818748929.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X4（四关键帧）视频生成工作流_2094650342708436993.json, 视频生成/图生视频/Minimax H3 多图参考生视频_2084688978254581762.json, 视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json, 视频生成/文生视频/Minimax-H3 多图参考_产品介绍视频_2090089362729033729.json, 视频生成/文生视频/Minimax-H3-4步加速-单图参考（二次采样_官方节点版）_2090043814345007105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_45

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json、视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json、视频生成/图生视频/MiniMax H3 图生视频｜一采生成 + 二采精修｜音画同步高清工作流_2086606849025073153.json、视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json、视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 12/15 个有
- `PrimitiveStringMultiline` —— 11/15 个有
- `LoraLoaderModelOnly` —— 10/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/15 个有
- `easy cleanGpuUsed` —— 6/15 个有
- `ModelAttentionBackend` —— 5/15 个有
- `EasyCache` —— 4/15 个有
- `Label (rgthree)` —— 4/15 个有
- `MiniMaxH3ImageToVideo` —— 4/15 个有
- `PathchSageAttentionKJ` —— 4/15 个有
- `RTXVideoSuperResolution` —— 4/15 个有
- `VAEEncode` —— 4/15 个有
- `VAEEncodeAudio` —— 4/15 个有
- `Float` —— 3/15 个有
- `ImageResizeKJv2` —— 3/15 个有
- `PT_H3ConcatAVLatent` —— 3/15 个有
- `Text` —— 3/15 个有
- `VRAMReserver` —— 3/15 个有
- `easy clearCacheAll` —— 3/15 个有
- `MiniMaxH3AddGuide` —— 2/15 个有
- `SaveImage` —— 2/15 个有
- `DiffusionModelLoaderKJ` —— 1/15 个有
- `DuckHideNode` —— 1/15 个有
- `LTXVConcatAVLatent` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
