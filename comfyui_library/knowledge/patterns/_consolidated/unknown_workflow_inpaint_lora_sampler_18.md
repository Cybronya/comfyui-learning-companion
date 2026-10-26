---
name: unknown_workflow_inpaint_lora_sampler_18
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9028
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageCrop, InpaintModelConditioning, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewImage, SamplerCustom, SaveImage, SolidMask, SplitSigmas, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/ICE-Edit 图像编辑工作流_1920016452320169985.json, 图片生成/图生图/IcEdit Nomal Lora图像编辑循环工作流（非MOE）V1_1920075398585974786.json, 图片生成/图生图/IcEdit图像编辑100%成功率进阶工作流V1_1919593964804964354.json, 图片生成/图生图/IcEdit图像编辑工作流V1_1919950328412966914.json, 图片生成/图生图/【💫书墨】ICEdit-MoE-LoRA言出法随模型_1918240005108465665.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ICE-Edit 图像编辑工作流_1920016452320169985.json、图片生成/图生图/IcEdit Nomal Lora图像编辑循环工作流（非MOE）V1_1920075398585974786.json、图片生成/图生图/IcEdit图像编辑100%成功率进阶工作流V1_1919593964804964354.json、图片生成/图生图/IcEdit图像编辑工作流V1_1919950328412966914.json、图片生成/图生图/【💫书墨】ICEdit-MoE-LoRA言出法随模型_1918240005108465665.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `SolidMask`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `Float` —— 3/5 个有
- `PMRF` —— 3/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `Primitive string multiline [Crystools]` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
