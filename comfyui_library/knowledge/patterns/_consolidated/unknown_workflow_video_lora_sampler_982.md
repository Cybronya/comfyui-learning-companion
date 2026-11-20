---
name: unknown_workflow_video_lora_sampler_982
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9525
common_nodes: [CR Image Input Switch, ColorMatch, DWPreprocessor, DownloadAndLoadWav2VecModel, ImageConcatenate_UTK, ImageMaskScaleAs_UTK, ImageScaleByAspectRatio_UTK, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, TextBoxNode_UTK, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy imagePixelPerfect]
problems: []
missing: []
members: [平台全量/Wan21_终极视频转绘单人_1966429249773219841.json, 平台全量/Wan21_终极视频转绘多人_1966443899713695746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_982

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Wan21_终极视频转绘单人_1966429249773219841.json、平台全量/Wan21_终极视频转绘多人_1966443899713695746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Image Input Switch`
- `ColorMatch`
- `DWPreprocessor`
- `DownloadAndLoadWav2VecModel`
- `ImageConcatenate_UTK`
- `ImageMaskScaleAs_UTK`
- `ImageScaleByAspectRatio_UTK`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `TextBoxNode_UTK`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy imagePixelPerfect`

**可变部分**（部分 workflow 才有）：
- `AudioCropProcessUTK` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `Constant Number` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `MathExpression_UTK` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有
- `SeparateMasks` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `WanVideoApplyNAG` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
