---
name: unknown_workflow_video_lora_sampler_697
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.726333
common_nodes: [ImageResizeKJv2, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan21_lynx_人物一致视频_1976007633784147970.json, 视频生成/文生视频/Wan_T2V_14B_lynx(Wrapper) - 使用参考图保持视频角色一致性！_1976302200433545218.json, 视频生成/文生视频/Wan_T2V_lynx+VACE (Wrapper) 面部参考+服装参考+视频动作驱动_1976330086129471490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_697

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan21_lynx_人物一致视频_1976007633784147970.json、视频生成/文生视频/Wan_T2V_14B_lynx(Wrapper) - 使用参考图保持视频角色一致性！_1976302200433545218.json、视频生成/文生视频/Wan_T2V_lynx+VACE (Wrapper) 面部参考+服装参考+视频动作驱动_1976330086129471490.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
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
- `Bounded Image Crop` —— 2/3 个有
- `Bounded Image Crop with Mask` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 2/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 2/3 个有
- `SAMModelLoader (segment anything)` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Image Crop Face` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoVACEEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
