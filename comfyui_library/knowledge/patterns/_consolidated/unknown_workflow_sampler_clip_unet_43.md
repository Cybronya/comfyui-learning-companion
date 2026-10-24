---
name: unknown_workflow_sampler_clip_unet_43
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.870412
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein 局部重绘+全节点注释_2061408975094112257.json, 图片生成/图生图/【ComfyUI】Klein单图精修工作流｜提示词驱动渲染+全节点注释_2061341398959476737.json, 图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json, 图片生成/图生图/【遇见AI】FLUX2-klein-4b，图像编辑_2012010188076748802.json, 图片生成/图生图/【遇见AI】FLUX2-klein-9b，图像编辑_2012018380978524162.json, 图片生成/图生图/嘟嘟-Flux2单图编辑_1994408022388641794.json, 图片生成/图生图/👾怪獸-FLUX.2单图编辑👾_1993647875032891394.json, 图片生成/图生图/👾怪獸-FLUX.2双图编辑👾_1993647975433961474.json, 图片生成/文生图/3D人物编辑器应用系列之二——FLUX-2-klein-9B文生图_2020299327251423234.json, 图片生成/文生图/FLUX-2-klein-9B_动作精准设计之二工作流_2016865671568691202.json, 图片生成/文生图/FLUX-2-klein-9b_动作精准设计之一工作流_2013405319954702338.json, 图片生成/文生图/FLUX2 混合模型_1993527380123860994.json, 图片生成/文生图/FLUX2-多参考一致性创意场景合成_2090769208387923969.json, 图片生成/文生图/Flux2 单图编辑_1993603003697610753.json, 图片生成/文生图/Flux2 文生图_1986239618842578945.json, 图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json, 图片生成/文生图/反差人设-剧场后台花絮_1999861137980223490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/klein 局部重绘+全节点注释_2061408975094112257.json、图片生成/图生图/【ComfyUI】Klein单图精修工作流｜提示词驱动渲染+全节点注释_2061341398959476737.json、图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json、图片生成/图生图/【遇见AI】FLUX2-klein-4b，图像编辑_2012010188076748802.json、图片生成/图生图/【遇见AI】FLUX2-klein-9b，图像编辑_2012018380978524162.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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
- `FluxGuidance` —— 16/17 个有
- `EmptyFlux2LatentImage` —— 13/17 个有
- `ImageScaleToTotalPixels` —— 11/17 个有
- `CR Prompt Text` —— 7/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/17 个有
- `ImpactImageInfo` —— 3/17 个有
- `PrimitiveInt` —— 3/17 个有
- `INTConstant` —— 2/17 个有
- `INPAINT_ExpandMask` —— 1/17 个有
- `InpaintModelConditioning` —— 1/17 个有
- `Int` —— 1/17 个有
- `LoraLoader` —— 1/17 个有
- `ModelPatchTorchSettings` —— 1/17 个有
- `PathchSageAttentionKJ` —— 1/17 个有
- `TTResolutionSelector` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.1 | - | 1 | 100% |
| LoRA 文本强度 | 1.1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
