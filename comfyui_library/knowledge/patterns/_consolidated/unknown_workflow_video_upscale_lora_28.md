---
name: unknown_workflow_video_upscale_lora_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.864
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, HfImageToRGB, ImageResizeKJ, ImageResizeKJv2, ImageUpscaleWithModelBatched, ImpactSwitch, IntegerInput, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, ToInt, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy anythingInversedSwitch, easy int, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/智能口播-高清版-输入修复-像素修复_2054047934005694466.json, 数字人/数字人/智能口播-高清版-输入修复_2001479088147660801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/智能口播-高清版-输入修复-像素修复_2054047934005694466.json、数字人/数字人/智能口播-高清版-输入修复_2001479088147660801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `HfImageToRGB`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImageUpscaleWithModelBatched`
- `ImpactSwitch`
- `IntegerInput`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `ToInt`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy anythingInversedSwitch`
- `easy int`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
