---
name: unknown_workflow_controlnet_video_lora_5
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.899154
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Primitive integer [Crystools], SaveAudio, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1945316434345959426.json, 视频生成/图生视频/1937138982268379137.json, 视频生成/图生视频/1936094319805648897.json, 视频生成/图生视频/2015642745657892866.json, 视频生成/图生视频/1967011405411049474.json, 视频生成/图生视频/KTV歌后音乐生成器_腾讯音乐+MultiTalk_1936420652008001537.json, 视频生成/图生视频/1957465245520424961.json, 视频生成/图生视频/2026920518938529794.json, 视频生成/图生视频/2052624667902525442.json, 视频生成/图生视频/2031551827505844225.json, 视频生成/图生视频/2029395948555735041.json, 视频生成/图生视频/2030446247387074561.json, 视频生成/图生视频/1996612956362260482.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1945316434345959426.json、视频生成/图生视频/1937138982268379137.json、视频生成/图生视频/1936094319805648897.json、视频生成/图生视频/2015642745657892866.json、视频生成/图生视频/1967011405411049474.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `Primitive integer [Crystools]`
- `SaveAudio`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 12/13 个有
- `easy showAnything` —— 12/13 个有
- `LoadAudio` —— 11/13 个有
- `CreateCFGScheduleFloatList` —— 10/13 个有
- `RH_Captioner` —— 10/13 个有
- `Text Concatenate` —— 10/13 个有
- `VHS_DuplicateImages` —— 10/13 个有
- `Audio Cut (mtb)` —— 2/13 个有
- `ColorMatch` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `GetNode` —— 2/13 个有
- `GetTextFromJson` —— 2/13 个有
- `LoadJsonFromText` —— 2/13 个有
- `RHHiddenNodes` —— 2/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `RandomInt` —— 2/13 个有
- `ReplaceText` —— 2/13 个有
- `Save Text File` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `ShowText` —— 2/13 个有
- `SongGeneration_Sampler` —— 2/13 个有
- `SongGeneration_Stage1` —— 2/13 个有
- `SongGeneration_Stage2` —— 2/13 个有
- `StringReplace` —— 2/13 个有
- `easy anythingIndexSwitch` —— 2/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
