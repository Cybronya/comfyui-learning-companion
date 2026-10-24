---
name: text_to_image_lora_sampler_clip_320
type: Text To Image
frequency: 6
level: strong
coverage: 0.809833
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Text_Box, EmptyLatentImage, GoohaiRatioAndResolution, GoohaiRouteBlocker, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json, 图片生成/文生图/Qwen Image 2.1文生图编辑一体化｜抠图扩图局部重绘多图融合｜全自动扩写提示词_2112121620461608962.json, 图片生成/文生图/Qwen Image 2.1文生多图像编辑一体化工作流，文生图图生图处理方案_2106487983930175490.json, 图片生成/文生图/Qwen-Image 2.1多图参考生图编辑｜智能提示词工作流_2108439442263461890.json, 图片生成/文生图/Qwen-Image-2.1 加速简洁版，中文繁体招牌王_2111938255540285442.json, 图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_320

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json、图片生成/文生图/Qwen Image 2.1文生图编辑一体化｜抠图扩图局部重绘多图融合｜全自动扩写提示词_2112121620461608962.json、图片生成/文生图/Qwen Image 2.1文生多图像编辑一体化工作流，文生图图生图处理方案_2106487983930175490.json、图片生成/文生图/Qwen-Image 2.1多图参考生图编辑｜智能提示词工作流_2108439442263461890.json、图片生成/文生图/Qwen-Image-2.1 加速简洁版，中文繁体招牌王_2111938255540285442.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Text_Box`
- `EmptyLatentImage`
- `GoohaiRatioAndResolution`
- `GoohaiRouteBlocker`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImagePromptOptimizer`
- `RestoreQwenImage21GH`
- `SaveImage`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `LoadImageGoohai` —— 4/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `GoohaiAnyExists` —— 1/6 个有
- `GoohaiDisplayAny` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `easy ifElse` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
