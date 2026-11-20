---
name: unknown_workflow_video_sampler_clip_97
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.943714
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/空白工作流_1899517701415456770.json, 视频生成/图生视频/美女飞翔+AI视频生成=艾橘溪_1899801104287150081.json, 视频生成/图生视频/羞羞的铁拳+人物拳击特效=艾橘溪_1899436993728696322.json, 视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json, 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json, 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1992837863268216833.json, 视频生成/文生视频/火力 全开！冲锋枪射击特效--万相WAN2.1_1934071211976478722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/空白工作流_1899517701415456770.json、视频生成/图生视频/美女飞翔+AI视频生成=艾橘溪_1899801104287150081.json、视频生成/图生视频/羞羞的铁拳+人物拳击特效=艾橘溪_1899436993728696322.json、视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json、视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
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
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoTeaCache` —— 5/7 个有
- `LayerUtility: PurgeVRAM` —— 4/7 个有
- `easy imageSize` —— 4/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `UpscaleModelLoader` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `PreviewImage` —— 1/7 个有
- `Select Image Indices` —— 1/7 个有
- `TextWildcardList_AS` —— 1/7 个有
- `WanVideoEnhanceAVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
