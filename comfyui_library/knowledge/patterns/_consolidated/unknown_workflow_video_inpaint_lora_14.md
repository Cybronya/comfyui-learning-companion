---
name: unknown_workflow_video_inpaint_lora_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5575
common_nodes: [Any Switch (rgthree), ApplyFaceProcessor, DWPreprocessor, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, FaceProcessorLoader, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, INPAINT_MaskedFill, ImageResizeKJ, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PreviewImage, PrimitiveString, PrimitiveStringMultiline, RMBG, SetNode, StringConcatenate, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy int, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/姿态+深度+遮罩视频三合一Stand-IN加vace控制 人物一致性_1959568027425648642.json, 视频生成/文生视频/Stand-IN 脸部一致性+视频换脸动作模仿_1959234838102487041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/姿态+深度+遮罩视频三合一Stand-IN加vace控制 人物一致性_1959568027425648642.json、视频生成/文生视频/Stand-IN 脸部一致性+视频换脸动作模仿_1959234838102487041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ApplyFaceProcessor`
- `DWPreprocessor`
- `DeepTranslatorTextNode`
- `DepthAnythingV2Preprocessor`
- `FaceProcessorLoader`
- `Fast Groups Muter (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `INPAINT_MaskedFill`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RMBG`
- `SetNode`
- `StringConcatenate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
