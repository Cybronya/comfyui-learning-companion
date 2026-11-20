---
name: unknown_workflow_video_sampler_vae_31
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.968917
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/FusionX文生视频0629_1934893611441922049.json, 视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json, 视频生成/文生视频/Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json, 视频生成/文生视频/Wan2.1 Fusion X 文生视频_1947180692524019713.json, 视频生成/文生视频/Wan2.1 FusionX 智能手机快照 现实风格_1943829823070539777.json, 视频生成/文生视频/Wan2.1 FusionX文生视频极速版_1940968493145866242.json, 视频生成/文生视频/Wan2.1 日本美女主播直播带货视频讲解_1945637043122917377.json, 视频生成/文生视频/Wan2.1 美丽的日本歌舞表演风格的女人_1947907852955463682.json, 视频生成/文生视频/Wan2.1FusionX-超高清文生视频_1934584295552163842.json, 视频生成/文生视频/Wan2.1文生视频fusionX+NAG_1933775109922709506.json, 视频生成/文生视频/[最新文生视频] Wan2.1 美女模特华丽转身视频特效_1947915676540383234.json, 视频生成/文生视频/龙明Wan2.1文生视频fusionX+NAG_1935006868597350401.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_31

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/FusionX文生视频0629_1934893611441922049.json、视频生成/文生视频/Wan2.1  KPOP Idol turn 偶像转身_1946373102530125826.json、视频生成/文生视频/Wan2.1 Fusion X  文生视频NAG_1947181441907732481.json、视频生成/文生视频/Wan2.1 Fusion X 文生视频_1947180692524019713.json、视频生成/文生视频/Wan2.1 FusionX 智能手机快照 现实风格_1943829823070539777.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ImageScaleToMegapixels` —— 11/12 个有
- `UpscaleModelLoader` —— 11/12 个有
- `WanVideoApplyNAG` —— 11/12 个有
- `WanVideoSLG` —— 11/12 个有
- `WanVideoTextEncodeSingle` —— 11/12 个有
- `Fast Groups Bypasser (rgthree)` —— 5/12 个有
- `WanVideoLoraSelect` —— 5/12 个有
- `LoadImageFromUrl` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `WanVideoTextEncode` —— 1/12 个有
- `WanVideoTorchCompileSettings` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
