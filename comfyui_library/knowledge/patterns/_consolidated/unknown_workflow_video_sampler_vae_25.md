---
name: unknown_workflow_video_sampler_vae_25
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.966154
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: [String Literal]
members: [视频生成/文生视频/1934538720651747329.json, 视频生成/文生视频/1934893611441922049.json, 视频生成/文生视频/1946373102530125826.json, 视频生成/文生视频/1947181441907732481.json, 视频生成/文生视频/1947180692524019713.json, 视频生成/文生视频/1943829823070539777.json, 视频生成/文生视频/1940968493145866242.json, 视频生成/文生视频/1945637043122917377.json, 视频生成/文生视频/1947907852955463682.json, 视频生成/文生视频/1934584295552163842.json, 视频生成/文生视频/1933775109922709506.json, 视频生成/文生视频/1947915676540383234.json, 视频生成/文生视频/1935006868597350401.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/1934538720651747329.json、视频生成/文生视频/1934893611441922049.json、视频生成/文生视频/1946373102530125826.json、视频生成/文生视频/1947181441907732481.json、视频生成/文生视频/1947180692524019713.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 13 个 workflow 都包含：
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
- `DownloadAndLoadGIMMVFIModel` —— 12/13 个有
- `GIMMVFI_interpolate` —— 12/13 个有
- `WanVideoApplyNAG` —— 12/13 个有
- `WanVideoTextEncodeSingle` —— 12/13 个有
- `ImageScaleToMegapixels` —— 11/13 个有
- `UpscaleModelLoader` —— 11/13 个有
- `WanVideoSLG` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 5/13 个有
- `WanVideoLoraSelect` —— 5/13 个有
- `LoadImageFromUrl` —— 2/13 个有
- `Note Plus (mtb)` —— 2/13 个有
- `WanVideoTorchCompileSettings` —— 2/13 个有
- `String Literal` —— 1/13 个有
- `WanVideoTeaCache` —— 1/13 个有
- `WanVideoTextEncode` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal
