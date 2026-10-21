---
name: unknown_workflow_video_sampler_vae_76
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.958857
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1940936064079183874.json, 视频生成/图生视频/1962815833489715202.json, 视频生成/图生视频/1947465024660983810.json, 视频生成/图生视频/1914213434668347393.json, 视频生成/图生视频/1958363442241552386.json, 视频生成/图生视频/1913561897336041474.json, 视频生成/图生视频/1915976312136073218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_76

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1940936064079183874.json、视频生成/图生视频/1962815833489715202.json、视频生成/图生视频/1947465024660983810.json、视频生成/图生视频/1914213434668347393.json、视频生成/图生视频/1958363442241552386.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 5/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 5/7 个有
- `GIMMVFI_interpolate` —— 5/7 个有
- `ImageResizeKJ` —— 5/7 个有
- `WanVideoClipVisionEncode` —— 5/7 个有
- `WanVideoExperimentalArgs` —— 5/7 个有
- `WanVideoTextEncode` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `UpscaleModelLoader` —— 4/7 个有
- `WanVideoLoraSelect` —— 4/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `Int` —— 3/7 个有
- `TextInputBasic` —— 3/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `WanVideoApplyNAG` —— 2/7 个有
- `WanVideoTextEncodeSingle` —— 2/7 个有
- `WanVideoUniAnimateDWPoseDetector` —— 2/7 个有
- `WanVideoUniAnimatePoseInput` —— 2/7 个有
- `CreateCFGScheduleFloatList` —— 1/7 个有
- `ImageScaleToMegapixels` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `WanVideoFreeInitArgs` —— 1/7 个有
- `WanVideoLoraSelectMulti` —— 1/7 个有
- `WanVideoVACEModelSelect` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
