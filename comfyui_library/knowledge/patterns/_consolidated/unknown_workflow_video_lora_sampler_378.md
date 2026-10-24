---
name: unknown_workflow_video_lora_sampler_378
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7975
common_nodes: [GetImageSizeAndCount, INTConstant, ImageResizeKJ, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, RH_Captioner, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/lynx-VACE-ID一致性图生视频_1975850238516793345.json, 视频生成/文生视频/lynx-VACE-ID一致性图生视频（独立垫图）_1975858725598662658.json, 视频生成/文生视频/lynx-VACE-ID一致性首尾帧_1975861201806692353.json, 视频生成/文生视频/lynx-VACE-ID双一致性姿态视频引导视频生成_1975863056892866561.json, 视频生成/文生视频/lynx-VACE-ID双一致性文生视频_1975862492029169665.json, 视频生成/文生视频/lynx-VACE-ID换脸后图生视频_1975861887592214529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_378

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/lynx-VACE-ID一致性图生视频_1975850238516793345.json、视频生成/文生视频/lynx-VACE-ID一致性图生视频（独立垫图）_1975858725598662658.json、视频生成/文生视频/lynx-VACE-ID一致性首尾帧_1975861201806692353.json、视频生成/文生视频/lynx-VACE-ID双一致性姿态视频引导视频生成_1975863056892866561.json、视频生成/文生视频/lynx-VACE-ID双一致性文生视频_1975862492029169665.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJ`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `RH_Captioner`
- `VHS_VideoCombine`
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
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoEmptyEmbeds` —— 4/6 个有
- `GetImageSize` —— 2/6 个有
- `Image Blank` —— 2/6 个有
- `ImageCompositeMasked` —— 2/6 个有
- `LayerMask: LoadFlorence2Model` —— 2/6 个有
- `LayerMask: ObjectDetectorFL2` —— 2/6 个有
- `LayerMask: SAM2Ultra` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `MaskToImage` —— 2/6 个有
- `SolidMask` —— 2/6 个有
- `DWPreprocessor` —— 1/6 个有
- `GPENO Face Restoration` —— 1/6 个有
- `ReActorFaceSwap` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
