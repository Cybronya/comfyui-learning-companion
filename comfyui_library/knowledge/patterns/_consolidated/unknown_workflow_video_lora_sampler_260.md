---
name: unknown_workflow_video_lora_sampler_260
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.4413
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyAudio, GetImageSize, ImageConcanate, ImageScaleBy, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/LTX 2.3 视频编辑｜写提示词编辑视频（修改、添加、替换、转换风格）_2046581374215266306.json, 平台全量/LTX-2.3 ReFocus视频细节增强_2047278494165508097.json, 平台全量/LTX2.3 V2V EditAnything视频编辑-高级工作流_2046264739034046466.json, 平台全量/LTX2.3 real2anime真实视频转动画风格_2046258155289583617.json, 平台全量/LTX2.3 一句话视频编辑edit_anything_2046271174505664513.json, 平台全量/LTX2.3视频编辑工作流_2052005121772531713.json, 平台全量/LTX2.3视频编辑（字幕去除）工作流_2053386058578051074.json, 平台全量/豆包视频 - 除水印_2053408442727059457.json, 数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json, 视频生成/图生视频/豆包视频 - 除水印_2056637158571732994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_260

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/LTX 2.3 视频编辑｜写提示词编辑视频（修改、添加、替换、转换风格）_2046581374215266306.json、平台全量/LTX-2.3 ReFocus视频细节增强_2047278494165508097.json、平台全量/LTX2.3 V2V EditAnything视频编辑-高级工作流_2046264739034046466.json、平台全量/LTX2.3 real2anime真实视频转动画风格_2046258155289583617.json、平台全量/LTX2.3 一句话视频编辑edit_anything_2046271174505664513.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyAudio`
- `GetImageSize`
- `ImageConcanate`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/10 个有
- `LTXVAddGuide` —— 9/10 个有
- `LatentUpscaleModelLoader` —— 9/10 个有
- `RecordAudio` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `easy convertAnything` —— 9/10 个有
- `APGGuider` —— 8/10 个有
- `Textbox` —— 6/10 个有
- `CLIPLoader` —— 5/10 个有
- `GetImageRangeFromBatch` —— 5/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `Label (rgthree)` —— 5/10 个有
- `ShowText|pysssss` —— 5/10 个有
- `StringConcatenate` —— 5/10 个有
- `TextGenerate` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `LTXVAddGuideMulti` —— 4/10 个有
- `SaveVideo` —— 4/10 个有
- `UnetLoaderGGUF` —— 4/10 个有
- `CM_IntToNumber` —— 1/10 个有
- `LTXVAudioVAEDecode` —— 1/10 个有
- `Number to String` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 24 | 24 - 24 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，10 个样本，取值集中（一致性 100%）
