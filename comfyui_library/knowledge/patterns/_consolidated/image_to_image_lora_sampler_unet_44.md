---
name: image_to_image_lora_sampler_unet_44
type: Image To Image
frequency: 11
level: strong
coverage: 0.935091
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit IClight服务端_1959118992034181121.json, 图片生成/图生图/Qwen edit一句话Q版改写实_1958805864788418561.json, 图片生成/图生图/Qwen edit一句话改变图片_1958535559591391233.json, 图片生成/图生图/Qwen edit一句话老照片修复服务端_1958737882548760578.json, 图片生成/图生图/Qwen edit产品精修_1959184380298211330.json, 图片生成/图生图/Qwen edit高清修复服务端_1959056991652098050.json, 图片生成/图生图/Qwen-动漫转真人-百万像素_2000487022429077506.json, 图片生成/图生图/Qwen-动漫转真人_1992896735680983041.json, 图片生成/图生图/qwen-edit-plus一键换装（最强编辑）_1970796555513065473.json, 图片生成/图生图/千问Qwen edit一段话文生图高精度bf16_2000496512356544513.json, 图片生成/文生图/25.8.22 Qwen edit一段话任意改变图片_1958882089787666433.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_44

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen edit IClight服务端_1959118992034181121.json、图片生成/图生图/Qwen edit一句话Q版改写实_1958805864788418561.json、图片生成/图生图/Qwen edit一句话改变图片_1958535559591391233.json、图片生成/图生图/Qwen edit一句话老照片修复服务端_1958737882548760578.json、图片生成/图生图/Qwen edit产品精修_1959184380298211330.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio` —— 10/11 个有
- `CR Text` —— 8/11 个有
- `RepeatLatentBatch` —— 8/11 个有
- `Image Comparer (rgthree)` —— 5/11 个有
- `ResizeLongestToNode` —— 5/11 个有
- `easy imageConcat` —— 5/11 个有
- `ImageConcanate` —— 4/11 个有
- `TextEncodeQwenImageEditPlus` —— 3/11 个有
- `CFGNorm` —— 1/11 个有
- `Seed_` —— 1/11 个有
- `Text` —— 1/11 个有
- `easy imageScaleDownToSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
