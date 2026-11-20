---
name: unknown_workflow_video_upscale_latent_upscale_4
type: Unknown Workflow
frequency: 27
level: strong
coverage: 0.630778
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, UNETLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/LTX-2.5_ICLoRA_Union_Control（3采）V1-cc-1_2105578432393469954.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control_2064300604129898497.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control（2采）_2064316689243791362.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control（3采）V2_2068963265690034177.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control（3采）_2064318009904287745.json, 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_2047700964789981186.json, 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2-镜头迁移_2074096652201320450.json, 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2-镜头迁移_2074111504655405057.json, 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2_2072497688859471874.json, 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2_2075049953608687617.json, 视频生成/图生视频/LTX-2.3_动作参考并保持脸部一致性_2048694979278671873.json, 视频生成/图生视频/LTX2.3动作迁移  数字人 动作模仿+图片跳舞  极速图生视频 虚拟美女模特 数字人对话_2048935364718501889.json, 视频生成/图生视频/LTX2.3动作迁移  数字人 动作模仿+图片跳舞 极速图生视频  工作流 V1.0_2051190166873755649.json, 视频生成/图生视频/LTX2.3动作迁移模仿+极速图生视频+数字人+动作模仿+图片跳舞+虚拟美女模特+数字人对话唱歌_2058717709986263041.json, 视频生成/图生视频/LTX2.3数字人 动作模仿+图片跳舞+动作迁移 极速图生视频 虚拟美女模特 数字人对话_2048925401644273665.json, 视频生成/图生视频/Ltx2.3 抖音短视频清洗 动作90%迁移_2082866580660252674.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移! B站艾橘溪_2048751560372523009.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞 动作复刻_2079154920137248770.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞 复刻跳舞动作_2069007016567336961.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞 复刻跳舞动作_2082805573707456514.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625.json, 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞工作流_2049052727711375361.json, 视频生成/图生视频/模特动作迁移模仿 LTX2.3极速图生视频+数字人+动作模仿+图片跳舞 虚拟美女+数字人对话_2056200505206026241.json, 视频生成/图生视频/（1图1视频 动作模仿只需要上传图片和视频）Ltx2.3 抖音短视频清洗 动作90%迁移_2111328483942158338.json, 视频生成/文生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_controlnet_2047612025181835265.json, 视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json, 视频生成/文生视频/LTX2.3动作迁移模仿 极速图生视频+数字人+动作模仿+图片跳舞 虚拟美女模特+数字人对话_2056190819454988290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（平台全量/LTX-2.5_ICLoRA_Union_Control（3采）V1-cc-1_2105578432393469954.json、视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control_2064300604129898497.json、视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control（2采）_2064316689243791362.json、视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control（3采）V2_2068963265690034177.json、视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control（3采）_2064318009904287745.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 27 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 25/27 个有
- `VAELoaderKJ` —— 25/27 个有
- `DWPreprocessor` —— 22/27 个有
- `LTXVImgToVideoInplace` —— 22/27 个有
- `LTXVLatentUpsampler` —— 22/27 个有
- `PrimitiveBoolean` —— 21/27 个有
- `VAEDecodeTiled` —— 21/27 个有
- `ComfyMathExpression` —— 17/27 个有
- `RTXVideoSuperResolution` —— 17/27 个有
- `JjkText` —— 14/27 个有
- `LayerUtility: PurgeVRAM` —— 14/27 个有
- `LTXVAudioVAEDecode` —— 13/27 个有
- `CannyEdgePreprocessor` —— 8/27 个有
- `DepthAnythingPreprocessor` —— 8/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/27 个有
- `Text` —— 6/27 个有
- `VAEDecode` —— 6/27 个有
- `LTXVPreprocess` —— 5/27 个有
- `MathExpression|pysssss` —— 5/27 个有
- `CLIPLoader` —— 2/27 个有
- `LoraLoaderModelOnly` —— 2/27 个有
- `VAELoader` —— 2/27 个有
- `Label (rgthree)` —— 1/27 个有
- `LowVRAMCheckpointLoader` —— 1/27 个有
- `PreviewAny` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 27 | 100% |
| 高度 | 25 | 25 - 25 | 27 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，27 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，27 个样本，取值集中（一致性 100%）
