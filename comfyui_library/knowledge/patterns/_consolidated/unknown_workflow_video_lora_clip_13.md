---
name: unknown_workflow_video_lora_clip_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9365
common_nodes: [CLIPLoader, CLIPTextEncode, Float, INTConstant, ImageResizeKJv2, JjkText, LayerUtility: ImageScaleRestore V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingSD3, PathchSageAttentionKJ, RHHiddenNodes, UNETLoader, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/数字人wan2.2首尾帧+infinitetalk说话_唱歌 对口型（真人_动漫_拟人态）_1962143850557063170.json, 视频生成/图生视频/数字人稳定版-Infinitetalk+wan2.2首尾帧视频生成_1927213525364592641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/数字人wan2.2首尾帧+infinitetalk说话_唱歌 对口型（真人_动漫_拟人态）_1962143850557063170.json、视频生成/图生视频/数字人稳定版-Infinitetalk+wan2.2首尾帧视频生成_1927213525364592641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Float`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `LayerUtility: ImageScaleRestore V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RHHiddenNodes`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AudioEncoderLoader` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
