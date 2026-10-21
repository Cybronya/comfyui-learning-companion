---
name: text_to_image_upscale_lora_sampler_28
type: Text To Image
frequency: 4
level: strong
coverage: 0.855
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Image Remove Alpha JK, ImageApplyLUT+, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530.json, 图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA XM触发词画质提升方案_2103227411071590401.json, 图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018.json, 图片生成/文生图/Qwen Image 2.1全能文生图4K放大处理生成工具_2102464269244780545.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530.json、图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA XM触发词画质提升方案_2103227411071590401.json、图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018.json、图片生成/文生图/Qwen Image 2.1全能文生图4K放大处理生成工具_2102464269244780545.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Remove Alpha JK`
- `ImageApplyLUT+`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Lora Loader Stack (rgthree)` —— 3/4 个有
- `PlaySound|pysssss` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `easy imageChooser` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `QwenImage21BlockCacheT8` —— 1/4 个有
- `QwenImage21SageAttentionT8` —— 1/4 个有
- `QwenImage21SpectrumT8` —— 1/4 个有
- `RegexExtract` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有
- `StringFormat` —— 1/4 个有
- `TextGenerate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
