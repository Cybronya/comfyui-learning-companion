---
name: unknown_workflow_sampler_clip_unet_351
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.766667
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, JjkText, KSamplerSelect, LoadImage, RH_LLMAPI_NODE, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/两个角色合影Kontext-DEV开源ComfyUI官方版_1938854784072142849.json, 图片生成/图生图/图片水印移除Kontext-DEV开源ComfyUI官方版_2089558568663076865.json, 图片生成/图生图/图片水印移除Kontext-DEV开源ComfyUI官方版_2090097090373447681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_351

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/两个角色合影Kontext-DEV开源ComfyUI官方版_1938854784072142849.json、图片生成/图生图/图片水印移除Kontext-DEV开源ComfyUI官方版_2089558568663076865.json、图片生成/图生图/图片水印移除Kontext-DEV开源ComfyUI官方版_2090097090373447681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
