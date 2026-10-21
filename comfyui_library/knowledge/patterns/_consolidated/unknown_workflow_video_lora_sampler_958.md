---
name: unknown_workflow_video_lora_sampler_958
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.706
common_nodes: [Bounded Image Crop, Bounded Image Crop with Mask, GetImageSizeAndCount, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageResizeKJv2, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, SAMModelLoader (segment anything), SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan_T2V_14B_lynx(Wrapper) - 使用参考图保持视频角色一致性！_1976302200433545218.json, 视频生成/文生视频/Wan_T2V_lynx+VACE (Wrapper) 面部参考+服装参考+视频动作驱动_1976330086129471490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_958

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan_T2V_14B_lynx(Wrapper) - 使用参考图保持视频角色一致性！_1976302200433545218.json、视频生成/文生视频/Wan_T2V_lynx+VACE (Wrapper) 面部参考+服装参考+视频动作驱动_1976330086129471490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `Bounded Image Crop`
- `Bounded Image Crop with Mask`
- `GetImageSizeAndCount`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
