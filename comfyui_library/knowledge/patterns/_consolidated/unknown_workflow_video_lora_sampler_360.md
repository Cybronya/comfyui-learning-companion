---
name: unknown_workflow_video_lora_sampler_360
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.978625
common_nodes: [Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan变身假面骑士发波动拳_1910730836017147906.json, 平台全量/Wan变身超级赛亚人_1902209827517702146.json, 视频生成/图生视频/Wan360度旋转-微波炉特效视频工作流_1899781896895881218.json, 视频生成/图生视频/Wan变身超级赛亚人_2079036262153023489.json, 视频生成/图生视频/Wan捏捏图生视频工作流_1899122164795133953.json, 视频生成/图生视频/Wan波动拳图生视频工作流_1899508208174809089.json, 视频生成/图生视频/【张元英跳舞】WAN2.1 跳舞特效_1914559831519494146.json, 视频生成/图生视频/让照片说话【万相图生视频】_1914130917185548290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_360

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Wan变身假面骑士发波动拳_1910730836017147906.json、平台全量/Wan变身超级赛亚人_1902209827517702146.json、视频生成/图生视频/Wan360度旋转-微波炉特效视频工作流_1899781896895881218.json、视频生成/图生视频/Wan变身超级赛亚人_2079036262153023489.json、视频生成/图生视频/Wan捏捏图生视频工作流_1899122164795133953.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Textbox` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `ConcatTextOfUtils` —— 1/8 个有
- `ImageBatch` —— 1/8 个有
- `KepStringLiteral` —— 1/8 个有
- `TextBox` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy indexAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
