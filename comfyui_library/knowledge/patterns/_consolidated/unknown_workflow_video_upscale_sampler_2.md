---
name: unknown_workflow_video_upscale_sampler_2
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.949
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageResizeKJ, ImageScaleToMegapixels, ImageSmartSharpen+, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/ani全能视频S专业动漫2.0模型版图生视频_1944587037297266689.json, 视频生成/图生视频/fusionx 图生视频提速补版又爱了+lora_1934580843572862978.json, 视频生成/图生视频/wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json, 视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG_1933771102806003714.json, 视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG，上传图片点击运行工作流即可！_2040762237102592001.json, 视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG，上传图片点击运行工作流即可！_2046787167770382338.json, 视频生成/图生视频/万相Skyreels V2突破81帧魔咒工作流_1913991140356620289.json, 视频生成/图生视频/像素风格2.0模型版图生视频_2056181586005110785.json, 视频生成/图生视频/全能视频S专业动漫2.0模型版图生视频_2055177930787041282.json, 视频生成/图生视频/全能视频S专业动漫2.0模型版图生视频_2056263992364060673.json, 视频生成/图生视频/全能视频S专业动漫2.0模型版图生视频_2056548681435926530.json, 视频生成/图生视频/全能视频S专业动漫2.0模型版图生视频_2056904231692627969.json, 视频生成/图生视频/全能视频S专业动漫2.0模型版图生视频_2059187455856832514.json, 视频生成/图生视频/全能视频专业动漫2.0-图生视频-最新_2056273124878016513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/ani全能视频S专业动漫2.0模型版图生视频_1944587037297266689.json、视频生成/图生视频/fusionx 图生视频提速补版又爱了+lora_1934580843572862978.json、视频生成/图生视频/wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json、视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG_1933771102806003714.json、视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG，上传图片点击运行工作流即可！_2040762237102592001.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageResizeKJ`
- `ImageScaleToMegapixels`
- `ImageSmartSharpen+`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 11/14 个有
- `WanVideoLoraSelect` —— 10/14 个有
- `WanVideoTextEncode` —— 10/14 个有
- `RH_Translator` —— 9/14 个有
- `WanVideoApplyNAG` —— 4/14 个有
- `WanVideoTextEncodeSingle` —— 4/14 个有
- `CLIPVisionLoader` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `ImageUpscaleWithModel` —— 1/14 个有
- `Int` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `WanVideoClipVisionEncode` —— 1/14 个有
- `WanVideoTeaCache` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
