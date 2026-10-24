---
name: unknown_workflow_video_sampler_vae_133
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.856
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 FusionX Phantom NAG多图像转视频_1949705582357422081.json, 视频生成/图生视频/Wan2.1 FusionX Phantom 多图像转视频_1949690915247017986.json, 视频生成/图生视频/wanvideo_14B_pusa 图生视频工作流_1946953105147211777.json, 视频生成/图生视频/大融合参考生视频 FusionX Phantom_1934266814887063554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_133

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 FusionX Phantom NAG多图像转视频_1949705582357422081.json、视频生成/图生视频/Wan2.1 FusionX Phantom 多图像转视频_1949690915247017986.json、视频生成/图生视频/wanvideo_14B_pusa 图生视频工作流_1946953105147211777.json、视频生成/图生视频/大融合参考生视频 FusionX Phantom_1934266814887063554.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoPhantomEmbeds` —— 3/4 个有
- `LoadImageFromUrl` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `WanVideoApplyNAG` —— 2/4 个有
- `WanVideoTextEncode` —— 2/4 个有
- `WanVideoTextEncodeSingle` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
