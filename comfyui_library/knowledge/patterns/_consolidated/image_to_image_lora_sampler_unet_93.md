---
name: image_to_image_lora_sampler_unet_93
type: Image To Image
frequency: 7
level: strong
coverage: 0.973
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/删除人物保留衣服_2006911696627048449.json, 图片生成/图生图/单图多角度_2073899870544551938.json, 图片生成/图生图/商业级万物提取-鞋子+帽子+裤子+挂饰+包包+衣服提取工作流（Qwen2511加速版）_2004439988181889026.json, 图片生成/图生图/老照片修复qwen2511千问2511加速版_2003646847212265474.json, 图片生成/图生图/衣服提取衣服_2058616474121625602.json, 图片生成/图生图/衣服提取衣服qwen2511千问2511加速版_2004402979652468737.json, 图片生成/图生图/豆包图片去水印_高清修复_2082761030039588866.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_93

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/删除人物保留衣服_2006911696627048449.json、图片生成/图生图/单图多角度_2073899870544551938.json、图片生成/图生图/商业级万物提取-鞋子+帽子+裤子+挂饰+包包+衣服提取工作流（Qwen2511加速版）_2004439988181889026.json、图片生成/图生图/老照片修复qwen2511千问2511加速版_2003646847212265474.json、图片生成/图生图/衣服提取衣服_2058616474121625602.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
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
- `ReferenceLatent` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `ImageConcanate` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `FluxKontextImageScale` —— 2/7 个有
- `GenerateNoise` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `LGNoiseInjectionLatent` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `QwenMultiangleCameraNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
