---
name: unknown_workflow_video_sampler_vae_160
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.567667
common_nodes: [Any Switch (rgthree), DWPreprocessor, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, ImageFromBatch, ImageResize+, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy int, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/VACE 动作迁移_1917063491289812993.json, 视频生成/图生视频/VACE 视频转绘 真人转漫画 漫画转真人即可_1913722947981508609.json, 视频生成/文生视频/【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_160

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/VACE 动作迁移_1917063491289812993.json、视频生成/图生视频/VACE 视频转绘 真人转漫画 漫画转真人即可_1913722947981508609.json、视频生成/文生视频/【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `DWPreprocessor`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `Fast Groups Muter (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch`
- `ImageResize+`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `EmptyImage` —— 2/3 个有
- `Florence2ModelLoader` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `String Literal` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `WanVideoVRAMManagement` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
