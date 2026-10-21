---
name: text_to_image_video_lora_sampler_95
type: Text To Image
frequency: 8
level: strong
coverage: 0.69025
common_nodes: [Any Switch (rgthree), Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, EmptyLatentImage, Fast Groups Muter (rgthree), FlashVSRNode, Float to Int, GetNode, INTConstant, ImageResizeKJv2, JjkText, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, MultiTalkWav2VecEmbeds, RHHiddenNodes, RH_Captioner, RH_GetAudioDuration, RH_LLMAPI_Pro_Node, RIFEInterpolation, SaveAudio, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoContextOptions, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy boolean, easy cleanGpuUsed, easy clearCacheAll, easy ifElse, easy imageSize, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan 2.2提示词丝滑运镜高动态MV图生视频处理工具_2101374439895162882.json, 视频生成/图生视频/Wan2.2丝滑运镜MV工作流｜高动态提示词视频生成_2097804026267131906.json, 视频生成/图生视频/wan 2.2提示词丝滑运镜｜高动态MV数字人图生视频_2092003605388808194.json, 视频生成/图生视频/wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233.json, 视频生成/图生视频/丝滑运镜高动态MV｜wan 2.2提示词驱动图生视频直出_2089548883880923138.json, 视频生成/图生视频/提示词丝滑运镜高动态｜wan 2.2数字人MV制作_2101203802224418818.json, 视频生成/图生视频/高动态MV运镜｜wan 2.2自动提示词丝滑图生视频数字人_2092134052450095105.json, 视频生成/图生视频/高动态提示词丝滑运镜2.2wan数字人图生视频新奇创意_2087306443576930306.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2提示词丝滑运镜高动态MV图生视频处理工具_2101374439895162882.json、视频生成/图生视频/Wan2.2丝滑运镜MV工作流｜高动态提示词视频生成_2097804026267131906.json、视频生成/图生视频/wan 2.2提示词丝滑运镜｜高动态MV数字人图生视频_2092003605388808194.json、视频生成/图生视频/wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233.json、视频生成/图生视频/丝滑运镜高动态MV｜wan 2.2提示词驱动图生视频直出_2089548883880923138.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`
- `Float to Int`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_GetAudioDuration`
- `RH_LLMAPI_Pro_Node`
- `RIFEInterpolation`
- `SaveAudio`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy ifElse`
- `easy imageSize`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
