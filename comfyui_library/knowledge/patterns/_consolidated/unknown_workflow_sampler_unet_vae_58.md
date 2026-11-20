---
name: unknown_workflow_sampler_unet_vae_58
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.603467
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 FL2V｜首尾帧锁定，国风画面丝滑动起来_2116023128378920961.json, 视频生成/图生视频/MiniMax H3全能参考生视频_2084114253300199425.json, 视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）_2087383302742298625.json, 视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）（9参考图3视频）_2087443247135281154.json, 视频生成/图生视频/MiniMax H3全能参考生视频（自定义背景+自定义人物+动作迁移）​_2088807649155567617.json, 视频生成/图生视频/MiniMax H3全能参考生视频，图片、视频。音频参考（动作迁移）_2085606340298366977.json, 视频生成/图生视频/Minimax-动作迁移_2086299017864114177.json, 视频生成/图生视频/Minimax3-参考生视频-8月8日版_2086541785450500098.json, 视频生成/图生视频/h3自定义背景人物换视频背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2092949782200414209.json, 视频生成/图生视频/h3自定义背景换视频背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2092910196111794178.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-文生+图生视频（支持首尾帧）_2084260178744139778.json, 视频生成/图生视频/自定义背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2091761423037853697.json, 视频生成/文生视频/H3-多功能工作流_2084183787587596289.json, 视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json, 视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_58

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 FL2V｜首尾帧锁定，国风画面丝滑动起来_2116023128378920961.json、视频生成/图生视频/MiniMax H3全能参考生视频_2084114253300199425.json、视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）_2087383302742298625.json、视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）（9参考图3视频）_2087443247135281154.json、视频生成/图生视频/MiniMax H3全能参考生视频（自定义背景+自定义人物+动作迁移）​_2088807649155567617.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `CreateVideo` —— 13/15 个有
- `Fast Groups Bypasser (rgthree)` —— 13/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/15 个有
- `MiniMaxH3ReferenceToVideo` —— 13/15 个有
- `SaveVideo` —— 13/15 个有
- `CR Prompt Text` —— 11/15 个有
- `GetNode` —— 11/15 个有
- `LoadAudio` —— 11/15 个有
- `SetNode` —— 11/15 个有
- `VHS_LoadVideo` —— 11/15 个有
- `MiniMaxChunkFeedForward` —— 3/15 个有
- `MiniMaxH3ImageToVideo` —— 3/15 个有
- `MiniMaxLowVRAMAttention` —— 3/15 个有
- `PrimitiveStringMultiline` —— 3/15 个有
- `ModelAttentionBackend` —— 2/15 个有
- `ModelPreviewOverrideKJ` —— 2/15 个有
- `VHS_VideoCombine` —— 2/15 个有
- `Any Switch (rgthree)` —— 1/15 个有
- `EasyCache` —— 1/15 个有
- `GetImageRangeFromBatch` —— 1/15 个有
- `MiniMaxH3AddGuide` —— 1/15 个有
- `SpectrumApplyMiniMaxH3` —— 1/15 个有
- `TrimAudioDuration` —— 1/15 个有
- `easy float` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
