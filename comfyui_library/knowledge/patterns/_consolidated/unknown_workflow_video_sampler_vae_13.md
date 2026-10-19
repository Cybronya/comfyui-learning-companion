---
name: unknown_workflow_video_sampler_vae_13
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.698778
common_nodes: [AIO_Preprocessor, AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], SetNode, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1933077979956215810.json, 视频生成/图生视频/1986080138964205570.json, 视频生成/图生视频/1989255304942596097.json, 视频生成/图生视频/160帧-舞蹈-超高拟态-直出1920高清-V2版本_1942202708122341377.json, 视频生成/图生视频/1932617969560383490.json, 视频生成/图生视频/1927527393152634881.json, 视频生成/图生视频/1947326478251872258.json, 视频生成/图生视频/1943365680282693633.json, 视频生成/图生视频/1950083383838818305.json, 视频生成/图生视频/1922696527037480962.json, 视频生成/图生视频/1932273644485902337.json, 视频生成/图生视频/1992633923415109634.json, 视频生成/图生视频/1992639334528643074.json, 视频生成/图生视频/1966126625408675842.json, 视频生成/图生视频/1945365424944947201.json, 视频生成/图生视频/1946130631811055617.json, 视频生成/图生视频/1964248565730131970.json, 视频生成/文生视频/1949732964007059457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1933077979956215810.json、视频生成/图生视频/1986080138964205570.json、视频生成/图生视频/1989255304942596097.json、视频生成/图生视频/160帧-舞蹈-超高拟态-直出1920高清-V2版本_1942202708122341377.json、视频生成/图生视频/1932617969560383490.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 18 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `SetNode`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 17/18 个有
- `WanVideoSLG` —— 17/18 个有
- `ColorMatch` —— 15/18 个有
- `WanVideoTeaCache` —— 15/18 个有
- `ShowText|pysssss` —— 14/18 个有
- `WanVideoExperimentalArgs` —— 14/18 个有
- `easy cleanGpuUsed` —— 14/18 个有
- `ImpactSwitch` —— 13/18 个有
- `PreviewImage` —— 13/18 个有
- `SimpleMath+` —— 13/18 个有
- `RHHiddenNodes` —— 11/18 个有
- `WanVideoBlockSwap` —— 10/18 个有
- `WanVideoModelLoader` —— 10/18 个有
- `WanVideoTorchCompileSettings` —— 10/18 个有
- `WanVideoLoraSelect` —— 8/18 个有
- `WanVideoVACEModelSelect` —— 8/18 个有
- `ImageBlend` —— 5/18 个有
- `easy seed` —— 5/18 个有
- `Fast Groups Bypasser (rgthree)` —— 4/18 个有
- `ImagePadKJ` —— 4/18 个有
- `DepthAnything_V2` —— 3/18 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/18 个有
- `GetImageRangeFromBatch` —— 3/18 个有
- `WanVideoEasyCache` —— 2/18 个有
- `WanVideoSetRadialAttention` —— 2/18 个有
- `Joy_caption_two` —— 1/18 个有
- `Joy_caption_two_load` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
