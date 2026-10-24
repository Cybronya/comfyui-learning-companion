---
name: image_to_image_sampler_clip_unet_51
type: Image To Image
frequency: 8
level: strong
coverage: 0.93125
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片编辑_2088607792931360770.json, 图片生成/图生图/基础kontext工作流_2005321098000560130.json, 图片生成/图生图/好用的小工具-去除水印_1983138134869352449.json, 图片生成/图生图/情侣Q版转绘淘宝转绘_2057721392849838081.json, 图片生成/图生图/旧照片精准修复+放大_1992858360515022850.json, 图片生成/图生图/溶图 色彩变动小_Kontext_2064292965186621441.json, 图片生成/图生图/真人转水彩画风格 - Kontext 一键转绘_1945351279969488898.json, 图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/图片编辑_2088607792931360770.json、图片生成/图生图/基础kontext工作流_2005321098000560130.json、图片生成/图生图/好用的小工具-去除水印_1983138134869352449.json、图片生成/图生图/情侣Q版转绘淘宝转绘_2057721392849838081.json、图片生成/图生图/旧照片精准修复+放大_1992858360515022850.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `FluxKontextImageScale` —— 7/8 个有
- `LoraLoader` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `RH_Translator` —— 4/8 个有
- `ImageUpscaleWithModel` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `UpscaleModelLoader` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `RMBG` —— 2/8 个有
- `easy imageConcat` —— 2/8 个有
- `CR Latent Batch Size` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `TT_img_enc` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.925 | 0.8 - 1 | 6 | 91% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 6 | 92% |
| 采样步数 | 20 | 20 - 25 | 8 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.925，观测区间 0.8 - 1，6 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 92%）
- 采样步数 中位数 20，观测区间 20 - 25，8 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
