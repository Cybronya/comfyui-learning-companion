---
name: unknown_workflow_lora_sampler_clip_14
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.6503
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VHS_LoadVideo, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_ICLoRA_crossview_2076951479637864450.json, 视频生成/图生视频/LTX-2.3_ICLoRA_outpaint_2044337798932598786.json, 视频生成/图生视频/LTX2.3动作迁移  数字人 动作模仿+图片跳舞  极速图生视频 虚拟美女模特 数字人对话_2048935364718501889.json, 视频生成/图生视频/LTX2.3动作迁移  数字人 动作模仿+图片跳舞 极速图生视频  工作流 V1.0_2051190166873755649.json, 视频生成/图生视频/LTX2.3动作迁移模仿+极速图生视频+数字人+动作模仿+图片跳舞+虚拟美女模特+数字人对话唱歌_2058717709986263041.json, 视频生成/图生视频/LTX2.3数字人 动作模仿+图片跳舞+动作迁移 极速图生视频 虚拟美女模特 数字人对话_2048925401644273665.json, 视频生成/图生视频/LTXIC视频生成 二次元_2079022514478608385.json, 视频生成/图生视频/Ltx2.3 抖音短视频清洗 动作90%迁移_2082866580660252674.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移! B站艾橘溪_2048751560372523009.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞 动作复刻_2079154920137248770.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞 复刻跳舞动作_2069007016567336961.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞 复刻跳舞动作_2082805573707456514.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞工作流_2049052727711375361.json, 视频生成/图生视频/模特动作迁移模仿 LTX2.3极速图生视频+数字人+动作模仿+图片跳舞 虚拟美女+数字人对话_2056200505206026241.json, 视频生成/图生视频/（1图1视频 动作模仿只需要上传图片和视频）Ltx2.3 抖音短视频清洗 动作90%迁移_2111328483942158338.json, 视频生成/文生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_2033749447833821185.json, 视频生成/文生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_controlnet_2047612025181835265.json, 视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json, 视频生成/文生视频/LTX2.3动作迁移模仿 极速图生视频+数字人+动作模仿+图片跳舞 虚拟美女模特+数字人对话_2056190819454988290.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_ICLoRA_crossview_2076951479637864450.json、视频生成/图生视频/LTX-2.3_ICLoRA_outpaint_2044337798932598786.json、视频生成/图生视频/LTX2.3动作迁移  数字人 动作模仿+图片跳舞  极速图生视频 虚拟美女模特 数字人对话_2048935364718501889.json、视频生成/图生视频/LTX2.3动作迁移  数字人 动作模仿+图片跳舞 极速图生视频  工作流 V1.0_2051190166873755649.json、视频生成/图生视频/LTX2.3动作迁移模仿+极速图生视频+数字人+动作模仿+图片跳舞+虚拟美女模特+数字人对话唱歌_2058717709986263041.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 19/20 个有
- `ImageResizeKJv2` —— 19/20 个有
- `VAEDecodeTiled` —— 19/20 个有
- `VAELoaderKJ` —— 19/20 个有
- `VHS_VideoCombine` —— 19/20 个有
- `GetNode` —— 18/20 个有
- `INTConstant` —— 18/20 个有
- `LTXVImgToVideoConditionOnly` —— 18/20 个有
- `LatentUpscaleModelLoader` —— 18/20 个有
- `LoadImage` —— 18/20 个有
- `SetNode` —— 18/20 个有
- `DWPreprocessor` —— 17/20 个有
- `PrimitiveBoolean` —— 17/20 个有
- `LTXVImgToVideoInplace` —— 16/20 个有
- `LTXVLatentUpsampler` —— 16/20 个有
- `ComfyMathExpression` —— 15/20 个有
- `RTXVideoSuperResolution` —— 15/20 个有
- `JjkText` —— 14/20 个有
- `LayerUtility: PurgeVRAM` —— 14/20 个有
- `LTXVAudioVAEDecode` —— 6/20 个有
- `CannyEdgePreprocessor` —— 3/20 个有
- `DepthAnythingPreprocessor` —— 3/20 个有
- `LTXTiledSampler` —— 2/20 个有
- `LTXVLatentUpsamplerTiled` —— 2/20 个有
- `LTXVPreprocess` —— 2/20 个有
- `ResizeImageMaskNode` —— 2/20 个有
- `CLIPLoader` —— 1/20 个有
- `CreateVideo` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `MathExpression|pysssss` —— 1/20 个有
- `PreviewAny` —— 1/20 个有
- `SaveVideo` —— 1/20 个有
- `Text` —— 1/20 个有
- `TextGenerateLTX2Prompt` —— 1/20 个有
- `VAEDecode` —— 1/20 个有
- `VAELoader` —— 1/20 个有

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
