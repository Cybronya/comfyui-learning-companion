---
name: unknown_workflow_upscale_latent_upscale_lora_33
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9528
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 的 100% 实力释放图生视频三阶段采样工作流_2034922243968471041.json, 视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json, 视频生成/文生视频/LTX-2.3三阶渲染1+3数字人100%性能释放_2034922238251634690.json, 视频生成/文生视频/LTX-2三阶渲染1+3数字人100%性能释放_2034922123667447810.json, 视频生成/文生视频/VBVR数字人_2043983796604768258.json, 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473.json, 视频生成/文生视频/『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938.json, 视频生成/文生视频/图片+音频数字人 2.0｜Dev-Dare + VBVR 最终版_2051722678544941058.json, 视频生成/文生视频/图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626.json, 视频生成/文生视频/音频数字人 2.0｜三阶渲染打磨版，人物说话更自然_2050906015968837633.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 的 100% 实力释放图生视频三阶段采样工作流_2034922243968471041.json、视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json、视频生成/文生视频/LTX-2.3三阶渲染1+3数字人100%性能释放_2034922238251634690.json、视频生成/文生视频/LTX-2三阶渲染1+3数字人100%性能释放_2034922123667447810.json、视频生成/文生视频/VBVR数字人_2043983796604768258.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 9/10 个有
- `CM_FloatToInt` —— 9/10 个有
- `GetLatentSizeAndCount` —— 9/10 个有
- `JWImageResizeByLongerSide` —— 9/10 个有
- `LTXVAudioVAEEncode` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `MelBandRoFormerModelLoader` —— 9/10 个有
- `MelBandRoFormerSampler` —— 9/10 个有
- `SetLatentNoiseMask` —— 9/10 个有
- `SolidMask` —— 9/10 个有
- `TrimAudioDuration` —— 9/10 个有
- `VAEDecodeTiled` —— 9/10 个有
- `image_scale_pixel_v2` —— 9/10 个有
- `Float` —— 6/10 个有
- `LTX2_NAG` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `SimpleMath+` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `VRAMReserver` —— 5/10 个有
- `PromptRelayEncode` —— 4/10 个有
- `Seed Everywhere` —— 3/10 个有
- `SimpleCalculatorKJ` —— 3/10 个有
- `Text` —— 2/10 个有
- `INTConstant` —— 1/10 个有
- `KepStringLiteral` —— 1/10 个有
- `LTXFloatToInt` —— 1/10 个有
- `LTXVTiledVAEDecode` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `SetNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
