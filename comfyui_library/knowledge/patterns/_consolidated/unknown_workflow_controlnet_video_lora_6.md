---
name: unknown_workflow_controlnet_video_lora_6
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.961364
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Primitive integer [Crystools], RH_Captioner, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/KTV歌后音乐生成器1.0_1967011405411049474.json, 视频生成/图生视频/KTV歌后音乐生成器_腾讯音乐+MultiTalk_1936420652008001537.json, 视频生成/图生视频/MultiTalk 唱歌数字人｜KJ加速版_1936694256662908929.json, 视频生成/图生视频/MultiTalk-动态数字人天花板 单图KJ版-StarAI_1936454016199200770.json, 视频生成/图生视频/全民K唱歌数字人_1957465245520424961.json, 视频生成/图生视频/可带运镜唱歌或口播数字人-VIP顶配版_2026920518938529794.json, 视频生成/图生视频/可带运镜唱歌或口播数字人-VIP顶配版_2052624667902525442.json, 视频生成/图生视频/图生视频 -K唱歌数字人KJ加速版-顶流MultiTalk_2031551827505844225.json, 视频生成/图生视频/图生视频 全民K唱歌数字人KJ加速版-顶流MultiTalk_2029395948555735041.json, 视频生成/图生视频/图生视频 全民K唱歌数字人KJ加速版-顶流MultiTalk_2030446247387074561.json, 视频生成/图生视频/超顶MultiTalk动态K歌数字人--KJ量化极速版_1936293743358038017.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/KTV歌后音乐生成器1.0_1967011405411049474.json、视频生成/图生视频/KTV歌后音乐生成器_腾讯音乐+MultiTalk_1936420652008001537.json、视频生成/图生视频/MultiTalk 唱歌数字人｜KJ加速版_1936694256662908929.json、视频生成/图生视频/MultiTalk-动态数字人天花板 单图KJ版-StarAI_1936454016199200770.json、视频生成/图生视频/全民K唱歌数字人_1957465245520424961.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `Text Concatenate`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 10/11 个有
- `VHS_DuplicateImages` —— 10/11 个有
- `CreateCFGScheduleFloatList` —— 9/11 个有
- `LoadAudio` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `GetTextFromJson` —— 2/11 个有
- `LoadJsonFromText` —— 2/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `RandomInt` —— 2/11 个有
- `ReplaceText` —— 2/11 个有
- `Save Text File` —— 2/11 个有
- `ShowText` —— 2/11 个有
- `SongGeneration_Sampler` —— 2/11 个有
- `SongGeneration_Stage1` —— 2/11 个有
- `SongGeneration_Stage2` —— 2/11 个有
- `StringReplace` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `easy clearCacheAll` —— 2/11 个有
- `ImageUpscaleWithModel` —— 1/11 个有
- `ImpactSwitch` —— 1/11 个有
- `Int` —— 1/11 个有
- `UpscaleModelLoader` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
