---
name: image_to_image_lora_sampler_unet_64
type: Image To Image
frequency: 9
level: strong
coverage: 0.879333
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/☯️qwen姿态迁移_1972199397960445953.json, 图片生成/图生图/☯️千问QUYI-DIY换装流_1978128358280159234.json, 图片生成/图生图/人物动作修改 姿势参考 动作修改_1998944623194165250.json, 图片生成/图生图/千问Edit2509图像编辑姿势迁移版_1972903574260879362.json, 图片生成/图生图/图片编辑姿势完美迁移_1970415639292747778.json, 图片生成/图生图/🌙千问2509人物姿势强化 完美迁移【最强版】🌙_1978831165643722754.json, 图片生成/图生图/🥯千问2509人物姿势完美迁移【姿势强化】🥯_1971739399983722497.json, 图片生成/图生图/🥯千问Edit 2509版 多图稳定编辑版🥯_1971769285058162689.json, 图片生成/图生图/🥯千问新王炸！2509模型图片姿势完美迁移🥯_1970302455412125698.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_64

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/☯️qwen姿态迁移_1972199397960445953.json、图片生成/图生图/☯️千问QUYI-DIY换装流_1978128358280159234.json、图片生成/图生图/人物动作修改 姿势参考 动作修改_1998944623194165250.json、图片生成/图生图/千问Edit2509图像编辑姿势迁移版_1972903574260879362.json、图片生成/图生图/图片编辑姿势完美迁移_1970415639292747778.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `AIO_Preprocessor` —— 7/9 个有
- `CR Text` —— 7/9 个有
- `StringFunction|pysssss` —— 6/9 个有
- `RH_Captioner` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `ImitationHueNode` —— 4/9 个有
- `Note Plus (mtb)` —— 3/9 个有
- `Display Any (rgthree)` —— 1/9 个有
- `GLM_Vision_ImageToPrompt` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
