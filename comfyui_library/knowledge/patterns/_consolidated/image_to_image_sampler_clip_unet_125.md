---
name: image_to_image_sampler_clip_unet_125
type: Image To Image
frequency: 5
level: strong
coverage: 0.9026
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SRPO重绘修复工作流——提升细节质感_2073084527190302722.json, 图片生成/图生图/【遇见AI】flux-kontext 单图编辑工作流_2050856923859308546.json, 图片生成/图生图/千府AI-FLUX Kontext 图片去水印工作流_1929384205183041538.json, 图片生成/图生图/好用的小工具-去除水印_1983138134869352449.json, 图片生成/图生图/提取产品-生成三视图（FLUX_Kontext）_1958816743533785089.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SRPO重绘修复工作流——提升细节质感_2073084527190302722.json、图片生成/图生图/【遇见AI】flux-kontext 单图编辑工作流_2050856923859308546.json、图片生成/图生图/千府AI-FLUX Kontext 图片去水印工作流_1929384205183041538.json、图片生成/图生图/好用的小工具-去除水印_1983138134869352449.json、图片生成/图生图/提取产品-生成三视图（FLUX_Kontext）_1958816743533785089.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
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
- `ReferenceLatent` —— 4/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `Image Resize To Width` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.5 - 1 | 5 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，5 个样本
