---
name: unknown_workflow_controlnet_video_lora_34
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.896
common_nodes: [Audio Duration (mtb), AudioSeparation, CLIPVisionLoader, DF_Int_to_Float, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DownloadAndLoadWav2VecModel, Florence2Run, Florence2toCoordinates, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MaskBatchMulti, MaskPreview+, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Sam2Segmentation, Text, VHS_DuplicateImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1995300923469705218.json, 视频生成/图生视频/1995137111139528706.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1995300923469705218.json、视频生成/图生视频/1995137111139528706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DF_Int_to_Float`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DownloadAndLoadWav2VecModel`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskBatchMulti`
- `MaskPreview+`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `Sam2Segmentation`
- `Text`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
