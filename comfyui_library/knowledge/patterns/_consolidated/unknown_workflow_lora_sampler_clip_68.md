---
name: unknown_workflow_lora_sampler_clip_68
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.85075
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json, 图片生成/图生图/人脸纹理细节（自然，橙黄色版）_2070005207978827778.json, 图片生成/图生图/人脸纹理细节（超自然、轻纹理）_2072296887910232066.json, 图片生成/图生图/真实人脸纹理细节_2080879332058288129.json, 图片生成/图生图/真实人脸纹理细节_2116396811941408770.json, 平台全量/FLUX-2 Klein & RMBG 2.0 主体背景一键分离｜自动识别主体扣图_2088086199658442754.json, 平台全量/FLUX-2 Klein & Sam3 主体背景一键分离｜语义分割主体扣图_2088096230055432194.json, 平台全量/加强脸部纹理细节V3.5_2099746457011183618.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json、图片生成/图生图/人脸纹理细节（自然，橙黄色版）_2070005207978827778.json、图片生成/图生图/人脸纹理细节（超自然、轻纹理）_2072296887910232066.json、图片生成/图生图/真实人脸纹理细节_2080879332058288129.json、图片生成/图生图/真实人脸纹理细节_2116396811941408770.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 6/8 个有
- `Int` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `Float` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `Fast Groups Muter (rgthree)` —— 3/8 个有
- `LayerMask: MaskGrow` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `ThresholdMask` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `AILab_MaskOverlay` —— 2/8 个有
- `GetImageSize+` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `LayerMask: BiRefNetUltraV2` —— 2/8 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/8 个有
- `RH_Translator` —— 1/8 个有
- `SDVN Overlay Mask Color Image` —— 1/8 个有
- `easy sam3ImageSegmentation` —— 1/8 个有
- `easy sam3ModelLoader` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
