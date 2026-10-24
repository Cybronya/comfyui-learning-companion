---
name: text_to_image_lora_sampler_clip_310
type: Text To Image
frequency: 6
level: strong
coverage: 0.891667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1图像编辑 高质量改图方案稳定出图_2109379879476219906.json, 图片生成/图生图/Qwen2.1图像编辑工作流，官方图生图处理方案_2106439543493844993.json, 图片生成/图生图/Qwen2.1图像编辑无PE版，纯净图生图处理工作流方案_2103935662083895298.json, 图片生成/图生图/Qwen2.1图像编辑透明图专用版，图生图透明背景处理工具_2103974957599510529.json, 图片生成/图生图/Qwen2.1图像编辑高质量改图方案稳定出图 高质量改图方案_2109754729986347010.json, 图片生成/图生图/QwenImage2.1千问图像2.1任意姿态生成 人物姿态精准控制_2109699653339009025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_310

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen2.1图像编辑 高质量改图方案稳定出图_2109379879476219906.json、图片生成/图生图/Qwen2.1图像编辑工作流，官方图生图处理方案_2106439543493844993.json、图片生成/图生图/Qwen2.1图像编辑无PE版，纯净图生图处理工作流方案_2103935662083895298.json、图片生成/图生图/Qwen2.1图像编辑透明图专用版，图生图透明背景处理工具_2103974957599510529.json、图片生成/图生图/Qwen2.1图像编辑高质量改图方案稳定出图 高质量改图方案_2109754729986347010.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `Seed (rgthree)` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `StringToInt` —— 2/6 个有
- `Text` —— 2/6 个有
- `easy seed` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `StringConstantMultiline` —— 1/6 个有
- `easy loraStack` —— 1/6 个有
- `easy loraStackApply` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
