---
name: unknown_workflow_video_lora_sampler_428
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.767143
common_nodes: [CR Text, GetImageSizeAndCount, ImageFromBatch+, ImageResizeKJ, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, Text Concatenate, VHS_LoadVideo, VHS_VideoCombine, Wan22PromptSelector, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354.json, 平台全量/Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794.json, 平台全量/姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425.json, 视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json, 视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json, 视频生成/图生视频/完美参考人脸lynx加VACE精准姿势迁移_1977047772987838465.json, 视频生成/图生视频/顶配视频换脸lynx+VACE完美一致性_1977047808907857921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_428

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354.json、平台全量/Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794.json、平台全量/姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425.json、视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json、视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Text`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
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
- `GetNode` —— 6/7 个有
- `ImpactSwitch` —— 6/7 个有
- `RH_LLMAPI_NODE` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `AIO_Preprocessor` —— 4/7 个有
- `DrawMaskOnImage` —— 4/7 个有
- `GrowMask` —— 4/7 个有
- `SeCModelLoader` —— 4/7 个有
- `SeCVideoSegmentation` —— 4/7 个有
- `BlockifyMask` —— 3/7 个有
- `DepthAnything_V2` —— 3/7 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/7 个有
- `ImageFromBatch` —— 3/7 个有
- `LayerMask: LoadSegmentAnythingModels` —— 3/7 个有
- `LayerMask: SegmentAnythingUltra V3` —— 3/7 个有
- `MaskPreview+` —— 3/7 个有
- `PointsEditor` —— 2/7 个有
- `Image Crop Face` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy imageColorMatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
