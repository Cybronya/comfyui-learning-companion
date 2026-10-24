---
name: image_to_image_lora_sampler_unet_57
type: Image To Image
frequency: 10
level: strong
coverage: 0.8942
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509模特换装工作流_2003380174030868482.json, 图片生成/图生图/Qwen Image Edit  三图融合_1962314713319325698.json, 图片生成/图生图/Qwen-Image-Edit 2509：冬日萌宠童话，一键入画，定格魔法瞬间！_1987879653480271873.json, 图片生成/图生图/Qwen2511+模特换脸_2003793177066782722.json, 图片生成/图生图/qwen-edit-2509三图万物迁移_1993203591836008450.json, 图片生成/图生图/☯️qwen姿态迁移_1972199397960445953.json, 图片生成/图生图/人物动作修改 姿势参考 动作修改_1998944623194165250.json, 图片生成/图生图/千问Edit2509图像编辑姿势迁移版_1972903574260879362.json, 图片生成/图生图/🌙千问2509人物姿势强化 完美迁移【最强版】🌙_1978831165643722754.json, 图片生成/图生图/🥯千问2509人物姿势完美迁移【姿势强化】🥯_1971739399983722497.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_57

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509模特换装工作流_2003380174030868482.json、图片生成/图生图/Qwen Image Edit  三图融合_1962314713319325698.json、图片生成/图生图/Qwen-Image-Edit 2509：冬日萌宠童话，一键入画，定格魔法瞬间！_1987879653480271873.json、图片生成/图生图/Qwen2511+模特换脸_2003793177066782722.json、图片生成/图生图/qwen-edit-2509三图万物迁移_1993203591836008450.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 9/10 个有
- `TextEncodeQwenImageEditPlus` —— 9/10 个有
- `TextEncodeQwenImageEdit` —— 8/10 个有
- `CR Text` —— 7/10 个有
- `ImageConcanate` —— 7/10 个有
- `RH_Captioner` —— 6/10 个有
- `AIO_Preprocessor` —— 5/10 个有
- `StringFunction|pysssss` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `ImitationHueNode` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `PIP_图像联结` —— 2/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `Display Any (rgthree)` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `String` —— 1/10 个有
- `easy anythingIndexSwitch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 10 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
