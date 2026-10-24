---
name: unknown_workflow_video_sampler_clip_164
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.77975
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/中文出视频 WAN2.1 万相图生视频_1894627814531051521.json, 视频生成/图生视频/图生视频   Wan2.1  局部动作_2032283738113056769.json, 视频生成/图生视频/生成中文的AI视频+图片视频+通义万相=艾橘溪_1896135143269007362.json, 视频生成/图生视频/通义万相 Wan2.1 图生视频_1894649502454710273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/中文出视频 WAN2.1 万相图生视频_1894627814531051521.json、视频生成/图生视频/图生视频   Wan2.1  局部动作_2032283738113056769.json、视频生成/图生视频/生成中文的AI视频+图片视频+通义万相=艾橘溪_1896135143269007362.json、视频生成/图生视频/通义万相 Wan2.1 图生视频_1894649502454710273.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeAdvanced` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TextCombinerTwo` —— 1/4 个有
- `Textbox` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
