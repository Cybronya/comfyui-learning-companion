---
name: unknown_workflow_video_sampler_clip_64
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.965444
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1894624556043141122.json, 视频生成/图生视频/1894632581118472194.json, 视频生成/图生视频/1895446243693232129.json, 视频生成/图生视频/1938851754044018689.json, 视频生成/图生视频/1994266529971765249.json, 视频生成/图生视频/1997177362523570178.json, 视频生成/图生视频/1899517701415456770.json, 视频生成/图生视频/1913599266676273153.json, 视频生成/文生视频/1919571339177562113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1894624556043141122.json、视频生成/图生视频/1894632581118472194.json、视频生成/图生视频/1895446243693232129.json、视频生成/图生视频/1938851754044018689.json、视频生成/图生视频/1994266529971765249.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
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
- `easy imageSize` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `WanVideoLoraSelect` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `TextInput_` —— 2/9 个有
- `WanVideoTeaCache` —— 2/9 个有
- `WanVideoTorchCompileSettings` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `FILM VFI` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `Primitive string [Crystools]` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `TextWildcardList_AS` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
