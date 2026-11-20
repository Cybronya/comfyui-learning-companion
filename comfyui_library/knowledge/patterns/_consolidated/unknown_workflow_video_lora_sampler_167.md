---
name: unknown_workflow_video_lora_sampler_167
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.8345
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生数字人、动物、角色--InfiniteTalk+IndexTTS2语音克隆_1970779502160867329.json, 视频生成/图生视频/对口型-图生视频_2042896857407426562.json, 视频生成/图生视频/户外-Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2029255220571676673.json, 视频生成/图生视频/户外-Infinite talk数字人：动态加强高版V4（Lightx2v+Rcm）_2029417074241576961.json, 视频生成/图生视频/打造个人音乐+视频数字人-Infinite_Talk_1987692626436665345.json, 视频生成/图生视频/数字人-Infinite talk-对口型-动态加强版（Lightx2v+Rcm）_1995458566553264130.json, 视频生成/图生视频/数字人-Infinite talk-对口型-动态加强版（Lightx2v+Rcm）_2039856506417455105.json, 视频生成/图生视频/数字人口播专用 -阿浩_2029081632229036033.json, 视频生成/图生视频/数字人对口型_2065824497244135425.json, 视频生成/图生视频/数字人自用版_2044411398406545409.json, 视频生成/图生视频/极速高质量图生视频数字人-阿浩_2026900959795879938.json, 视频生成/图生视频/极速高质量图生视频数字人-阿浩_2028672160373415937.json, 视频生成/图生视频/超长视频生成 Infinite talk 图生视频 写实高清视频 数字人动态加强高版 Lightx2_2025798781039546370.json, 视频生成/图生视频/跨模态仿OVI无限时长图生视频含配音数字人工作流V1（支持中文）_1974878137764982786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_167

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/图生数字人、动物、角色--InfiniteTalk+IndexTTS2语音克隆_1970779502160867329.json、视频生成/图生视频/对口型-图生视频_2042896857407426562.json、视频生成/图生视频/户外-Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2029255220571676673.json、视频生成/图生视频/户外-Infinite talk数字人：动态加强高版V4（Lightx2v+Rcm）_2029417074241576961.json、视频生成/图生视频/打造个人音乐+视频数字人-Infinite_Talk_1987692626436665345.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 13/14 个有
- `LoadAudio` —— 13/14 个有
- `JWInteger` —— 11/14 个有
- `JWFloat` —— 9/14 个有
- `AudioCrop` —— 8/14 个有
- `Int` —— 4/14 个有
- `AddLabel` —— 3/14 个有
- `Label (rgthree)` —— 3/14 个有
- `SimpleMath+` —— 3/14 个有
- `TextToUppercase` —— 3/14 个有
- `IndexTTS2Run` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `SaveAudio` —— 1/14 个有
- `VHS_LoadAudioUpload` —— 1/14 个有
- `VHS_SplitImages` —— 1/14 个有
- `easy anythingIndexSwitch` —— 1/14 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/14 个有
- `easy indexTTSGenerateSimple` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
