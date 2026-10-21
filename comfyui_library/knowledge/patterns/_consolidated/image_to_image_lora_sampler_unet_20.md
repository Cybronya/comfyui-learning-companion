---
name: image_to_image_lora_sampler_unet_20
type: Image To Image
frequency: 5
level: weak
coverage: 0.764
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2.最强编辑融合，单图，双图，三图编辑qwen_image_edit_2511_2066121923188322306.json, 图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json, 图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json, 图片生成/文生图/Qwen_Image_Edit图像编辑模型_2105216109094981633.json, 图片生成/文生图/可视化多角度摄像头控制2511_2010974579350577153.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/2.最强编辑融合，单图，双图，三图编辑qwen_image_edit_2511_2066121923188322306.json、图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json、图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json、图片生成/文生图/Qwen_Image_Edit图像编辑模型_2105216109094981633.json、图片生成/文生图/可视化多角度摄像头控制2511_2010974579350577153.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `Switch any [Crystools]` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 5 | 31% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 5 | 48% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，5 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，5 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
