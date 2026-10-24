---
name: image_to_image_sampler_vae_6
type: Image To Image
frequency: 15
level: moderate
coverage: 0.8796
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/B6、图像编辑 千问2.5 GGUF - 和风_1992879635685855234.json, 图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963555215508328450.json, 图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963568662437400578.json, 图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963550771471273985.json, 图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963563706520260610.json, 图片生成/图生图/KIWI-qwen-edit-产品精修_1963557059360952321.json, 图片生成/图生图/KIWI-qwen-edit-衣服提取_1963567265559171074.json, 图片生成/图生图/Nunchaku 4步 Qwen Edit 图像编辑_1966416216682377218.json, 图片生成/图生图/Nunchaku 8步加速 Qwen Edit 图像编辑_1966416545608052737.json, 图片生成/图生图/Nunchaku超级加速Qwen Edit 图像编辑_1966409148596465666.json, 图片生成/图生图/QWEN 2511 图像编辑 百万像素返图 _接入SDPPP 实现图像QWEN图像编辑_2073357158070181889.json, 图片生成/图生图/QWEN Edit plus 2509多图编辑功能极速生成（平替香蕉）_1988121202399014914.json, 图片生成/图生图/千问Edit2509图像编辑三图版_1972125442494885889.json, 图片生成/图生图/千问Edit2509图像编辑单图版_1972125938593034241.json, 图片生成/图生图/千问Edit2509图像编辑双图版_1972837097528860674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/B6、图像编辑 千问2.5 GGUF - 和风_1992879635685855234.json、图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963555215508328450.json、图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963568662437400578.json、图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963550771471273985.json、图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963563706520260610.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 14/15 个有
- `TextEncodeQwenImageEdit` —— 14/15 个有
- `LoraLoaderModelOnly` —— 12/15 个有
- `UNETLoader` —— 10/15 个有
- `JjkText` —— 8/15 个有
- `ImageConcanate` —— 7/15 个有
- `ImageConcatMulti` —— 7/15 个有
- `NunchakuQwenImageDiTLoader` —— 4/15 个有
- `TextEncodeQwenImageEditPlus` —— 4/15 个有
- `Display Any (rgthree)` —— 3/15 个有
- `Image Comparer (rgthree)` —— 3/15 个有
- `PreviewImage` —— 3/15 个有
- `RH_LLMAPI_NODE` —— 3/15 个有
- `easy anythingIndexSwitch` —— 3/15 个有
- `Anything Everywhere` —— 1/15 个有
- `DWPreprocessor` —— 1/15 个有
- `LayerUtility: ImageReel` —— 1/15 个有
- `LayerUtility: ImageReelComposit` —— 1/15 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `easy float` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 15 | 54% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 15 | 61% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
