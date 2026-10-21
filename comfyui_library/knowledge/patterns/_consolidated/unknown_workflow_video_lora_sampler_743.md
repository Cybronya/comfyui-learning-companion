---
name: unknown_workflow_video_lora_sampler_743
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.867
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageBatch, ImageScaleToMegapixels, ImageStitch, ImageToMask, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, RepeatImageBatch, SolidMask, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1966707596608647169.json, 视频生成/图生视频/1980133936569421825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_743

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1966707596608647169.json、视频生成/图生视频/1980133936569421825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageBatch`
- `ImageScaleToMegapixels`
- `ImageStitch`
- `ImageToMask`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `RepeatImageBatch`
- `SolidMask`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 3.5 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
