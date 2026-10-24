---
name: unknown_workflow_video_lora_sampler_82
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.918412
common_nodes: [CLIPVisionLoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AniWan+Fastwan+LightX64+Radial+Free最强万相wan2.1图生视频_1945425557527961601.json, 视频生成/图生视频/AniWan专业动漫超高动态图生视频加速版V1_1944770056771260417.json, 视频生成/图生视频/EasyCache+LightX2v+AniWan超高动态图生视频加速版V1_1946230889756913665.json, 视频生成/图生视频/FastWan+Aniwan+LightX2V高质量图生视频V1_1949398182790365185.json, 视频生成/图生视频/Fusionx+lightx2v图生视频_1941647575110074369.json, 视频生成/图生视频/KJ版WAN2.1 GGUF Q8 LightX2V加速图生视频高质量版V1_1942759645448744961.json, 视频生成/图生视频/LightX2v Rank64极限质量+AniWan超高动态图生视频加速版V1_1945356910293917698.json, 视频生成/图生视频/MTV Crafter+FusionX 3D运动建模动态图生视频V1_1958913367148802050.json, 视频生成/图生视频/MTV Crafter+FusionX 3D运动建模动态图生视频V1_1960985740777852930.json, 视频生成/图生视频/MoviiGen+Free+LightX64+AniWan+最强万相wan2.1图生视频_1945462640925921281.json, 视频生成/图生视频/Moviigen & lightx2v 电影级图生视频｜高清4K_1936033018391990273.json, 视频生成/图生视频/RadialAttn加速模式图生视频范例工作流V2_1946266555401560066.json, 视频生成/图生视频/ani全能视频S+fusionx+free动漫二次元鬼畜专用图生视频万相wan2.1工作流_1944601426138157058.json, 视频生成/图生视频/【b站开源】ani全能视频S + fusionx 图生视频｜动漫友好_1946050505720164354.json, 视频生成/图生视频/动态表情包_原图控制增强版_2008939674751995905.json, 视频生成/图生视频/微信动态表情包制作AniWan+Fastwan+LightX64+Radial+Free_1946428011036205057.json, 视频生成/图生视频/电影级图生视频moviigen+lightx2v+自动扩词+运镜万相win2.1_1935149925716172801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_82

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/AniWan+Fastwan+LightX64+Radial+Free最强万相wan2.1图生视频_1945425557527961601.json、视频生成/图生视频/AniWan专业动漫超高动态图生视频加速版V1_1944770056771260417.json、视频生成/图生视频/EasyCache+LightX2v+AniWan超高动态图生视频加速版V1_1946230889756913665.json、视频生成/图生视频/FastWan+Aniwan+LightX2V高质量图生视频V1_1949398182790365185.json、视频生成/图生视频/Fusionx+lightx2v图生视频_1941647575110074369.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPVisionLoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 16/17 个有
- `WanVideoExperimentalArgs` —— 15/17 个有
- `WanVideoSLG` —— 15/17 个有
- `WanVideoFreeInitArgs` —— 12/17 个有
- `WanVideoTextEncode` —— 9/17 个有
- `WanVideoVRAMManagement` —— 9/17 个有
- `RH_OneShot_Prompter` —— 8/17 个有
- `SimpleMath+` —— 8/17 个有
- `WanVideoApplyNAG` —— 8/17 个有
- `WanVideoTextEncodeSingle` —— 8/17 个有
- `WanVideoEasyCache` —— 6/17 个有
- `WanVideoSetRadialAttention` —— 4/17 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/17 个有
- `GIMMVFI_interpolate` —— 2/17 个有
- `WanVideoTeaCache` —— 2/17 个有
- `WanVideoTorchCompileSettings` —— 2/17 个有
- `BackgroundEraseNetwork` —— 1/17 个有
- `ImageConcanate` —— 1/17 个有
- `LayerMask: BiRefNetUltraV2` —— 1/17 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `WanVideoMagCache` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
