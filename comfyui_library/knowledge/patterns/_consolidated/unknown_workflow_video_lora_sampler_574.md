---
name: unknown_workflow_video_lora_sampler_574
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78525
common_nodes: [CR Text, GetImageSizeAndCount, ImageFromBatch+, ImageResizeKJ, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, RH_LLMAPI_NODE, Text Concatenate, VHS_LoadVideo, VHS_VideoCombine, Wan22PromptSelector, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json, 视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json, 视频生成/图生视频/完美参考人脸lynx加VACE精准姿势迁移_1977047772987838465.json, 视频生成/图生视频/顶配视频换脸lynx+VACE完美一致性_1977047808907857921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_574

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json、视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json、视频生成/图生视频/完美参考人脸lynx加VACE精准姿势迁移_1977047772987838465.json、视频生成/图生视频/顶配视频换脸lynx+VACE完美一致性_1977047808907857921.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `BlockifyMask` —— 2/4 个有
- `DepthAnything_V2` —— 2/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/4 个有
- `DrawMaskOnImage` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `SeCModelLoader` —— 2/4 个有
- `SeCVideoSegmentation` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
