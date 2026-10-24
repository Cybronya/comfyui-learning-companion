---
name: unknown_workflow_lora_sampler_unet_239
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4125
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CR Text, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), FastUnsharpSharpen, GetImageSize, GetImagesFromBatchIndexed, GetNode, Image Comparer (rgthree), ImageScaleBy, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SaveVideo, SetNode, TextPreview, UNETLoader, VAEDecode, VAELoader, VRGDG_Music3ConditioningStrength, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, workflow>SeedVR2]
problems: []
missing: []
members: [图片生成/反推提示词/MinimaxH3 文生图、图生图、图像编辑三合一工作流（ByCC菜）_2106814779062054913.json, 视频生成/图生视频/MinimaxH3_文生图、图生图、图像编辑三合一工作流ByCC菜_2110204533308739585.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_239

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/MinimaxH3 文生图、图生图、图像编辑三合一工作流（ByCC菜）_2106814779062054913.json、视频生成/图生视频/MinimaxH3_文生图、图生图、图像编辑三合一工作流ByCC菜_2110204533308739585.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `FastUnsharpSharpen`
- `GetImageSize`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `SetNode`
- `TextPreview`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRGDG_Music3ConditioningStrength`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `workflow>SeedVR2`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
