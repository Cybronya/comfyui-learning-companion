---
name: unknown_workflow_video_sampler_vae_71
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.679
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1919743926129852417.json, 视频生成/图生视频/1916922893887016961.json, 视频生成/图生视频/1917000103838547969.json, 视频生成/图生视频/1948590349152321538.json, 视频生成/图生视频/1927647202212986882.json, 视频生成/图生视频/1920720222377152514.json, 视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_71

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1919743926129852417.json、视频生成/图生视频/1916922893887016961.json、视频生成/图生视频/1917000103838547969.json、视频生成/图生视频/1948590349152321538.json、视频生成/图生视频/1927647202212986882.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `INTConstant`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `WanVideoVRAMManagement` —— 6/7 个有
- `CreateCFGScheduleFloatList` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `WanVideoContextOptions` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `CLIPLoader` —— 1/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `CR Integer To String` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LoadImageFromUrl` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `WanVideoEnhanceAVideo` —— 1/7 个有
- `WanVideoTextEmbedBridge` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
