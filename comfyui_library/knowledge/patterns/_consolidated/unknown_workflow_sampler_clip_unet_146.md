---
name: unknown_workflow_sampler_clip_unet_146
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.95225
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, ManualSigmas, RandomNoise, ReferenceMultiLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX3 KLEIN--工作流合集_2111157512895549441.json, 图片生成/图生图/FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306.json, 图片生成/图生图/Flux3 Amumu 图像编辑邪修_2110875194008096769.json, 图片生成/图生图/Flux3加速版多图编辑-sd-int8_2111151836345491457.json, 图片生成/图生图/Flux3多图编辑加速版_2111354552862728193.json, 图片生成/图生图/（4图 可以上满4张最少可以上传1张）Flux3多图编辑加速版_2111603711633092609.json, 图片生成/文生图/FLUX3 KLEIN--工作流合集_2111003999917924353.json, 图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX3 KLEIN--工作流合集_2111157512895549441.json、图片生成/图生图/FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306.json、图片生成/图生图/Flux3 Amumu 图像编辑邪修_2110875194008096769.json、图片生成/图生图/Flux3加速版多图编辑-sd-int8_2111151836345491457.json、图片生成/图生图/Flux3多图编辑加速版_2111354552862728193.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ReferenceMultiLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/8 个有
- `MuyeTextEditOutput` —— 4/8 个有
- `忽略多组孤海` —— 4/8 个有
- `ResolutionSelector` —— 3/8 个有
- `Text` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `llama_cpp_instruct_adv` —— 2/8 个有
- `llama_cpp_model_loader` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `QwenPERewriteT8` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
