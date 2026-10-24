---
name: unknown_workflow_sampler_clip_vae_59
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6885
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXFloatToInt, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 多图参考图生成视频｜+多图参考图 LORA ｜IC-LoRA-Ingredients_2067412522302529537.json, 视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json, 视频生成/文生视频/LTX2.3 In​gredients IC LORA全能参考_2070747298736463873.json, 视频生成/文生视频/LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 多图参考图生成视频｜+多图参考图 LORA ｜IC-LoRA-Ingredients_2067412522302529537.json、视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json、视频生成/文生视频/LTX2.3 In​gredients IC LORA全能参考_2070747298736463873.json、视频生成/文生视频/LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXFloatToInt`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `GetVideoComponents` —— 3/4 个有
- `LTXAddVideoICLoRAGuide` —— 3/4 个有
- `LTXICLoRALoaderModelOnly` —— 3/4 个有
- `LTXVAudioVAELoader` —— 3/4 个有
- `LTXVCropGuides` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `RepeatImageBatch` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `SimpleCalculatorKJ` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `VAELoaderKJ` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ClownSampler_Beta` —— 1/4 个有
- `DualCLIPLoaderGGUF` —— 1/4 个有
- `GemmaAPITextEncode` —— 1/4 个有
- `GuiderParameters` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageBatchMultiple+` —— 1/4 个有
- `ImageConcatFromBatch` —— 1/4 个有
- `Int` —— 1/4 个有
- `LTXVScheduler` —— 1/4 个有
- `MultimodalGuider` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `UnetLoaderGGUFAdvanced` —— 1/4 个有
- `easy positive` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 24 | 24 - 25 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）
