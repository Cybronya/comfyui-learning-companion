---
name: unknown_workflow_lora_sampler_clip_185
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoConditionOnly, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.5 - CQ Enhancer lora for images 图像高清修复放大工具-RH_2100842979803095041.json, 图片生成/图生图/Workflow_LTX2.5 - CQ Enhancer lora for images.json_2100773980268490754.json, 数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/LTX2.5 - CQ Enhancer lora for images 图像高清修复放大工具-RH_2100842979803095041.json、图片生成/图生图/Workflow_LTX2.5 - CQ Enhancer lora for images.json_2100773980268490754.json、数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ImpactInt` —— 2/3 个有
- `LG_Color_Match_V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `FL_Switch` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KOOK_SaveJPGImage` —— 1/3 个有
- `LTXVAudioVAEDecode` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LTXVEmptyLatentAudio` —— 1/3 个有
- `LTXVSeparateAVLatent` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
