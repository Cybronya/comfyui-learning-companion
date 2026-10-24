---
name: unknown_workflow_video_sampler_clip_107
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.945
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/空白工作流_1899517701415456770.json, 视频生成/图生视频/美女飞翔+AI视频生成=艾橘溪_1899801104287150081.json, 视频生成/图生视频/羞羞的铁拳+人物拳击特效=艾橘溪_1899436993728696322.json, 视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json, 视频生成/文生视频/Wan2.1高质量图生视频_1894956774334595074.json, 视频生成/文生视频/【转身舞动】升级版WAN2.1 网红跳舞视频动画_1919571339177562113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_107

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/空白工作流_1899517701415456770.json、视频生成/图生视频/美女飞翔+AI视频生成=艾橘溪_1899801104287150081.json、视频生成/图生视频/羞羞的铁拳+人物拳击特效=艾橘溪_1899436993728696322.json、视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json、视频生成/文生视频/Wan2.1高质量图生视频_1894956774334595074.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

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
- `WanVideoLoraSelect` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `easy imageSize` —— 3/6 个有
- `WanVideoTeaCache` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `TextWildcardList_AS` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
