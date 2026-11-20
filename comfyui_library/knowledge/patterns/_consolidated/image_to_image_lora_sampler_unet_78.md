---
name: image_to_image_lora_sampler_unet_78
type: Image To Image
frequency: 9
level: strong
coverage: 0.946889
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2511可视化重打光·自由调节灯光_2017606636478664705.json, 图片生成/图生图/RH-PSAPI插件用-_图生图edit2511_2068683270535081985.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+打光_2010914134002503681.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+重打光+选视角_2011254283882205186.json, 图片生成/图生图/双图编辑-图片人物替换-AIGC大赏-修改_2090115164480827393.json, 图片生成/图生图/双图编辑-图片人物替换-AIGC大赏_2043255864382988289.json, 图片生成/图生图/提示词替换人物_2111667142767763458.json, 图片生成/文生图/解说漫-人物拼接-2人_2057418782854967297.json, 图片生成/文生图/解说漫-人物拼接-3人_2058559683757170689.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_78

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2511可视化重打光·自由调节灯光_2017606636478664705.json、图片生成/图生图/RH-PSAPI插件用-_图生图edit2511_2068683270535081985.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+打光_2010914134002503681.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+重打光+选视角_2011254283882205186.json、图片生成/图生图/双图编辑-图片人物替换-AIGC大赏-修改_2090115164480827393.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 7/9 个有
- `SeedVR2LoadDiTModel` —— 6/9 个有
- `SeedVR2LoadVAEModel` —— 6/9 个有
- `SeedVR2VideoUpscaler` —— 6/9 个有
- `ImageConcanate` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `CompressImages` —— 3/9 个有
- `ImageScaleBy` —— 3/9 个有
- `QwenMultiangleLightningNode` —— 3/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `easy saveText` —— 2/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `QwenMultiangleCameraNode` —— 1/9 个有
- `easy imageScaleDownToSize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
