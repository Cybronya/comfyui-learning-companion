---
name: image_to_image_sampler_unet_vae_15
type: Image To Image
frequency: 9
level: strong
coverage: 0.923667
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图_1948702291495460865.json, 图片生成/图生图/FLUX图生图_1994673031052206081.json, 图片生成/图生图/Flux  kontext 老照片修复_1940415172613926913.json, 图片生成/图生图/Flux Kontext  保持风格一键Teache加速扩图_1961480141107085314.json, 图片生成/图生图/KONTEXT -dev万能移除物品_1954813690525605889.json, 图片生成/图生图/Kontext基础编辑工作流_1948946546302824449.json, 图片生成/图生图/flux_kontext图像编辑_万物玻璃_1961470553272029186.json, 图片生成/图生图/图片编辑_2088607792931360770.json, 图片生成/图生图/情侣Q版转绘淘宝转绘_2057721392849838081.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX图生图_1948702291495460865.json、图片生成/图生图/FLUX图生图_1994673031052206081.json、图片生成/图生图/Flux  kontext 老照片修复_1940415172613926913.json、图片生成/图生图/Flux Kontext  保持风格一键Teache加速扩图_1961480141107085314.json、图片生成/图生图/KONTEXT -dev万能移除物品_1954813690525605889.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 7/9 个有
- `CLIPTextEncode` —— 6/9 个有
- `FluxKontextImageScale` —— 6/9 个有
- `LoraLoader` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `CLIPTextEncodeFlux` —— 3/9 个有
- `RMBG` —— 3/9 个有
- `DeepTranslatorTextNode` —— 2/9 个有
- `TeaCache` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `INPAINT_MaskedFill` —— 1/9 个有
- `ImagePadKJ` —— 1/9 个有
- `ImageStitch` —— 1/9 个有
- `ModelSamplingFlux` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.925 | 0.35 - 1 | 6 | 73% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 20 | 20 - 38 | 9 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 0.5 - 1 | 9 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.925，观测区间 0.35 - 1，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 38，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，9 个样本，取值集中（一致性 83%）
