---
name: unknown_workflow_video_sampler_clip_229
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.923
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DuckHideNode, FL_RIFE, Fast Groups Bypasser (rgthree), ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanImageToVideo, WanMoeKSampler]
problems: []
missing: []
members: [视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频&音频_2058439942333886465.json, 视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频_2056998498276569090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_229

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频&音频_2058439942333886465.json、视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频_2056998498276569090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DuckHideNode`
- `FL_RIFE`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanImageToVideo`
- `WanMoeKSampler`

**可变部分**（部分 workflow 才有）：
- `HunyuanVideoFoley` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | increment | - | 2 | 100% |
| Prompt 约束强度(CFG) | 16 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler_ancestral | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 increment，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 16，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
