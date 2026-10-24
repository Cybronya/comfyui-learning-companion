---
name: image_to_image_sampler_unet_vae_52
type: Image To Image
frequency: 3
level: strong
coverage: 0.847
common_nodes: [CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, ImageConcanate, KSampler, LoadImage, PreviewImage, RH_LLMAPI_NODE, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1971122834372206593.json, 图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1984428089918832641.json, 图片生成/图生图/Qwen-Edit-2509 CN 控制参考，图像编辑_1971156046700023809.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_52

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1971122834372206593.json、图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1984428089918832641.json、图片生成/图生图/Qwen-Edit-2509 CN 控制参考，图像编辑_1971156046700023809.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
