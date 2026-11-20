---
name: image_to_image_lora_sampler_unet_177
type: Image To Image
frequency: 4
level: strong
coverage: 0.9675
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929.json, 图片生成/图生图/qwen Edit 2511 单图编辑+修改表情_2059458819733942274.json, 图片生成/图生图/二次元图片转真人Qwen_1977227595215458305.json, 图片生成/图生图/商业级万物提取-鞋子+帽子+裤子+挂饰+包包+衣服提取工作流（Qwen2511加速版）_2004439988181889026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929.json、图片生成/图生图/qwen Edit 2511 单图编辑+修改表情_2059458819733942274.json、图片生成/图生图/二次元图片转真人Qwen_1977227595215458305.json、图片生成/图生图/商业级万物提取-鞋子+帽子+裤子+挂饰+包包+衣服提取工作流（Qwen2511加速版）_2004439988181889026.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
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
- `CFGNorm` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `PixelSmileConditioning` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CustomAddLabel` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Float` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
