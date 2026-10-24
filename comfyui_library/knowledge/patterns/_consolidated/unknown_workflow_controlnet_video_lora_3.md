---
name: unknown_workflow_controlnet_video_lora_3
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.910867
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Multitalk数字人图片唱歌（kj加速升级版）_1937093293593251841.json, 图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json, 视频生成/图生视频/25到29秒长视频唱歌_1945316434345959426.json, 视频生成/图生视频/Ai女友唱歌对口型=Multitalk=艾橘溪_1937138982268379137.json, 视频生成/图生视频/KJ加速版-顶流MultiTalk全民K唱歌数字人_1936094319805648897.json, 视频生成/图生视频/KJ加速版-顶流MultiTalk全民K唱歌数字人：智能AI唱歌软件工作流_2015642745657892866.json, 视频生成/图生视频/KTV歌后音乐生成器1.0_1967011405411049474.json, 视频生成/图生视频/KTV歌后音乐生成器_腾讯音乐+MultiTalk_1936420652008001537.json, 视频生成/图生视频/全民K唱歌数字人_1957465245520424961.json, 视频生成/图生视频/可带运镜唱歌或口播数字人-VIP顶配版_2026920518938529794.json, 视频生成/图生视频/可带运镜唱歌或口播数字人-VIP顶配版_2052624667902525442.json, 视频生成/图生视频/图生视频 -K唱歌数字人KJ加速版-顶流MultiTalk_2031551827505844225.json, 视频生成/图生视频/图生视频 全民K唱歌数字人KJ加速版-顶流MultiTalk_2029395948555735041.json, 视频生成/图生视频/图生视频 全民K唱歌数字人KJ加速版-顶流MultiTalk_2030446247387074561.json, 视频生成/图生视频/图生高清唱歌视频--25到29秒长视频唱歌_1996612956362260482.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_3

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Multitalk数字人图片唱歌（kj加速升级版）_1937093293593251841.json、图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json、视频生成/图生视频/25到29秒长视频唱歌_1945316434345959426.json、视频生成/图生视频/Ai女友唱歌对口型=Multitalk=艾橘溪_1937138982268379137.json、视频生成/图生视频/KJ加速版-顶流MultiTalk全民K唱歌数字人_1936094319805648897.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `INTConstant` —— 14/15 个有
- `MathExpression|pysssss` —— 14/15 个有
- `Primitive integer [Crystools]` —— 14/15 个有
- `SaveAudio` —— 14/15 个有
- `Text Multiline` —— 14/15 个有
- `VHS_LoadVideo` —— 14/15 个有
- `LoadAudio` —— 13/15 个有
- `easy showAnything` —— 13/15 个有
- `CreateCFGScheduleFloatList` —— 12/15 个有
- `VHS_DuplicateImages` —— 12/15 个有
- `RH_Captioner` —— 11/15 个有
- `Text Concatenate` —— 11/15 个有
- `Audio Cut (mtb)` —— 2/15 个有
- `ColorMatch` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `GetNode` —— 2/15 个有
- `GetTextFromJson` —— 2/15 个有
- `LoadJsonFromText` —— 2/15 个有
- `RHHiddenNodes` —— 2/15 个有
- `RH_LLMAPI_NODE` —— 2/15 个有
- `RandomInt` —— 2/15 个有
- `ReplaceText` —— 2/15 个有
- `Save Text File` —— 2/15 个有
- `SetNode` —— 2/15 个有
- `ShowText` —— 2/15 个有
- `SongGeneration_Sampler` —— 2/15 个有
- `SongGeneration_Stage1` —— 2/15 个有
- `SongGeneration_Stage2` —— 2/15 个有
- `StringReplace` —— 2/15 个有
- `easy anythingIndexSwitch` —— 2/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
