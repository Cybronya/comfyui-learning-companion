---
name: unknown_workflow_sampler_clip_unet_222
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.878
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2文生图工作流--直出2K_1926661482686353410.json, 图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json, 图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json, 图片生成/文生图/image_flux2_1999252927225229314.json, 图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json, 图片生成/文生图/最强开源 FLUX2系列合集_1993708586574479361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_222

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Flux2文生图工作流--直出2K_1926661482686353410.json、图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json、图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json、图片生成/文生图/image_flux2_1999252927225229314.json、图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `ModelPatchTorchSettings` —— 3/6 个有
- `VAEEncode` —— 3/6 个有
- `ApplySageAttention` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
