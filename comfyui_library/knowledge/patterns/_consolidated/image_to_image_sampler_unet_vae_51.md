---
name: image_to_image_sampler_unet_vae_51
type: Image To Image
frequency: 5
level: strong
coverage: 0.9272
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Imgae Edit任意产品纹理提取与纹理迁移工作流_2066960213785268225.json, 图片生成/图生图/Qwen-Image-Edit 2509-模特分镜多角度_1987910970393694209.json, 图片生成/图生图/雪11.tonnie-2155打光lora_2012115137938857986.json, 平台全量/Qwen Edit 人物多视角12连出图 （着重脸部与全身出图）（动漫 真人都可以）_2067645021679083522.json, 平台全量/影视人物资产生成 人物特写  正 侧 背面全身一键出图（动漫 真人都可以）开源版_2101821078501941250.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Imgae Edit任意产品纹理提取与纹理迁移工作流_2066960213785268225.json、图片生成/图生图/Qwen-Image-Edit 2509-模特分镜多角度_1987910970393694209.json、图片生成/图生图/雪11.tonnie-2155打光lora_2012115137938857986.json、平台全量/Qwen Edit 人物多视角12连出图 （着重脸部与全身出图）（动漫 真人都可以）_2067645021679083522.json、平台全量/影视人物资产生成 人物特写  正 侧 背面全身一键出图（动漫 真人都可以）开源版_2101821078501941250.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `ImpactInt` —— 3/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `Image Lucy Sharpen` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LatentUpscale` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LayerColor: AutoAdjustV2` —— 1/5 个有
- `PixaromaLabel` —— 1/5 个有
- `easy getNode` —— 1/5 个有
- `easy setNode` —— 1/5 个有
- `孤海图像组合批次` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（20/5 个样本）：Steps较低可能导致细节不足
