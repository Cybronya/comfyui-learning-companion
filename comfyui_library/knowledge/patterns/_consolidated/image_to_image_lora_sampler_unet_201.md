---
name: image_to_image_lora_sampler_unet_201
type: Image To Image
frequency: 4
level: strong
coverage: 0.97
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/双图像输入千问编辑_1959814190741532674.json, 平台全量/真人转-可爱Q版卡通ip形象 qwen edit 一键Chibi角色风格转换+Q版风格化_1994315901975592962.json, 平台全量/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053866201029324801.json, 平台全量/（qwen_klein）服装提取工作流_2061323496176832513.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_201

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/双图像输入千问编辑_1959814190741532674.json、平台全量/真人转-可爱Q版卡通ip形象 qwen edit 一键Chibi角色风格转换+Q版风格化_1994315901975592962.json、平台全量/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053866201029324801.json、平台全量/（qwen_klein）服装提取工作流_2061323496176832513.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `CR Simple Image Compare` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `Resolutions by Ratio (WLSH)` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 8 | 4 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
