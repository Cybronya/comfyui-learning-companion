---
name: image_to_image_sampler_vae_10
type: Image To Image
frequency: 11
level: moderate
coverage: 0.875909
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku 4步 Qwen Edit 图像编辑_1966416216682377218.json, 图片生成/图生图/Nunchaku 8步加速 Qwen Edit 图像编辑_1966416545608052737.json, 图片生成/图生图/Nunchaku Qwen Edit 8步极速图像编辑V1_1965770098017505282.json, 图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json, 图片生成/图生图/Nunchaku超级加速Qwen Edit 图像编辑_1966409148596465666.json, 图片生成/图生图/QWEN Edit plus 2509单图编辑功能极速生成（平替香蕉）_1988110170234449922.json, 图片生成/图生图/QWEN Edit plus 2509多图编辑功能极速生成（平替香蕉）_1988121202399014914.json, 图片生成/图生图/Qwen Image  Edit 2511 三工作流组合（指引版本）_2004049715199131650.json, 图片生成/图生图/QwenEditPlus2509单双三图_1986908950937407489.json, 图片生成/图生图/镜头转换工作流（可批量）-qwen_1990249628895506433.json, 图片生成/文生图/QWEN Edit plus 2509三工作流组合（指引版本） 附详细的多图像范例及提示词模板_1975091649036595202.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Nunchaku 4步 Qwen Edit 图像编辑_1966416216682377218.json、图片生成/图生图/Nunchaku 8步加速 Qwen Edit 图像编辑_1966416545608052737.json、图片生成/图生图/Nunchaku Qwen Edit 8步极速图像编辑V1_1965770098017505282.json、图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json、图片生成/图生图/Nunchaku超级加速Qwen Edit 图像编辑_1966409148596465666.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 9/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `Image Comparer (rgthree)` —— 6/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `JjkText` —— 5/11 个有
- `TextEncodeQwenImageEdit` —— 5/11 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 5/11 个有
- `DWPreprocessor` —— 4/11 个有
- `Fast Groups Muter (rgthree)` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `ImageConcanate` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `UNETLoader` —— 2/11 个有
- `TT_img_enc` —— 1/11 个有
- `TextEncodeQwenImageEditPlus` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 11 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 53% |
| 采样算法 | euler | - | 11 | 64% |
| 调度器 | simple | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，11 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 64%
- 调度器 最常用 simple，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（15/11 个样本）：Steps较低可能导致细节不足
