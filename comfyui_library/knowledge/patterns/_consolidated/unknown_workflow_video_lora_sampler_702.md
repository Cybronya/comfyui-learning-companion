---
name: unknown_workflow_video_lora_sampler_702
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5795
common_nodes: [AddLabel, Any Switch (rgthree), Bookmark (rgthree), EmptyImage, Fast Groups Muter (rgthree), GetImageRangeFromBatch, GetImageSize+, GetImageSizeAndCount, GetNode, GoogleTranslateTextNode, ImageConcatMulti, ImagePadKJ, JoinStrings, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskPreview+, MiniCPM_VQA_Polished, SetNode, String Literal, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Wan Vace 14B  视频扩图工作流_1923647335333548033.json, 视频生成/图生视频/Wan Vace 14B  扩充电影镜头_1923521881121746946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_702

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Wan Vace 14B  视频扩图工作流_1923647335333548033.json、视频生成/图生视频/Wan Vace 14B  扩充电影镜头_1923521881121746946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `EmptyImage`
- `Fast Groups Muter (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GoogleTranslateTextNode`
- `ImageConcatMulti`
- `ImagePadKJ`
- `JoinStrings`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `MiniCPM_VQA_Polished`
- `SetNode`
- `String Literal`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
