---
name: unknown_workflow_video_sampler_clip_100
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.770333
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1915835994845941761.json, 视频生成/图生视频/1895846905987596290.json, 视频生成/图生视频/1942427410207813634.json, 视频生成/图生视频/1942490603743555586.json, 视频生成/图生视频/1944753394462674945.json, 视频生成/图生视频/1942526282015911937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_100

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1915835994845941761.json、视频生成/图生视频/1895846905987596290.json、视频生成/图生视频/1942427410207813634.json、视频生成/图生视频/1942490603743555586.json、视频生成/图生视频/1944753394462674945.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 5/6 个有
- `Int` —— 4/6 个有
- `LayerUtility: PurgeVRAM` —— 4/6 个有
- `WanVideoEnhanceAVideo` —— 4/6 个有
- `WanVideoExperimentalArgs` —— 4/6 个有
- `WanVideoTeaCache` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `easy float` —— 2/6 个有
- `CropFace` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `String` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
