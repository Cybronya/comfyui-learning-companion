---
name: image_to_image_sampler_unet_vae_60
type: Image To Image
frequency: 4
level: strong
coverage: 0.814
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, QwenMultiangleLightningNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177.json, 平台全量/千问可视灯光调节_2020709093387800577.json, 平台全量/图像重打光_2016413813658099714.json, 平台全量/智能摄影机 多角色拍摄 镜头自动多视角 可视化灯光调节 重新打光lora强化版  qwen_imag_2013791785939636226.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177.json、平台全量/千问可视灯光调节_2020709093387800577.json、平台全量/图像重打光_2016413813658099714.json、平台全量/智能摄影机 多角色拍摄 镜头自动多视角 可视化灯光调节 重新打光lora强化版  qwen_imag_2013791785939636226.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `QwenMultiangleLightningNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `Light-Tool: RGB2Hex` —— 1/4 个有
- `NumberClamp` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SimpleMathSlider+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
