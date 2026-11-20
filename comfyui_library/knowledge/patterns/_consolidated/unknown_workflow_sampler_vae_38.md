---
name: unknown_workflow_sampler_vae_38
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8266
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json, 视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json, 视频生成/图生视频/MiniMax H3 图生视频｜一采生成 + 二采精修｜音画同步高清工作流_2086606849025073153.json, 视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json, 视频生成/图生视频/MiniMax H3全能参考（图片、音频、视频皆可参考）_2084166446040567809.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频加速版_2084302463045300225.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频加速版_2098314026001461250.json, 视频生成/图生视频/minimaxH3首尾帧视频工作流（超级加速版）_2084965664602804226.json, 视频生成/文生视频/MiniMax H3 多参生视频 加速版_2084297922312761346.json, 视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json、视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json、视频生成/图生视频/MiniMax H3 图生视频｜一采生成 + 二采精修｜音画同步高清工作流_2086606849025073153.json、视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json、视频生成/图生视频/MiniMax H3全能参考（图片、音频、视频皆可参考）_2084166446040567809.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
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
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `Label (rgthree)` —— 6/10 个有
- `MiniMaxH3ReferenceToVideo` —— 6/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/10 个有
- `LoadAudio` —— 3/10 个有
- `PathchSageAttentionKJ` —— 3/10 个有
- `DiffusionModelLoaderKJ` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ModelPreviewOverrideKJ` —— 2/10 个有
- `RTXVideoSuperResolution` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `LTXVConcatAVLatent` —— 1/10 个有
- `LTX_lora_loader` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `SpectrumApplyMiniMaxH3` —— 1/10 个有
- `TESpeedMiniMaxH3` —— 1/10 个有
- `VAEEncode` —— 1/10 个有
- `VAEEncodeAudio` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
