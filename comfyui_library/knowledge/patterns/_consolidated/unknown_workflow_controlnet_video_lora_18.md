---
name: unknown_workflow_controlnet_video_lora_18
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.5195
common_nodes: [Any Switch (rgthree), Audio Cut (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoVAELoader, easy int, easy positive, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1938467765139496961.json, 视频生成/图生视频/2020045552515289089.json, 视频生成/图生视频/1937584753665032193.json, 视频生成/文生视频/语音驱动图片说话数字人工作流_1988165359964438530.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_18

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1938467765139496961.json、视频生成/图生视频/2020045552515289089.json、视频生成/图生视频/1937584753665032193.json、视频生成/文生视频/语音驱动图片说话数字人工作流_1988165359964438530.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Cut (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `PrimitiveString` —— 3/4 个有
- `StringConcatenate` —— 3/4 个有
- `VHS_DuplicateImages` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `WanVideoUni3C_embeds` —— 3/4 个有
- `WanVideoVRAMManagement` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `Bookmark (rgthree)` —— 2/4 个有
- `GoogleTranslateTextNode` —— 2/4 个有
- `Mute / Bypass Relay (rgthree)` —— 2/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `WanVideoContextOptions` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
