---
name: unknown_workflow_sampler_clip_unet_263
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9926
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2.0图生图_1994969105419657218.json, 图片生成/图生图/flux2_klein双图编辑_2038872372450697217.json, 图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json, 图片生成/图生图/【遇见AI】FLUX2-klein-4b，图像编辑_2012010188076748802.json, 图片生成/图生图/【遇见AI】FLUX2-klein-9b，图像编辑_2012018380978524162.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_263

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux2.0图生图_1994969105419657218.json、图片生成/图生图/flux2_klein双图编辑_2038872372450697217.json、图片生成/图生图/【遇见AI】FLUX2-klein-4b，spritesheet四视图，fal版lora_2014170035505340418.json、图片生成/图生图/【遇见AI】FLUX2-klein-4b，图像编辑_2012010188076748802.json、图片生成/图生图/【遇见AI】FLUX2-klein-9b，图像编辑_2012018380978524162.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
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
- `BasicGuider` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `ImpactImageInfo` —— 3/5 个有
- `EmptyFlux2LatentImage` —— 2/5 个有
- `CFGGuider` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `Width/Height Literal` —— 1/5 个有
- `Width/Height Literal (Image Saver)` —— 1/5 个有
- `easy imageScaleDown` —— 1/5 个有
- `孤海图像缩放按像素` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.1 | - | 1 | 100% |
| LoRA 文本强度 | 1.1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
