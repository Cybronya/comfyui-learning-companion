---
name: unknown_workflow_video_sampler_vae_77
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.996429
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1917476719106920449.json, 视频生成/图生视频/1929004971717726210.json, 视频生成/图生视频/1923968706664460289.json, 视频生成/图生视频/1924687673779212289.json, 视频生成/图生视频/1934543155603644418.json, 视频生成/图生视频/1934460404364111874.json, 视频生成/图生视频/1937073203258773506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_77

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1917476719106920449.json、视频生成/图生视频/1929004971717726210.json、视频生成/图生视频/1923968706664460289.json、视频生成/图生视频/1924687673779212289.json、视频生成/图生视频/1934543155603644418.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 6/7 个有
- `WanVideoEnhanceAVideo` —— 6/7 个有
- `WanVideoExperimentalArgs` —— 6/7 个有
- `WanVideoSLG` —— 6/7 个有
- `WanVideoVACEModelSelect` —— 6/7 个有
- `WanVideoVACEStartToEndFrame` —— 6/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `Int` —— 4/7 个有
- `INTConstant` —— 3/7 个有
- `String Literal` —— 3/7 个有
- `GetImageRangeFromBatch` —— 2/7 个有
- `ImageBatchMulti` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `MaskBatchMulti` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LayerMask: LoadFlorence2Model` —— 1/7 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/7 个有
- `LoadWanVideoClipTextEncoder` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `WanVideoImageClipEncode` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
