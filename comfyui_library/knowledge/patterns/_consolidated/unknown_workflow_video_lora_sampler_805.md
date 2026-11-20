---
name: unknown_workflow_video_lora_sampler_805
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9435
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3 角色替换_2092994502658183169.json, 数字人/数字人/仅换头_自动时长宽高_H3_2110546203753672706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_805

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/MinimaxH3 角色替换_2092994502658183169.json、数字人/数字人/仅换头_自动时长宽高_H3_2110546203753672706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
