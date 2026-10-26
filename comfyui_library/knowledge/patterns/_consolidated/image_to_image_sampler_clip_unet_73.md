---
name: image_to_image_sampler_clip_unet_73
type: Image To Image
frequency: 6
level: strong
coverage: 0.949167
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 产品专业打光｜电商_1947606970641670145.json, 图片生成/图生图/Kontext 角色一致性多角度_1950003872502865922.json, 图片生成/图生图/Kontext【一键】提取线稿，适合二创_1958351836795310082.json, 图片生成/图生图/flux 一键参考生成图像_1928839789221679106.json, 图片生成/图生图/好用的小工具-去除水印_1983138134869352449.json, 图片生成/文生图/芝麻街特效_2073346446350442497.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext 产品专业打光｜电商_1947606970641670145.json、图片生成/图生图/Kontext 角色一致性多角度_1950003872502865922.json、图片生成/图生图/Kontext【一键】提取线稿，适合二创_1958351836795310082.json、图片生成/图生图/flux 一键参考生成图像_1928839789221679106.json、图片生成/图生图/好用的小工具-去除水印_1983138134869352449.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `RH_Translator` —— 4/6 个有
- `LoraLoader` —— 2/6 个有
- `ShowText` —— 2/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: ImageScaleRestore` —— 1/6 个有
- `PDIMAGE_LongerSize` —— 1/6 个有
- `PIP_图像联结` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
