---
name: unknown_workflow_controlnet_video_lora_7
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.871923
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Multitalk数字人图片唱歌（kj加速升级版）_1937093293593251841.json, 图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json, 平台全量/【宠物说话视频制作指南】MultiTalk完美对口型，lightx2v加速生成视频_1937185690939768833.json, 数字人/数字人/MultiTalk-最强数字人_1936721152276353025.json, 数字人/数字人/MultiTalk数字人·K歌极速版-阿浩_2027218966384484354.json, 视频生成/图生视频/25到29秒长视频唱歌_1945316434345959426.json, 视频生成/图生视频/Ai女友唱歌对口型=Multitalk=艾橘溪_1937138982268379137.json, 视频生成/图生视频/KJ加速版-顶流MultiTalk全民K唱歌数字人_1936094319805648897.json, 视频生成/图生视频/KJ加速版-顶流MultiTalk全民K唱歌数字人：智能AI唱歌软件工作流_2015642745657892866.json, 视频生成/图生视频/MultiTalk 唱歌数字人｜KJ加速版_1936694256662908929.json, 视频生成/图生视频/MultiTalk-动态数字人天花板 单图KJ版-StarAI_1936454016199200770.json, 视频生成/图生视频/Multitalk万能数字人- 真人-卡通- 动物--生成超长视频_1939669350049878017.json, 视频生成/图生视频/图生高清唱歌视频--25到29秒长视频唱歌_1996612956362260482.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_7

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Multitalk数字人图片唱歌（kj加速升级版）_1937093293593251841.json、图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json、平台全量/【宠物说话视频制作指南】MultiTalk完美对口型，lightx2v加速生成视频_1937185690939768833.json、数字人/数字人/MultiTalk-最强数字人_1936721152276353025.json、数字人/数字人/MultiTalk数字人·K歌极速版-阿浩_2027218966384484354.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
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
- `AudioCrop` —— 12/13 个有
- `MathExpression|pysssss` —— 12/13 个有
- `INTConstant` —— 11/13 个有
- `Text Multiline` —— 11/13 个有
- `VHS_LoadVideo` —— 11/13 个有
- `Primitive integer [Crystools]` —— 10/13 个有
- `easy showAnything` —— 10/13 个有
- `SaveAudio` —— 9/13 个有
- `VHS_DuplicateImages` —— 9/13 个有
- `RH_Captioner` —— 8/13 个有
- `Text Concatenate` —— 8/13 个有
- `CreateCFGScheduleFloatList` —— 6/13 个有
- `GetNode` —— 3/13 个有
- `SetNode` —— 3/13 个有
- `easy anythingIndexSwitch` —— 3/13 个有
- `Audio Cut (mtb)` —— 2/13 个有
- `Audio Duration (mtb)` —— 2/13 个有
- `ColorMatch` —— 2/13 个有
- `Int` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `LayerUtility: PurgeVRAM` —— 2/13 个有
- `Note Plus (mtb)` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `RHHiddenNodes` —— 2/13 个有
- `Bookmark (rgthree)` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `FloatConstant` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `PreviewAudio` —— 1/13 个有
- `WanVideoSLG` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
