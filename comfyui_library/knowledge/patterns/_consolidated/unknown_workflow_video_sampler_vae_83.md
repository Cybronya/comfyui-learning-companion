---
name: unknown_workflow_video_sampler_vae_83
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.861167
common_nodes: [DownloadAndLoadHyVideoTextEncoder, GetImageSizeAndCount, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoEnhanceAVideo, HyVideoI2VEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoVAELoader, LoadImage, Note _O, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1898308200272482306.json, 视频生成/图生视频/2065290197557932034.json, 视频生成/图生视频/1897648675362164738.json, 视频生成/图生视频/1908742730107727873.json, 视频生成/图生视频/1911249083103703042.json, 视频生成/图生视频/1897601417920598018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_83

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1898308200272482306.json、视频生成/图生视频/2065290197557932034.json、视频生成/图生视频/1897648675362164738.json、视频生成/图生视频/1908742730107727873.json、视频生成/图生视频/1911249083103703042.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `DownloadAndLoadHyVideoTextEncoder`
- `GetImageSizeAndCount`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoEnhanceAVideo`
- `HyVideoI2VEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoVAELoader`
- `LoadImage`
- `Note _O`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `HyVideoTorchCompileSettings` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `Note Plus (mtb)` —— 5/6 个有
- `Image Resize` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `CR Prompt Text` —— 2/6 个有
- `HyVideoLoraSelect` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadLatent` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SaveLatent` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
