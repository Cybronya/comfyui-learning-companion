---
name: unknown_workflow_video_sampler_clip_118
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8804
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Remix首尾帧生视频动态模型-官方工作流_2011093205202247682.json, 视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json, 视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json, 视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_2030191511907864578.json, 视频生成/图生视频/图生视频 _ 高动态 _ wan smooth_1988988553113776129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Remix首尾帧生视频动态模型-官方工作流_2011093205202247682.json、视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json、视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json、视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_2030191511907864578.json、视频生成/图生视频/图生视频 _ 高动态 _ wan smooth_1988988553113776129.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanFirstLastFrameToVideo` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `ImageResize+` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `JWInteger` —— 2/5 个有
- `MultiplePathsInput` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `wanBlockSwap` —— 2/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
