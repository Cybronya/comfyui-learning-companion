---
name: unknown_workflow_upscale_latent_upscale_lora_7
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.9145
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 + VBVR 多图首尾帧_2043983802795560961.json, 视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json, 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json, 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json, 视频生成/文生视频/LTX 2.3 图生视频 2.0｜Dev-Dare 三阶渲染增强版_2051714465686667266.json, 视频生成/文生视频/LTX 2.3 多图首尾帧 2.0｜Dev-Dare 三阶渲染增强版_2051714484946915330.json, 视频生成/文生视频/LTX 2.3 多图首尾帧 2.0｜三阶渲染·极致打磨『最优实现』_2050912405437333506.json, 视频生成/文生视频/LTX 2.3 多图首尾帧高一致性丝滑过渡工作流_2039960294918721537.json, 视频生成/文生视频/LTX 2.3 的 100% 实力释放三阶段采样多图首尾帧工作流_2033913591946027010.json, 视频生成/文生视频/LTX 2.3-1.1 + VBVR 多图首尾帧_2045068937519439873.json, 视频生成/文生视频/LTX-2.3 一分四多图首尾帧 2.0 对比 Distilled+Dev-Dare + VBVR_2051701217973284866.json, 视频生成/文生视频/LTX-2.3 三模对比满编生产套件 2.0｜Distilled + Dev-Dare + VAVR_2051703959529771010.json, 视频生成/文生视频/『最优实现』LTX 2.3 双人对话增强版_2048727968108781570.json, 视频生成/文生视频/『最优实现』四宫格多图首尾帧工作流_2047657296414642177.json, 视频生成/文生视频/一分四多图首尾帧 2.0｜Dev-Dare + VBVR 最终版_2051722692126097409.json, 视频生成/文生视频/一分四多图首尾帧2.0_2050914490237112321.json, 视频生成/文生视频/单双人数字人 2.0｜Dev-Dare + VBVR 最终版_2051722705812111361.json, 视频生成/文生视频/图生视频 2.0｜Dev-Dare + VBVR 最终版_2051722684697989122.json, 视频生成/文生视频/图生视频 2.0｜三阶渲染打磨版，画面质感更强_2050910752227250177.json, 视频生成/文生视频/多图首尾帧 2.0｜Dev-Dare + VBVR 最终版_2051722699306749953.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 + VBVR 多图首尾帧_2043983802795560961.json、视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json、视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json、视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json、视频生成/文生视频/LTX 2.3 图生视频 2.0｜Dev-Dare 三阶渲染增强版_2051714465686667266.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
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
- `VAEDecodeTiled`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 19/20 个有
- `VRAMReserver` —— 19/20 个有
- `LayerUtility: PurgeVRAM V2` —— 18/20 个有
- `PromptRelayEncode` —— 15/20 个有
- `Seed Everywhere` —— 15/20 个有
- `easy showAnything` —— 13/20 个有
- `GetImageSize+` —— 12/20 个有
- `ImageResizeKJv2` —— 12/20 个有
- `JWImageSequenceExtractFromBatch` —— 12/20 个有
- `LTXVAddGuideMulti` —— 12/20 个有
- `PreviewImage` —— 12/20 个有
- `ResizeLongestToNode` —— 12/20 个有
- `VHS_VideoCombine` —— 12/20 个有
- `Int` —— 10/20 个有
- `Text` —— 10/20 个有
- `DisTorchPurgeVRAMV2` —— 8/20 个有
- `Image_Resize_longsize` —— 8/20 个有
- `SaveVideo` —— 8/20 个有
- `ImageCrop+` —— 5/20 个有
- `MathExpression|pysssss` —— 5/20 个有
- `SaveImage` —— 5/20 个有
- `KepStringLiteral` —— 4/20 个有
- `ResizeImageMaskNode` —— 2/20 个有
- `PathchSageAttentionKJ` —— 1/20 个有
- `RH_Translator` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 20 | 100% |
| 高度 | 25 | 25 - 25 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，20 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，20 个样本，取值集中（一致性 100%）
