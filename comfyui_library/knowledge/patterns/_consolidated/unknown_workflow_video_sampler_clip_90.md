---
name: unknown_workflow_video_sampler_clip_90
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.953
common_nodes: [Fast Groups Bypasser (rgthree), LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], Primitive string [Crystools], VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/360度旋转特效-wan图生视频KJ_1899625950118629378.json, 视频生成/图生视频/Wan2.1-阿里万相-图生视频(KJ版)_1894528926553911297.json, 视频生成/图生视频/杀手-视频特效_1901443764307509249.json, 视频生成/图生视频/肌肉男魅力特效-wan图生视频KJ_1899678523555008513.json, 视频生成/图生视频/膨胀特效-wan图生视频KJ_1899620141431439362.json, 视频生成/图生视频/跨屏幕牵手-Wan2.1图生视频_1896568283456528386.json, 视频生成/文生视频/Wan2.1-阿里万相开源文_图生视频(KJ版)_1894584540348743681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/360度旋转特效-wan图生视频KJ_1899625950118629378.json、视频生成/图生视频/Wan2.1-阿里万相-图生视频(KJ版)_1894528926553911297.json、视频生成/图生视频/杀手-视频特效_1901443764307509249.json、视频生成/图生视频/肌肉男魅力特效-wan图生视频KJ_1899678523555008513.json、视频生成/图生视频/膨胀特效-wan图生视频KJ_1899620141431439362.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `Primitive string [Crystools]`
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
- `Note _O` —— 5/7 个有
- `CR Text Concatenate` —— 4/7 个有
- `RH_Captioner` —— 4/7 个有
- `String Replace (mtb)` —— 4/7 个有
- `WanVideoLoraSelect` —— 4/7 个有
- `CM_IntToFloat` —— 3/7 个有
- `ImageScaleDownToSize` —— 3/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `WanVideoEmptyEmbeds` —— 2/7 个有
- `WanVideoExperimentalArgs` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
