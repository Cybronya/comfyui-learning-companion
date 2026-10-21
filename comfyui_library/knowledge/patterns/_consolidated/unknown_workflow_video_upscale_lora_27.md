---
name: unknown_workflow_video_upscale_lora_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.926
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyHunyuanLatentVideo, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, HunyuanVideoLoraLoader, ImageScale, ImageUpscaleWithModel, KSamplerSelect, MathExpression|pysssss, ModelSamplingSD3, RandomNoise, SaveAnimatedWEBP, TeaCacheHunyuanVideoSampler_FOK, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/混元视频.适用于低 VRAM + 升频器_1897293180122157057.json, 视频生成/文生视频/1897293180122157057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/混元视频.适用于低 VRAM + 升频器_1897293180122157057.json、视频生成/文生视频/1897293180122157057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `HunyuanVideoLoraLoader`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `RandomNoise`
- `SaveAnimatedWEBP`
- `TeaCacheHunyuanVideoSampler_FOK`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | double_blocks | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 最常用 double_blocks，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
