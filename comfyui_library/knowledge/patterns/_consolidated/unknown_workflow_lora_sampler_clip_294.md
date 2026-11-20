---
name: unknown_workflow_lora_sampler_clip_294
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoConditionOnly, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.5 - CQ Enhancer lora for images 图像高清修复放大工具-RH_2100842979803095041.json, 图片生成/图生图/Workflow_LTX2.5 - CQ Enhancer lora for images.json_2100773980268490754.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_294

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/LTX2.5 - CQ Enhancer lora for images 图像高清修复放大工具-RH_2100842979803095041.json、图片生成/图生图/Workflow_LTX2.5 - CQ Enhancer lora for images.json_2100773980268490754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoConditionOnly`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `KOOK_SaveJPGImage` —— 1/2 个有
- `LG_Color_Match_V2` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
