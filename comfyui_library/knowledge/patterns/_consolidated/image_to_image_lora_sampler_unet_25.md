---
name: image_to_image_lora_sampler_unet_25
type: Image To Image
frequency: 15
level: strong
coverage: 0.666533
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王018.单图 双图 三图编辑_2034661175719370753.json, 图片生成/图生图/251225001.002.Qwen-Edit-2511-支持 单图 双图 三图编辑_2004198351618928642.json, 图片生成/图生图/LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514.json, 图片生成/图生图/Qwen Image Edit 2511 合集_2004214649702805506.json, 图片生成/图生图/Qwen-2511单_双_三图编辑_2010241309461716993.json, 图片生成/图生图/Qwen-Edit-2511-单图+双图+三图编辑_2004033881311485953.json, 图片生成/图生图/Qwen-Edit-2511-支持 单图 双图 三图编辑_2003703615871197186.json, 图片生成/图生图/Qwen-Edit-2511-支持 单图 双图 三图编辑_2003752282514726913.json, 图片生成/图生图/Qwen-Edit-2511-支持 单图 双图 三图编辑_2042169776323170305.json, 图片生成/图生图/Qwen-Edit-2511-支持 单图 双图 三图编辑_2062798695934021633.json, 图片生成/图生图/Qwen-Edit-2511单图编辑_2032022282889076737.json, 图片生成/图生图/Qwen-edit 简易一键3D皮克斯 Qwen-edit 简易一键3D皮克斯_2005154361963671553.json, 图片生成/图生图/Qwen-edit-2511 明星代言｜手持产品替换_2005156061877334017.json, 图片生成/图生图/最新的Qwenimage-Edit-升级版2511合集_2003763847158767617.json, 图片生成/图生图/老照片修复_2008934700944986113.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_25

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王018.单图 双图 三图编辑_2034661175719370753.json、图片生成/图生图/251225001.002.Qwen-Edit-2511-支持 单图 双图 三图编辑_2004198351618928642.json、图片生成/图生图/LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514.json、图片生成/图生图/Qwen Image Edit 2511 合集_2004214649702805506.json、图片生成/图生图/Qwen-2511单_双_三图编辑_2010241309461716993.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 14/15 个有
- `LayerUtility: ImageReel` —— 14/15 个有
- `LayerUtility: ImageReelComposit` —— 14/15 个有
- `PlaySound|pysssss` —— 14/15 个有
- `PreviewImage` —— 14/15 个有
- `Fast Groups Bypasser (rgthree)` —— 13/15 个有
- `ColorMatch` —— 1/15 个有
- `MemoryCleaner` —— 1/15 个有
- `RAMCleanup` —— 1/15 个有
- `VRAMCleanup` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 15 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 53% |
| 调度器 | simple | - | 15 | 53% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 41/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 53%
- 调度器 最常用 simple，15 个样本，一致性 53%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（41/15 个样本）：Steps较低可能导致细节不足
