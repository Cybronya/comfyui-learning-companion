---
name: text_to_image_lora_sampler_clip_248
type: Text To Image
frequency: 3
level: strong
coverage: 0.939333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, DWPreprocessor, EmptyLTXVLatentVideo, EmptyLatentImage, GemmaAPITextEncode, GetImageSize, GetVideoComponents, ImageScale, ImageToMask, JjkText, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDilateVideoMask, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLaplacianPyramidBlend, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, MaskToImage, PrimitiveBoolean, PrimitiveString, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282.json, 视频生成/图生视频/人物动作迁移视频LTX2.3图生视频工作流_2088387000385761281.json, 视频生成/图生视频/人物动作迁移视频｜LTX2.3图生视频工作流_2088357506513985538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_248

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282.json、视频生成/图生视频/人物动作迁移视频LTX2.3图生视频工作流_2088387000385761281.json、视频生成/图生视频/人物动作迁移视频｜LTX2.3图生视频工作流_2088357506513985538.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `DWPreprocessor`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GemmaAPITextEncode`
- `GetImageSize`
- `GetVideoComponents`
- `ImageScale`
- `ImageToMask`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVDilateVideoMask`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLaplacianPyramidBlend`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskToImage`
- `PrimitiveBoolean`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
