---
name: unknown_workflow_video_vae_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [DownloadAndLoadHyVideoTextEncoder, GetImageSizeAndCount, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoTextEncode, HyVideoVAELoader, ImageConcatMulti, ImageResizeKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/HyVideoFlowEdit 混元视频元素替换_1885958983033737218.json, 平台全量/混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_vae_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/HyVideoFlowEdit 混元视频元素替换_1885958983033737218.json、平台全量/混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `DownloadAndLoadHyVideoTextEncoder`
- `GetImageSizeAndCount`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoModelLoader`
- `HyVideoTextEncode`
- `HyVideoVAELoader`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `HyVideoFlowEditSamplerWrapper` —— 1/2 个有
- `HyVideoSampler` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
