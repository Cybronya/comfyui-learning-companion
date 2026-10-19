---
name: unknown_workflow_video_sampler_clip_120
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8238
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1894627814531051521.json, 视频生成/图生视频/2032283738113056769.json, 视频生成/图生视频/1896135143269007362.json, 视频生成/图生视频/1894649502454710273.json, 视频生成/文生视频/1894963612530704385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1894627814531051521.json、视频生成/图生视频/2032283738113056769.json、视频生成/图生视频/1896135143269007362.json、视频生成/图生视频/1894649502454710273.json、视频生成/文生视频/1894963612530704385.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
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
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `ImageResizeAdvanced` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `RH_Prompter` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有
- `Textbox` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
