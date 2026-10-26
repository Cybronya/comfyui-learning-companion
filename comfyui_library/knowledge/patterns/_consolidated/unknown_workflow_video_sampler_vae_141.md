---
name: unknown_workflow_video_sampler_vae_141
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.945
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTextEmbedBridge, HyVideoTorchCompileSettings, HyVideoVAELoader, ImageResizeKJv2, LoadImage, TextEncodeHunyuanVideo_ImageToVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/混元Custom人物商品参考图生视频_1929828891127615489.json, 视频生成/图生视频/混元Custom单主体参考_1920972713995730945.json, 视频生成/图生视频/混元Custom单主题参考_1920770416519090178.json, 视频生成/图生视频/混元Custom多主题参考_1920831493852303362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/混元Custom人物商品参考图生视频_1929828891127615489.json、视频生成/图生视频/混元Custom单主体参考_1920972713995730945.json、视频生成/图生视频/混元Custom单主题参考_1920770416519090178.json、视频生成/图生视频/混元Custom多主题参考_1920831493852303362.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoTextEmbedBridge`
- `HyVideoTorchCompileSettings`
- `HyVideoVAELoader`
- `ImageResizeKJv2`
- `LoadImage`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `Primitive integer [Crystools]` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `HyVideoEnhanceAVideo` —— 1/4 个有
- `Int` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
