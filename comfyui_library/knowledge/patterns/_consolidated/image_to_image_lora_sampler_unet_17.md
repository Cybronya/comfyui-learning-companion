---
name: image_to_image_lora_sampler_unet_17
type: Image To Image
frequency: 20
level: weak
coverage: 0.8425
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen edit 2509 万物白底换背景+反推提示词_1997517208639193089.json, 图片生成/图生图/Meitu   Qwen2509 更好的一致性_1981217441818771457.json, 图片生成/图生图/Qwen-Edit-一键生成九宫格表情包_1980174598350213122.json, 图片生成/图生图/Qwen-Edit-人物提取衣服_1965793441999425537.json, 图片生成/图生图/Qwen-Edit-指尖触摸虚拟角色_1983534381887365121.json, 图片生成/图生图/Qwen-Edit-海的那边是什么_1983545460763893761.json, 图片生成/图生图/Qwen-Edit-科幻星空眼睛_1984170750527602690.json, 图片生成/图生图/Qwen-edit 超自然重打光_2054846333298724865.json, 图片生成/图生图/Qwen-edit_万物重打光_2099321308822724609.json, 图片生成/图生图/Qwen-edit_万物重打光_2099665295848861698.json, 图片生成/图生图/Qwen2509 Meitu版 一致性更好_1982409209759309825.json, 图片生成/图生图/Qwen2509_2002940398152609794.json, 图片生成/图生图/QwenEdit官方流改优图片编辑4步加速Lora 6步出图效果更佳_1958102515072061442.json, 图片生成/图生图/人像写真重打光_2076370520215474177.json, 图片生成/图生图/人像写真重打光_2077926058837504001.json, 图片生成/图生图/人像写真重打光_2077938985393020930.json, 平台全量/Qwen-edit 万物重打光_1931240660181909505.json, 平台全量/Qwen-edit 万物重打光_2098655613189447682.json, 平台全量/Qwen-edit 打光_2074256810613239809.json, 平台全量/Qwen千问-万物重打光 人物一致_2003746720003596289.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/反推提示词/Qwen edit 2509 万物白底换背景+反推提示词_1997517208639193089.json、图片生成/图生图/Meitu   Qwen2509 更好的一致性_1981217441818771457.json、图片生成/图生图/Qwen-Edit-一键生成九宫格表情包_1980174598350213122.json、图片生成/图生图/Qwen-Edit-人物提取衣服_1965793441999425537.json、图片生成/图生图/Qwen-Edit-指尖触摸虚拟角色_1983534381887365121.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 19/20 个有
- `ImageScaleToTotalPixels` —— 16/20 个有
- `PreviewImage` —— 14/20 个有
- `ConditioningZeroOut` —— 13/20 个有
- `ColorMatch` —— 11/20 个有
- `JjkText` —— 11/20 个有
- `LayerUtility: PurgeVRAM V2` —— 10/20 个有
- `Image Comparer (rgthree)` —— 9/20 个有
- `Fast Groups Bypasser (rgthree)` —— 4/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/20 个有
- `Canny` —— 3/20 个有
- `ModelPatchLoader` —— 3/20 个有
- `MuyeTextEditOutput` —— 3/20 个有
- `QwenImageDiffsynthControlnet` —— 3/20 个有
- `FluxKontextImageScale` —— 1/20 个有
- `JjkShowText` —— 1/20 个有
- `Qwen2.5VL` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 20 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 20 | 48% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，20 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，20 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（16/20 个样本）：Steps较低可能导致细节不足
