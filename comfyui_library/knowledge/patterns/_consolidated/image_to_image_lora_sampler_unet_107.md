---
name: image_to_image_lora_sampler_unet_107
type: Image To Image
frequency: 7
level: strong
coverage: 0.859714
common_nodes: [CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/8步加速-QwenEdit位置偏移解决方案_1968478135140397058.json, 图片生成/图生图/QwenEdit 小志版与原版一致性对比_2073056256641822721.json, 图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json, 图片生成/图生图/QwenEdit-万物竖中指一致性图像编辑V1_1968543069031288833.json, 图片生成/图生图/QwenEdit-电商服装人台V1（不支持真人）_1968545752215629825.json, 图片生成/图生图/QwenEdit偏移问题解决方案_1965093253525684225.json, 图片生成/图生图/（志佬开源）QwenEdit一致性图像编辑V2_1968246710134812674.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/8步加速-QwenEdit位置偏移解决方案_1968478135140397058.json、图片生成/图生图/QwenEdit 小志版与原版一致性对比_2073056256641822721.json、图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json、图片生成/图生图/QwenEdit-万物竖中指一致性图像编辑V1_1968543069031288833.json、图片生成/图生图/QwenEdit-电商服装人台V1（不支持真人）_1968545752215629825.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 6/7 个有
- `CR Prompt Text` —— 4/7 个有
- `ImageConcanate` —— 4/7 个有
- `TextEncodeQwenImageEdit` —— 4/7 个有
- `CLIPTextEncode` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `seed _O` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `NunchakuQwenImageDiTLoader` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta57 | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta57，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（26/7 个样本）：Steps较低可能导致细节不足
