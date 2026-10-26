---
name: unknown_workflow_video_sampler_vae_164
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.582667
common_nodes: [EmptyImage, GetImageSizeAndCount, GetNode, ImageConcanate, ImageConcatMulti, JoinStrings, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy int, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 VACE 双图参考_1948576222688227330.json, 视频生成/图生视频/vace 视频双图参考 卖货必备_1911155835706273794.json, 视频生成/图生视频/多图参考生视频_1933060763407843330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_164

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 VACE 双图参考_1948576222688227330.json、视频生成/图生视频/vace 视频双图参考 卖货必备_1911155835706273794.json、视频生成/图生视频/多图参考生视频_1933060763407843330.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `ImageConcatMulti`
- `JoinStrings`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `Bookmark (rgthree)` —— 2/3 个有
- `ImageCompositeMasked` —— 2/3 个有
- `ImageRemoveBackground+` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `TransparentBGSession+` —— 2/3 个有
- `WanVideoTeaCache` —— 2/3 个有
- `easy imageScaleDownToSize` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoVRAMManagement` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
