---
name: unknown_workflow_video_lora_sampler_96
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.743333
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, ImageBatchExtendWithOverlap, ImageFromBatch+, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, SetNode, Text, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [图片生成/图生图/修仙-漫剧图生视频优化版_2014595984575176706.json, 视频生成/图生视频/水池高清特效_2014865724992393217.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027295499975397377.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027312644432076802.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027802000825524225.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027917338749706242.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027920287546740737.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027921761626492930.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028112885385269249.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028125555844976641.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028393492883443713.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028664634638606338.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028827198974595073.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028846638088851458.json, 视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2028859143251038209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/修仙-漫剧图生视频优化版_2014595984575176706.json、视频生成/图生视频/水池高清特效_2014865724992393217.json、视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027295499975397377.json、视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027312644432076802.json、视频生成/图生视频/漫剧分镜视频 Real AI video リアルAIビデオ_2027802000825524225.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageFromBatch+`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `SetNode`
- `Text`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `JDCN_StringToList` —— 13/15 个有
- `JWInteger` —— 13/15 个有
- `easy indexAnything` —— 13/15 个有
- `ImageConcatMulti` —— 2/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `Int` —— 2/15 个有
- `LoadVQVAE` —— 2/15 个有
- `RH_Captioner` —— 2/15 个有
- `RunningHub Deepcleaner` —— 2/15 个有
- `TextConcatenate_UTK` —— 2/15 个有
- `easy showAnything` —— 2/15 个有
- `Load Cache` —— 1/15 个有
- `Load Lora` —— 1/15 个有
- `LoadDust3r` —— 1/15 个有
- `Ruyi_LoadLora` —— 1/15 个有
- `[Comfy3D] Load 3DGS` —— 1/15 个有
- `load_FLUX` —— 1/15 个有
- `load_SD35` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 15 | 100% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，15 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
