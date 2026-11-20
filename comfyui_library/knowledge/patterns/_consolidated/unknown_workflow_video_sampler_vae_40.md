---
name: unknown_workflow_video_sampler_vae_40
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.975909
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1文生视频fusionX+NAG_1936289706663399425.json, 视频生成/文生视频/B1-Wan2.1- MagCache加速版文生视频fusionX+NAG_1934582390809370626.json, 视频生成/文生视频/B1-Wan2.1文生视频fusionX+NAG_1934499736151871490.json, 视频生成/文生视频/FusionX文生视频0629_1934893611441922049.json, 视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json, 视频生成/文生视频/Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json, 视频生成/文生视频/Wan2.1 Fusion X 文生视频_1947180692524019713.json, 视频生成/文生视频/Wan2.1 FusionX 智能手机快照 现实风格_1943829823070539777.json, 视频生成/文生视频/Wan2.1 FusionX文生视频极速版_1940968493145866242.json, 视频生成/文生视频/Wan2.1 日本美女主播直播带货视频讲解_1945637043122917377.json, 视频生成/文生视频/Wan2.1 美丽的日本歌舞表演风格的女人_1947907852955463682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_40

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan2.1文生视频fusionX+NAG_1936289706663399425.json、视频生成/文生视频/B1-Wan2.1- MagCache加速版文生视频fusionX+NAG_1934582390809370626.json、视频生成/文生视频/B1-Wan2.1文生视频fusionX+NAG_1934499736151871490.json、视频生成/文生视频/FusionX文生视频0629_1934893611441922049.json、视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoApplyNAG` —— 10/11 个有
- `WanVideoSLG` —— 10/11 个有
- `WanVideoTextEncodeSingle` —— 10/11 个有
- `UpscaleModelLoader` —— 8/11 个有
- `ImageScaleToMegapixels` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `WanVideoLoraSelect` —— 4/11 个有
- `LoadImageFromUrl` —— 2/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `ImageUpscaleWithModel` —— 1/11 个有
- `WanVideoMagCache` —— 1/11 个有
- `WanVideoTextEncode` —— 1/11 个有
- `WanVideoTorchCompileSettings` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
