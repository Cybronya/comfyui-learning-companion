---
name: text_to_image_lora_sampler_clip_306
type: Text To Image
frequency: 6
level: strong
coverage: 0.876667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1透明背景抠图，PNG通道输出图生图专用工作流_2102867983600283649.json, 图片生成/图生图/Qwen Image 2.1配件编辑实测｜换配饰改道具轻松搞定_2103083517977645057.json, 图片生成/图生图/Qwen Image2.1强化抠图 精准移除遮挡输出完美PNG通道_2104659451750993922.json, 图片生成/图生图/Qwen Image2.1精准抠图移除遮挡 透明背景精准生成_2105404738362757121.json, 图片生成/图生图/Qwen image 2.1心宝溶图打光｜18种光效11种光照方向｜产品图光影自由调_2112107722241044481.json, 图片生成/图生图/心宝全能打光18种光效11向｜溶图打光一板搞定_2111300395590053890.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_306

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1透明背景抠图，PNG通道输出图生图专用工作流_2102867983600283649.json、图片生成/图生图/Qwen Image 2.1配件编辑实测｜换配饰改道具轻松搞定_2103083517977645057.json、图片生成/图生图/Qwen Image2.1强化抠图 精准移除遮挡输出完美PNG通道_2104659451750993922.json、图片生成/图生图/Qwen Image2.1精准抠图移除遮挡 透明背景精准生成_2105404738362757121.json、图片生成/图生图/Qwen image 2.1心宝溶图打光｜18种光效11种光照方向｜产品图光影自由调_2112107722241044481.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `ComfySwitchNode` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `Text Multiline` —— 4/6 个有
- `XinbaoImageStandardizer` —— 4/6 个有
- `SaveImageAdvanced` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `Text Concatenate` —— 2/6 个有
- `XinbaoLightingCompanion` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Float` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `QwenImage21PromptEnhancerT8` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `TextCombinerTwo` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

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
