---
name: unknown_workflow_video_upscale_sampler_5
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.981
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadImage, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/ani全能视频S专业动漫2.0模型版图生视频_1944587037297266689.json, 视频生成/图生视频/sky 玩偶起飞_1914213434668347393.json, 视频生成/图生视频/wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json, 视频生成/图生视频/wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json, 视频生成/图生视频/wan2.2首尾帧——KJ流_1958363442241552386.json, 视频生成/图生视频/wanvideo首尾帧高清放大补针版_1912059507571392514.json, 视频生成/图生视频/wan美女视频转绘，跳舞15秒直出_1913561897336041474.json, 视频生成/图生视频/服装展示图像转视频_1915976312136073218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/ani全能视频S专业动漫2.0模型版图生视频_1944587037297266689.json、视频生成/图生视频/sky 玩偶起飞_1914213434668347393.json、视频生成/图生视频/wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json、视频生成/图生视频/wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json、视频生成/图生视频/wan2.2首尾帧——KJ流_1958363442241552386.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 6/8 个有
- `WanVideoClipVisionEncode` —— 6/8 个有
- `WanVideoEnhanceAVideo` —— 6/8 个有
- `WanVideoExperimentalArgs` —— 6/8 个有
- `WanVideoLoraSelect` —— 6/8 个有
- `WanVideoTeaCache` —— 6/8 个有
- `ImageUpscaleWithModel` —— 5/8 个有
- `CLIPVisionLoader` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `ImageScaleToMegapixels` —— 3/8 个有
- `Int` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `TextInputBasic` —— 3/8 个有
- `Get resolution [Crystools]` —— 2/8 个有
- `ImageSmartSharpen+` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `LoadWanVideoClipTextEncoder` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `WanVideoUniAnimateDWPoseDetector` —— 2/8 个有
- `WanVideoUniAnimatePoseInput` —— 2/8 个有
- `CreateCFGScheduleFloatList` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
