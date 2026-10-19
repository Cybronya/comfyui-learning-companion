---
name: unknown_workflow_video_sampler_clip_36
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.939
common_nodes: [Fast Groups Bypasser (rgthree), LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1899625950118629378.json, 视频生成/图生视频/1894528926553911297.json, 视频生成/图生视频/1941226969910689794.json, 视频生成/图生视频/1941218870319595522.json, 视频生成/图生视频/1901443764307509249.json, 视频生成/图生视频/1941220218918301698.json, 视频生成/图生视频/1941765347643125762.json, 视频生成/图生视频/1899678523555008513.json, 视频生成/图生视频/1899620141431439362.json, 视频生成/图生视频/1896568283456528386.json, 视频生成/图生视频/1941194683714584578.json, 视频生成/文生视频/1894584540348743681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1899625950118629378.json、视频生成/图生视频/1894528926553911297.json、视频生成/图生视频/1941226969910689794.json、视频生成/图生视频/1941218870319595522.json、视频生成/图生视频/1901443764307509249.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 9/12 个有
- `LayerUtility: PurgeVRAM` —— 8/12 个有
- `Primitive integer [Crystools]` —— 7/12 个有
- `Primitive string [Crystools]` —— 7/12 个有
- `WanVideoExperimentalArgs` —— 7/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `Note _O` —— 5/12 个有
- `CR Text Concatenate` —— 4/12 个有
- `RH_Captioner` —— 4/12 个有
- `String Replace (mtb)` —— 4/12 个有
- `CM_IntToFloat` —— 3/12 个有
- `ImageScaleDownToSize` —— 3/12 个有
- `WanVideoEmptyEmbeds` —— 2/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
