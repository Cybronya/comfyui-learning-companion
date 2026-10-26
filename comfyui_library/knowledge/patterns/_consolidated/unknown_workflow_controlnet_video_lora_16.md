---
name: unknown_workflow_controlnet_video_lora_16
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.872143
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/PT娃导单图运镜控制串联版_1941554640133767170.json, 视频生成/图生视频/PT娃导单图运镜控制流单节点版_1941548722545442818.json, 视频生成/图生视频/WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json, 视频生成/图生视频/wanvideo_multitalk_test_01g_1936629963053256706.json, 视频生成/图生视频/图片+音频驱动数字人（PT单图运镜控制数字人自由运镜）_1942053669372379138.json, 视频生成/图生视频/开源顶流MultiTalk Kijai版单人工作流_1936154909266055170.json, 视频生成/图生视频/自制-MultiTalk v2 运镜版_1941456171754799106.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/PT娃导单图运镜控制串联版_1941554640133767170.json、视频生成/图生视频/PT娃导单图运镜控制流单节点版_1941548722545442818.json、视频生成/图生视频/WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json、视频生成/图生视频/wanvideo_multitalk_test_01g_1936629963053256706.json、视频生成/图生视频/图片+音频驱动数字人（PT单图运镜控制数字人自由运镜）_1942053669372379138.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
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
- `PT_KeyframeCamera` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `RepeatImageBatch` —— 4/7 个有
- `CreateCFGScheduleFloatList` —— 2/7 个有
- `VHS_DuplicateImages` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `Bjornulf_ShowStringText` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `FloatConstant` —— 1/7 个有
- `GetImagesFromBatchIndexed` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `ImageBatch` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `JWFloatToString` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
