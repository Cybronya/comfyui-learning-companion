---
name: text_to_image_lora_sampler_clip_254
type: Text To Image
frequency: 8
level: strong
coverage: 0.903125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2512商业商品摄影Lora 单品棚拍电商主图生成_2098659266436616193.json, 图片生成/图生图/Qwen image 2.1角色表生成 角色设定图生图处理工具_2113695669427982338.json, 图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2104686784390197250.json, 图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105067914251554817.json, 图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105446415681024002.json, 图片生成/图生图/Qwen-image2.1人像多角度生成｜图生图一套多机位素材_2104545126759620610.json, 图片生成/图生图/Qwen-image2.1最佳换头换脸｜图生图精准换脸不崩脸_2104521060145258498.json, 图片生成/图生图/qwen image 2.1角色表生成｜角色设定图批量产出参考模板_2113500742152708097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_254

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2512商业商品摄影Lora 单品棚拍电商主图生成_2098659266436616193.json、图片生成/图生图/Qwen image 2.1角色表生成 角色设定图生图处理工具_2113695669427982338.json、图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2104686784390197250.json、图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105067914251554817.json、图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105446415681024002.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `TextEncodeQwenImage21` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `QwenMultiangleCameraNode` —— 4/8 个有
- `easy promptList` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `QwenImage21Cache` —— 2/8 个有
- `easy promptLine` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `LoraLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（11/8 个样本）：Steps较低可能导致细节不足
