---
name: unknown_workflow_sampler_clip_unet_282
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.79925
common_nodes: [Anything Everywhere3, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 换脸【基础流】_2017112299043037185.json, 图片生成/图生图/Klein 转写实【基础流】_2018227045939023874.json, 图片生成/图生图/Klein+LLM极速扩图【效果强】_2016684919459680257.json, 图片生成/图生图/Klein9b扩图工作流_(只支持2K尺寸)_2064244174521724929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_282

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Klein 换脸【基础流】_2017112299043037185.json、图片生成/图生图/Klein 转写实【基础流】_2018227045939023874.json、图片生成/图生图/Klein+LLM极速扩图【效果强】_2016684919459680257.json、图片生成/图生图/Klein9b扩图工作流_(只支持2K尺寸)_2064244174521724929.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `ShowText` —— 2/4 个有
- `ImageColorMatch+` —— 1/4 个有
- `ImitationHueNode` —— 1/4 个有
- `LayerMask: HumanPartsUltra` —— 1/4 个有
- `LayerMask: MaskGrow` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
