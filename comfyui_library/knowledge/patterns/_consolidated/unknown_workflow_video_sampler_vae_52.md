---
name: unknown_workflow_video_sampler_vae_52
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.831
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/b站开源二次元ani全能视频S视频模型_1945071960848257026.json, 视频生成/图生视频/lightx2v-720P-图到视频-rank128-rank32-FreeInit对比测试_1945761108445556738.json, 视频生成/图生视频/万相Skyreels V2图生长视频_1915024014367227906.json, 视频生成/图生视频/万能图生视频_Aniwan_1945716479117447170.json, 视频生成/图生视频/动漫图生视频 wan ani全能视频S_1945116426497871874.json, 视频生成/图生视频/图生视频 Wan I2V nightly_1913661782513385473.json, 视频生成/图生视频/图生视频 首尾帧 Wan FLF nightly_1913309276788719618.json, 视频生成/图生视频/生产级图生视频 Wan I2V API latent output_1917988631829745665.json, 视频生成/图生视频/生产级图生视频 Wan I2V API latent output_2050270690158358530.json, 视频生成/图生视频/视频转绘 Fun Control nightly_1922720148057198593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_52

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/b站开源二次元ani全能视频S视频模型_1945071960848257026.json、视频生成/图生视频/lightx2v-720P-图到视频-rank128-rank32-FreeInit对比测试_1945761108445556738.json、视频生成/图生视频/万相Skyreels V2图生长视频_1915024014367227906.json、视频生成/图生视频/万能图生视频_Aniwan_1945716479117447170.json、视频生成/图生视频/动漫图生视频 wan ani全能视频S_1945116426497871874.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoClipTextEncoder` —— 9/10 个有
- `WanVideoEnhanceAVideo` —— 9/10 个有
- `WanVideoLoraSelect` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `WanVideoExperimentalArgs` —— 7/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `WanVideoTeaCache` —— 6/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 5/10 个有
- `GIMMVFI_interpolate` —— 5/10 个有
- `WanVideoVRAMManagement` —— 5/10 个有
- `WanVideoFreeInitArgs` —— 4/10 个有
- `ImageResizeKJ` —— 3/10 个有
- `ImageBlur` —— 2/10 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 2/10 个有
- `RH_Captioner` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `SaveLatent` —— 2/10 个有
- `CLIPVisionLoader` —— 1/10 个有
- `Int` —— 1/10 个有
- `LayerUtility: TextBox` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `WanVideoControlEmbeds` —— 1/10 个有
- `WanVideoEncode` —— 1/10 个有
- `WanVideoMagCache` —— 1/10 个有
- `easy seed` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
