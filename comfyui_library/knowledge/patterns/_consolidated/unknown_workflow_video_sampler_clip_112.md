---
name: unknown_workflow_video_sampler_clip_112
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.916
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan图生视频工作流-KJ版_1894765402319159298.json, 视频生成/图生视频/Wan图生视频特效版（捏捏、挤压、切片）-KJ版_1899884316468600834.json, 视频生成/图生视频/wan镜头拉近到眼睛_1915835994845941761.json, 视频生成/图生视频/【抖音同款】抖胸舞_1922170035954188290.json, 视频生成/图生视频/【简易版】万物捏捏乐 ， 图片挤压捏爆视频特效- StarAi_1900639314223448065.json, 视频生成/图生视频/抖起来_1997177362523570178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan图生视频工作流-KJ版_1894765402319159298.json、视频生成/图生视频/Wan图生视频特效版（捏捏、挤压、切片）-KJ版_1899884316468600834.json、视频生成/图生视频/wan镜头拉近到眼睛_1915835994845941761.json、视频生成/图生视频/【抖音同款】抖胸舞_1922170035954188290.json、视频生成/图生视频/【简易版】万物捏捏乐 ， 图片挤压捏爆视频特效- StarAi_1900639314223448065.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

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
- `WanVideoTeaCache` —— 4/6 个有
- `easy imageSize` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `CR Text Replace` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `CropFace` —— 1/6 个有
- `HyVideoEnhanceAVideo` —— 1/6 个有
- `Int` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
