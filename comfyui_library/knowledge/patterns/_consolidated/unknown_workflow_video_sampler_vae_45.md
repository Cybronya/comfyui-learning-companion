---
name: unknown_workflow_video_sampler_vae_45
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.945222
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [Text Multiline, Primitive integer [Crystools]]
members: [图片生成/文生图/1924016938777759746.json, 图片生成/文生图/1933717889453350913.json, 图片生成/文生图/1935149861173927937.json, 视频生成/图生视频/1934805890510069762.json, 视频生成/图生视频/1935618594950807553.json, 视频生成/图生视频/1935624058308317186.json, 视频生成/图生视频/1937018239794974722.json, 视频生成/图生视频/1924274970828918785.json, 视频生成/图生视频/1928305949314793473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_45

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1924016938777759746.json、图片生成/文生图/1933717889453350913.json、图片生成/文生图/1935149861173927937.json、视频生成/图生视频/1934805890510069762.json、视频生成/图生视频/1935618594950807553.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 8/9 个有
- `Text Multiline` —— 7/9 个有
- `WanVideoEnhanceAVideo` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `Primitive integer [Crystools]` —— 6/9 个有
- `WanVideoVACEEncode` —— 6/9 个有
- `WanVideoVACEStartToEndFrame` —— 6/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `WanVideoLoraSelect` —— 4/9 个有
- `WanVideoVACEModelSelect` —— 4/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/9 个有
- `GIMMVFI_interpolate` —— 3/9 个有
- `WanVideoEmptyEmbeds` —— 3/9 个有
- `CR Upscale Image` —— 2/9 个有
- `ImageResizeKJ` —— 2/9 个有
- `Int` —— 2/9 个有
- `JWInteger` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `ImageRepeat` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `String Literal` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、Primitive integer [Crystools]
