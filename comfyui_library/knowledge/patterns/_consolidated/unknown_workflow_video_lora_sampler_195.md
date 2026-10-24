---
name: unknown_workflow_video_lora_sampler_195
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8095
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/ani，ani全能视频S自选这些的的wan2.1自用加速7步_1944806594343522306.json, 视频生成/图生视频/lightx2v加速24fps版高运动最高质量版图生视频V1_1934996455494983682.json, 视频生成/图生视频/【加速版】lightx2v 16fps 图生视频_1936041797762076674.json, 视频生成/图生视频/万能图生视频_Aniwan_1945716479117447170.json, 视频生成/图生视频/动漫图生视频 wan ani全能视频S_1945116426497871874.json, 视频生成/图生视频/图生视频 Wan I2V nightly_1913661782513385473.json, 视频生成/图生视频/图生视频 首尾帧 Wan FLF nightly_1913309276788719618.json, 视频生成/图生视频/生产级图生视频 Wan I2V API latent output_1917988631829745665.json, 视频生成/图生视频/生产级图生视频 Wan I2V API latent output_2050270690158358530.json, 视频生成/图生视频/视频转绘 Fun Control nightly_1922720148057198593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_195

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/ani，ani全能视频S自选这些的的wan2.1自用加速7步_1944806594343522306.json、视频生成/图生视频/lightx2v加速24fps版高运动最高质量版图生视频V1_1934996455494983682.json、视频生成/图生视频/【加速版】lightx2v 16fps 图生视频_1936041797762076674.json、视频生成/图生视频/万能图生视频_Aniwan_1945716479117447170.json、视频生成/图生视频/动漫图生视频 wan ani全能视频S_1945116426497871874.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 9/10 个有
- `WanVideoSLG` —— 8/10 个有
- `LoadWanVideoClipTextEncoder` —— 7/10 个有
- `WanVideoExperimentalArgs` —— 7/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `WanVideoVRAMManagement` —— 7/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 5/10 个有
- `GIMMVFI_interpolate` —— 5/10 个有
- `WanVideoTeaCache` —— 4/10 个有
- `CLIPVisionLoader` —— 3/10 个有
- `Text Multiline` —— 3/10 个有
- `WanVideoFreeInitArgs` —— 3/10 个有
- `ImageBlur` —— 2/10 个有
- `JWInteger` —— 2/10 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `SaveLatent` —— 2/10 个有
- `CR Value` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `LayerUtility: TextBox` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `WanVideoControlEmbeds` —— 1/10 个有
- `WanVideoEasyCache` —— 1/10 个有
- `WanVideoEncode` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
