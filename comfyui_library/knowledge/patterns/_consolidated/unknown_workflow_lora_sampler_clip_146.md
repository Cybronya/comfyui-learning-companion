---
name: unknown_workflow_lora_sampler_clip_146
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84575
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json, 图片生成/图生图/人脸纹理细节（自然，橙黄色版）_2070005207978827778.json, 图片生成/图生图/人脸纹理细节（超自然、轻纹理）_2072296887910232066.json, 图片生成/图生图/真实人脸纹理细节_2080879332058288129.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json、图片生成/图生图/人脸纹理细节（自然，橙黄色版）_2070005207978827778.json、图片生成/图生图/人脸纹理细节（超自然、轻纹理）_2072296887910232066.json、图片生成/图生图/真实人脸纹理细节_2080879332058288129.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `AILab_MaskOverlay` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/4 个有
- `LayerMask: MaskGrow` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `ThresholdMask` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
