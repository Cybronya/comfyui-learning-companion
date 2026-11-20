---
name: unknown_workflow_video_lora_sampler_536
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json, 视频生成/图生视频/wanvideo_14B_pusa 图生视频工作流_1946953105147211777.json, 视频生成/文生视频/Wan2.1最新FusionX LORA  2分钟生视频_1935600068689068033.json, 视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_536

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json、视频生成/图生视频/wanvideo_14B_pusa 图生视频工作流_1946953105147211777.json、视频生成/文生视频/Wan2.1最新FusionX LORA  2分钟生视频_1935600068689068033.json、视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `Text Multiline` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoContextOptions` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
