---
name: image_to_image_lora_sampler_vae_6
type: Image To Image
frequency: 11
level: strong
coverage: 0.832
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Meitu   Qwen2509 更好的一致性_1981217441818771457.json, 图片生成/图生图/Nunchaku Qwen Edit 8步极速图像编辑V1_1965770098017505282.json, 图片生成/图生图/QWEN Edit plus 2509单图编辑功能极速生成（平替香蕉）_1988110170234449922.json, 图片生成/图生图/QWEN image edit 引导版工作流      附详细的多图像范例_1975862522542731265.json, 图片生成/图生图/Qwen Image  Edit 2511 三工作流组合（指引版本）_2004049715199131650.json, 图片生成/图生图/Qwen2509 Meitu版 一致性更好_1982409209759309825.json, 图片生成/图生图/Qwen2509_2002940398152609794.json, 图片生成/图生图/QwenEditPlus2509单双三图_1986908950937407489.json, 图片生成/图生图/（自用）Qwen Edit8步加速版3（换装前置）_1965423190451343362.json, 图片生成/文生图/QWEN Edit plus 2509三工作流组合（指引版本） 附详细的多图像范例及提示词模板_1975091649036595202.json, 图片生成/文生图/Qwen-Image_字体直出_字体设计_书法字体_综艺字体_海报生成QwenEdit_1982996678984773634.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Meitu   Qwen2509 更好的一致性_1981217441818771457.json、图片生成/图生图/Nunchaku Qwen Edit 8步极速图像编辑V1_1965770098017505282.json、图片生成/图生图/QWEN Edit plus 2509单图编辑功能极速生成（平替香蕉）_1988110170234449922.json、图片生成/图生图/QWEN image edit 引导版工作流      附详细的多图像范例_1975862522542731265.json、图片生成/图生图/Qwen Image  Edit 2511 三工作流组合（指引版本）_2004049715199131650.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 9/11 个有
- `PreviewImage` —— 8/11 个有
- `ConditioningZeroOut` —— 7/11 个有
- `TextEncodeQwenImageEdit` —— 7/11 个有
- `UNETLoader` —— 7/11 个有
- `NunchakuQwenImageDiTLoader` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/11 个有
- `CR Prompt Text` —— 3/11 个有
- `DWPreprocessor` —— 3/11 个有
- `Fast Groups Muter (rgthree)` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `MuyeTextEditOutput` —— 3/11 个有
- `TT_img_enc` —— 2/11 个有
- `CLIPTextEncode` —— 1/11 个有
- `CR SDXL Aspect Ratio` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 64% |
| 调度器 | simple | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 64%
- 调度器 最常用 simple，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（20/11 个样本）：Steps较低可能导致细节不足
