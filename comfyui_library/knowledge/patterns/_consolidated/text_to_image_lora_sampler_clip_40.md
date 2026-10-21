---
name: text_to_image_lora_sampler_clip_40
type: Text To Image
frequency: 17
level: strong
coverage: 0.879353
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Viggle 4-Step极速文生图工作流四步出图_2106210534201843714.json, 图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json, 图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json, 图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json, 图片生成/文生图/Qwen Image 2.1写实文生图｜图生图双模式 文生图质感稳定在线_2104101053124931586.json, 图片生成/文生图/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json, 图片生成/文生图/Qwen Image 2.1文生图 官方模板，原生2K高清文本到图像方案_2103550536535601154.json, 图片生成/文生图/Qwen Image 2.1文生图 高质量画面直出_2105349045723160578.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102103619591036930.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102510005793673217.json, 图片生成/文生图/Qwen Image 2.1文生图官方工作流BF16版处理生成工具_2102484931288068098.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2103558268332363777.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2107518180074807297.json, 图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json, 图片生成/文生图/Qwen Image 2.1文生图标准版 高质量画面稳定出图_2105033394219474945.json, 图片生成/文生图/千问2.1文生图片支持透明底｜文生图海报制作 商品换背景好帮手_2104051581292466177.json, 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Viggle 4-Step极速文生图工作流四步出图_2106210534201843714.json、图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json、图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json、图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json、图片生成/文生图/Qwen Image 2.1写实文生图｜图生图双模式 文生图质感稳定在线_2104101053124931586.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 15/17 个有
- `SaveImageAdvanced` —— 11/17 个有
- `PrimitiveStringMultiline` —— 7/17 个有
- `QwenImage21Cache` —— 7/17 个有
- `ModelAttentionBackend` —— 4/17 个有
- `PreviewAny` —— 4/17 个有
- `LoadImage` —— 3/17 个有
- `TextGenerate` —— 3/17 个有
- `CR Text` —— 2/17 个有
- `ComfySwitchNode` —— 2/17 个有
- `ModelSamplingFlux` —— 1/17 个有
- `PathchSageAttentionKJ` —— 1/17 个有
- `RH_LLMAPI_Pro_Node` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
