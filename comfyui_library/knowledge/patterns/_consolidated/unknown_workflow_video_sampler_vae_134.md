---
name: unknown_workflow_video_sampler_vae_134
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.49525
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 multitalk 数字人工作流_1950489721401167873.json, 视频生成/图生视频/wanvideo_multitalk 声音驱动视频生成_1937349573826527233.json, 视频生成/图生视频/万象视频MultiTalk——MV制造机_1943647883407360002.json, 视频生成/图生视频/自制-MultiTalk v2 运镜版_1941456171754799106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_134

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2 multitalk 数字人工作流_1950489721401167873.json、视频生成/图生视频/wanvideo_multitalk 声音驱动视频生成_1937349573826527233.json、视频生成/图生视频/万象视频MultiTalk——MV制造机_1943647883407360002.json、视频生成/图生视频/自制-MultiTalk v2 运镜版_1941456171754799106.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `VHS_DuplicateImages` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/4 个有
- `WanVideoUni3C_embeds` —— 3/4 个有
- `FloatConstant` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `RH_GetAudioDuration` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `Bjornulf_ShowStringText` —— 1/4 个有
- `CreateCFGScheduleFloatList` —— 1/4 个有
- `Display Int (rgthree)` —— 1/4 个有
- `DownloadAndLoadFlorence2Model` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWFloatToString` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoExperimentalArgs` —— 1/4 个有
- `WanVideoTeaCache` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
