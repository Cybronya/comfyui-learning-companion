---
name: unknown_workflow_video_lora_sampler_31
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.834962
common_nodes: [ApplySageAttention, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, EnhancedLoadDiffusionModel, GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PatchModelPatcherOrder, PreviewImage, PromptRelaySmartEncode, SetNode, Text, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/2065412683087831041.json, 视频生成/图生视频/2056269827312021506.json, 视频生成/图生视频/2059151277300473858.json, 视频生成/图生视频/2059150575673106433.json, 视频生成/图生视频/2059216439994830849.json, 视频生成/图生视频/2059588565125910530.json, 视频生成/图生视频/本地开源免费，漫剧提示词精准控制_2055133052308860930.json, 视频生成/图生视频/2054793002106793985.json, 视频生成/图生视频/2054892353684549633.json, 视频生成/图生视频/2054893808831221761.json, 视频生成/图生视频/2055982648325091329.json, 视频生成/图生视频/2060065758398472194.json, 视频生成/图生视频/2059305059367866370.json, 视频生成/图生视频/2059271969262104577.json, 视频生成/图生视频/2058799333788700673.json, 视频生成/图生视频/2058928699357097985.json, 视频生成/图生视频/本地开源免费，真人运镜长镜头4_2058930471333097473.json, 视频生成/图生视频/2059024762214641665.json, 视频生成/图生视频/2056038240448196610.json, 视频生成/图生视频/2056056568742981634.json, 视频生成/图生视频/2056070807918522370.json, 视频生成/图生视频/2057169759195713538.json, 视频生成/图生视频/漫剧分镜视频3_2058947419932553217.json, 视频生成/图生视频/漫剧分镜视频5_2056626510072729602.json, 视频生成/图生视频/漫剧分镜视频5_2101858170640617474.json, 视频生成/图生视频/漫剧分镜视频5_2102673990207762433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/2065412683087831041.json、视频生成/图生视频/2056269827312021506.json、视频生成/图生视频/2059151277300473858.json、视频生成/图生视频/2059150575673106433.json、视频生成/图生视频/2059216439994830849.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 26 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `EnhancedLoadDiffusionModel`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PreviewImage`
- `PromptRelaySmartEncode`
- `SetNode`
- `Text`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 24/26 个有
- `LoadAudio` —— 22/26 个有
- `easy indexAnything` —— 20/26 个有
- `ImageBatchExtendWithOverlap` —— 19/26 个有
- `easy mathInt` —— 19/26 个有
- `PreviewAny` —— 16/26 个有
- `RegexExtract` —— 16/26 个有
- `StringReplace` —— 16/26 个有
- `Switch` —— 13/26 个有
- `ColorMatchV2` —— 11/26 个有
- `RHLLMChatNode` —— 11/26 个有
- `TextSplitJoinByDelimiter` —— 11/26 个有
- `easy showAnything` —— 11/26 个有
- `FlashVSR_SM_KSampler` —— 10/26 个有
- `FlashVSR_SM_Model` —— 10/26 个有
- `GetImageRangeFromBatch` —— 10/26 个有
- `GetImageSize` —— 10/26 个有
- `TextConcatenate_UTK` —— 8/26 个有
- `BatchThief` —— 6/26 个有
- `RH_Captioner` —— 5/26 个有
- `SaveImage` —— 1/26 个有
- `TT_img_enc` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 26 | 81% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 21 | 100% |
| 采样算法 | 1 | 1 - 2 | 26 | 67% |
| 调度器 | euler | - | 26 | 81% |
| 重绘幅度 | simple | - | 26 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，26 个样本，一致性 81%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，21 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 2，26 个样本
- 调度器 最常用 euler，26 个样本，一致性 81%
- 重绘幅度 最常用 simple，26 个样本，一致性 81%
