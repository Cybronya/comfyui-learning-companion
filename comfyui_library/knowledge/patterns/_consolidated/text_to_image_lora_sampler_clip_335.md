---
name: text_to_image_lora_sampler_clip_335
type: Text To Image
frequency: 6
level: strong
coverage: 0.8635
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594.json, 图片生成/图生图/Qwen image2.1人物写真套图｜同角色多场景成套出图｜写真集批量生产_2112093588367691778.json, 图片生成/图生图/Qwen image2.1换头换脸｜注释自带模型LORA下载链接_2111328917192798209.json, 图片生成/图生图/Qwen2.1多图编辑工作流 多张输入精准改图_2105364467491106818.json, 图片生成/图生图/Qwen2.1多图编辑工作流｜局部重绘抠图样样精通_2105245280928092162.json, 图片生成/图生图/Qwenimage2.1漫转真加换头加写真 动漫转真人方案_2109717052633206786.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_335

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594.json、图片生成/图生图/Qwen image2.1人物写真套图｜同角色多场景成套出图｜写真集批量生产_2112093588367691778.json、图片生成/图生图/Qwen image2.1换头换脸｜注释自带模型LORA下载链接_2111328917192798209.json、图片生成/图生图/Qwen2.1多图编辑工作流 多张输入精准改图_2105364467491106818.json、图片生成/图生图/Qwen2.1多图编辑工作流｜局部重绘抠图样样精通_2105245280928092162.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `Anything Everywhere3` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `ProcessString` —— 3/6 个有
- `RHLLMChatNode` —— 3/6 个有
- `easy promptLine` —— 3/6 个有
- `RH_DLSS5Enhance` —— 2/6 个有
- `VOSR2ModelLoader` —— 2/6 个有
- `VOSR2Upscale` —— 2/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
