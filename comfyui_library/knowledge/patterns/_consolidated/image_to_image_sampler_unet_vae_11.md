---
name: image_to_image_sampler_unet_vae_11
type: Image To Image
frequency: 13
level: weak
coverage: 0.903231
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QIANWEN图像编辑_2088896217135800321.json, 图片生成/图生图/QWEN 2511 图像编辑 百万像素返图 _接入SDPPP 实现图像QWEN图像编辑_2073357158070181889.json, 图片生成/图生图/QWEN image edit 引导版工作流      附详细的多图像范例_1975862522542731265.json, 图片生成/图生图/QWen2509 单图简单编辑_1998227397973540865.json, 图片生成/图生图/Qwen Edit 4步 加速 图像编辑_1967372813134913537.json, 图片生成/图生图/Qwen Edit 8步加速 图像编辑_1967376109622976514.json, 图片生成/图生图/Qwen Edit 图像编辑_1966322447366696961.json, 图片生成/图生图/Qwen-Edit-毛绒绒饮料（冬季限定）_1980917424298049537.json, 图片生成/图生图/Qwen-Edit-生成爆款手办_1964950491358744577.json, 图片生成/图生图/Qwen-Image-Edit 2509-自动溶图+透视矫正_1987847089428344834.json, 图片生成/图生图/Qwen-Image-Edit 2509-自动溶图+透视矫正_1987858824298172417.json, 数字人/数字人/QWEN image edit_最新上睫毛终极版_ 许老师版_1985625300958621698.json, 数字人/数字人/qwenImage终极版万能生图_许老师版_1988925629787672578.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/QIANWEN图像编辑_2088896217135800321.json、图片生成/图生图/QWEN 2511 图像编辑 百万像素返图 _接入SDPPP 实现图像QWEN图像编辑_2073357158070181889.json、图片生成/图生图/QWEN image edit 引导版工作流      附详细的多图像范例_1975862522542731265.json、图片生成/图生图/QWen2509 单图简单编辑_1998227397973540865.json、图片生成/图生图/Qwen Edit 4步 加速 图像编辑_1967372813134913537.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 12/13 个有
- `LoraLoaderModelOnly` —— 11/13 个有
- `TextEncodeQwenImageEdit` —— 10/13 个有
- `Image Comparer (rgthree)` —— 9/13 个有
- `TextEncodeQwenImageEditPlus` —— 5/13 个有
- `JjkText` —— 4/13 个有
- `FastCanvas` —— 3/13 个有
- `FastCanvasTool` —— 3/13 个有
- `FluxKontextImageScale` —— 3/13 个有
- `ImageConcanate` —— 3/13 个有
- `NunchakuQwenImageDiTLoader` —— 3/13 个有
- `Anything Everywhere3` —— 2/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/13 个有
- `easy imageRemBg` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `Preview from image [Crystools]` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `easy float` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 13 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 13 | 50% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，13 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，13 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（12/13 个样本）：Steps较低可能导致细节不足
