---
name: unknown_workflow_video_lora_unet_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9135
common_nodes: [CLIPLoader, CreateVideo, ImageConcatMulti, LoraLoaderModelOnly, MiniMaxH3Director, ModelPreviewOverrideKJ, Note Plus (mtb), SaveVideo, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MiniMax H3 导演台加速版全能工作流-宗门神曲多人替换演示_2086298148011593730.json, 视频生成/图生视频/MiniMax H3 导演台加速版全能工作流-宗门神曲多人替换演示_2084983882264436737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_unet_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/MiniMax H3 导演台加速版全能工作流-宗门神曲多人替换演示_2086298148011593730.json、视频生成/图生视频/MiniMax H3 导演台加速版全能工作流-宗门神曲多人替换演示_2084983882264436737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `ImageConcatMulti`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `ModelPreviewOverrideKJ`
- `Note Plus (mtb)`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `QRCode` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `UploadVideoToHost` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
