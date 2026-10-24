---
name: unknown_workflow_video_sampler_clip_248
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [CLIPLoader, CLIPTextEncode, ImageBatch, ImageResize+, ImageToMask, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, MathExpression|pysssss, ModelSamplingSD3, PatchModelPatcherOrder, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, RepeatImageBatch, SolidMask, TorchCompileModelWanVideoV2, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1 fusionx vace 首尾帧 官方工作流（gguf版）_1937092855930458113.json, 视频生成/图生视频/首尾帧自动工作流WAN2.1+fusionx_1953295879823421441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_248

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.1 fusionx vace 首尾帧 官方工作流（gguf版）_1937092855930458113.json、视频生成/图生视频/首尾帧自动工作流WAN2.1+fusionx_1953295879823421441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageBatch`
- `ImageResize+`
- `ImageToMask`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `RepeatImageBatch`
- `SolidMask`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `TextBox` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
