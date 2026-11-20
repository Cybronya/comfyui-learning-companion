---
name: unknown_workflow_video_lora_sampler_810
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944333
common_nodes: [ImageBlur, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1 tile控制_1902591976716546050.json, 平台全量/wan2.1-1.3b-control-lora-tile转绘_1911997781874044930.json, 视频生成/图生视频/Wan2.1-Tile视频高清控制_1899280548576055298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_810

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan2.1 tile控制_1902591976716546050.json、平台全量/wan2.1-1.3b-control-lora-tile转绘_1911997781874044930.json、视频生成/图生视频/Wan2.1-Tile视频高清控制_1899280548576055298.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageBlur`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `Primitive string [Crystools]` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `WanVideoBlockSwap` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
