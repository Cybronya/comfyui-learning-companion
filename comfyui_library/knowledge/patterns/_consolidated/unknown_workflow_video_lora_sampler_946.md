---
name: unknown_workflow_video_lora_sampler_946
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.959
common_nodes: [INTConstant, ImageResize+, JWInteger, LayerUtility: PurgeVRAM, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2首尾帧工作流—Kj加速版_1962914848373968898.json, 视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json, 视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_946

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan2.2首尾帧工作流—Kj加速版_1962914848373968898.json、视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json、视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `WanVideoApplyNAG` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
