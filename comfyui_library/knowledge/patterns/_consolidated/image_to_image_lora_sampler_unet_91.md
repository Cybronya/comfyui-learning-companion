---
name: image_to_image_lora_sampler_unet_91
type: Image To Image
frequency: 7
level: strong
coverage: 0.862143
common_nodes: [CFGNorm, CLIPLoader, CR Text, Compare, GetImageSize, ImageResize+, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【双向补齐-故事分镜制作V2】全能图片pro-qwen 2509（关键帧叙事法）_1986024758141747201.json, 图片生成/图生图/【故事分镜制作】qwen-Edit-2509（next sceneV2）_1983000935146356738.json, 图片生成/图生图/【故事分镜制作】qwen-Edit-2509（next sceneV2）高清、光影、唯美的不二选择！_2034085594611060737.json, 图片生成/图生图/【故事分镜制作】qwen-Edit-2509（next sceneV2）高清、光影、唯美的不二选择！_2041160207996297218.json, 图片生成/图生图/千问【故事分镜制作】图生图工作流_1992872342263230466.json, 图片生成/图生图/双向分镜故事链_1994343795951083521.json, 视频生成/图生视频/【故事分镜制作】qwen-Edit-2509_2015966817742753793.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_91

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/【双向补齐-故事分镜制作V2】全能图片pro-qwen 2509（关键帧叙事法）_1986024758141747201.json、图片生成/图生图/【故事分镜制作】qwen-Edit-2509（next sceneV2）_1983000935146356738.json、图片生成/图生图/【故事分镜制作】qwen-Edit-2509（next sceneV2）高清、光影、唯美的不二选择！_2034085594611060737.json、图片生成/图生图/【故事分镜制作】qwen-Edit-2509（next sceneV2）高清、光影、唯美的不二选择！_2041160207996297218.json、图片生成/图生图/千问【故事分镜制作】图生图工作流_1992872342263230466.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `Compare`
- `GetImageSize`
- `ImageResize+`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 5/7 个有
- `EmptyLatentImage` —— 2/7 个有
- `FluxResolutionNode` —— 2/7 个有
- `RH_Nano_Banana2_Image2Image` —— 1/7 个有
- `RH_Nano_Banana_Image2Image` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
