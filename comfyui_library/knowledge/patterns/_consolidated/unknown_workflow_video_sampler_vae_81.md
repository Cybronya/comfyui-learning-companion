---
name: unknown_workflow_video_sampler_vae_81
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.554857
common_nodes: [Any Switch (rgthree), DWPreprocessor, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, ImageResize+, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy int, easy positive]
problems: []
missing: []
members: [平台全量/VACE 视频转绘 骨骼迁移_1915609929472737281.json, 平台全量/VACE 视频转绘_1921157630155489282.json, 平台全量/VACE_14B_视频首帧重绘_1930149558649786370.json, 平台全量/Wan2.1 VACE Control视频转绘_1949721598378549250.json, 平台全量/Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217.json, 视频生成/图生视频/VACE 视频转绘 真人转漫画 漫画转真人即可_1913722947981508609.json, 视频生成/文生视频/【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_81

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/VACE 视频转绘 骨骼迁移_1915609929472737281.json、平台全量/VACE 视频转绘_1921157630155489282.json、平台全量/VACE_14B_视频首帧重绘_1930149558649786370.json、平台全量/Wan2.1 VACE Control视频转绘_1949721598378549250.json、平台全量/Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `DWPreprocessor`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `Fast Groups Muter (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
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
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 6/7 个有
- `ImageFromBatch` —— 6/7 个有
- `WanVideoTeaCache` —— 6/7 个有
- `AddLabel` —— 5/7 个有
- `EmptyImage` —— 5/7 个有
- `Florence2ModelLoader` —— 5/7 个有
- `Florence2Run` —— 5/7 个有
- `JoinStrings` —— 5/7 个有
- `String Literal` —— 5/7 个有
- `WanVideoVRAMManagement` —— 5/7 个有
- `WanVideoVACEModelSelect` —— 4/7 个有
- `easy seed` —— 4/7 个有
- `Bookmark (rgthree)` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `WanVideoLoraSelect` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `DensePosePreprocessor` —— 1/7 个有
- `FILM VFI` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageBlend` —— 1/7 个有
- `ImageComposite+` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `InspyrenetRembg` —— 1/7 个有
- `LoadImageFromUrl` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
