---
name: unknown_workflow_video_sampler_6
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.947588
common_nodes: [AudioSeparation, CLIPVisionLoader, Int, LoadImage, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json, 图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json, 数字人/数字人/API-对口型-数字人-最新_2070339599389511682.json, 数字人/数字人/API-对口型-数字人_2043715361241047042.json, 数字人/数字人/API-对口型-数字人_2067238745916657666.json, 数字人/数字人/API-对口型-数字人（1280）_2057461580308238337.json, 数字人/数字人/API-对口型数字人-1280_2057455520889524226.json, 数字人/数字人/CustomerKing 数字人商品带货_2080338543561502721.json, 数字人/数字人/Infinite Talk数字人_1978415131019382786.json, 数字人/数字人/InfiniteTalk_MV唱歌_2115087623424397313.json, 数字人/数字人/digital_combination.json_2061365227471589378.json, 数字人/数字人/对口型-数字人_2052629675733733377.json, 数字人/数字人/数字人infinitetalk_1985970612617322498.json, 视频生成/图生视频/API-对口型-数字人_2051682079896809474.json, 视频生成/图生视频/InfiniteTalk图生视频+对口型+唱歌数字人_1991891221526409218.json, 视频生成/图生视频/InfiniteTalk图生视频+对口型+唱歌数字人_1994964520529539073.json, 视频生成/图生视频/高动态音乐数字人Infinite Talk 图生视频+对口型_1992045257871216642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_6

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json、图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json、数字人/数字人/API-对口型-数字人-最新_2070339599389511682.json、数字人/数字人/API-对口型-数字人_2043715361241047042.json、数字人/数字人/API-对口型-数字人_2067238745916657666.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `Int`
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 16/17 个有
- `easy showAnything` —— 16/17 个有
- `MultiTalkModelLoader` —— 15/17 个有
- `WanVideoBlockSwap` —— 15/17 个有
- `WanVideoLoraSelect` —— 15/17 个有
- `WanVideoModelLoader` —— 15/17 个有
- `WanVideoTorchCompileSettings` —— 15/17 个有
- `DownloadAndLoadWav2VecModel` —— 13/17 个有
- `ImageResizeKJv2` —— 13/17 个有
- `LoadAudio` —— 13/17 个有
- `LoadWanVideoT5TextEncoder` —— 13/17 个有
- `RH_GetAudioDuration` —— 13/17 个有
- `WanVideoVAELoader` —— 13/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/17 个有
- `easy int` —— 9/17 个有
- `RHHiddenNodes` —— 6/17 个有
- `VHS_LoadAudioUpload` —— 6/17 个有
- `Audio Duration (mtb)` —— 4/17 个有
- `ColorMatch` —— 4/17 个有
- `ImageScaleBy` —— 4/17 个有
- `Pick From Batch (mtb)` —— 4/17 个有
- `SaveImage` —— 4/17 个有
- `CreateVideo` —— 2/17 个有
- `JWFloat` —— 2/17 个有
- `PreViewVideo` —— 2/17 个有
- `SaveAudio` —— 1/17 个有
- `VHS_LoadVideo` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
