---
name: unknown_workflow_lora_sampler_unet_270
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.905
common_nodes: [CLIPLoader, CR Prompt Text, Cut By Mask, Image Comparer (rgthree), InvertMask (segment anything), KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, MaskToImage, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UC_ImagePad, UNETLoader, VAEDecode, VAELoader, 图像缩放V2_孤海, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1光影溶图_2104916372500340738.json, 图片生成/图生图/Qwen-Image-2.1纠正背景透视溶图_2106759126654218241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_270

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1光影溶图_2104916372500340738.json、图片生成/图生图/Qwen-Image-2.1纠正背景透视溶图_2106759126654218241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `Cut By Mask`
- `Image Comparer (rgthree)`
- `InvertMask (segment anything)`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UC_ImagePad`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `图像缩放V2_孤海`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 1/2 个有
- `MaskPreview` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 26 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 26，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 26，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
